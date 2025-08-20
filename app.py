from flask import Flask, jsonify, request, send_file, render_template
from src.repository.database import db
from src.models.payment import Payment
from src.payments.pix import Pix
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'secret123'
db.init_app(app)

@app.route('/payments/pix', methods=['POST'])
def create_pix_payment():
    data = request.get_json()

    # validation
    if 'value' not in data:
        return jsonify({
            'status': 'error',
            'message': 'Value is required'
        }), 400
    
    # expiration time limit 30 minutes
    expires_at = datetime.now() + timedelta(minutes=30)
    
    new_payment = Payment(
        value=data['value'],
        expires_at=expires_at
    )

    pix = Pix()
    data_pix = pix.create_payment()
    new_payment.bank_payment_id = data_pix['bank_payment_id']
    new_payment.qrcode = data_pix['qrcode_url']

    db.session.add(new_payment)
    db.session.commit()

    return jsonify({
        'status': 'success',
        'message': 'Pix payment created successfully',
        'payment': new_payment.to_dict()
    })

# route to get qrcode image
@app.route('/payments/pix/qrcode/<file_name>', methods=['GET'])
def get_qrcode_image(file_name):
    return send_file(f'static/img/{file_name}.png', mimetype='image/png')

@app.route('/payments/pix/confirmation', methods=['POST'])
def confirm_pix_payment():
    return jsonify({
        'status': 'success',
        'message': 'Pix payment confirmed successfully'
    })

@app.route('/payments/pix/<int:payment_id>', methods=['GET'])
def get_pix_payment(payment_id):
    payment = Payment.query.get(payment_id)
    return render_template('payment.html', 
        payment_id=payment.id, 
        value=payment.value, 
        host="http://127.0.0.1:5000", 
        qrcode=payment.qrcode
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)