from src.repository.database import db

class Payment(db.Model):
    # id, value, paid, bank_payment_id, qrcode, expires_at
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float, nullable=False)
    paid = db.Column(db.Boolean, default=False)
    bank_payment_id = db.Column(db.Integer, nullable=True)
    qrcode = db.Column(db.String(255), nullable=True)
    expires_at = db.Column(db.DateTime)

    def to_dict(self):
        return {
            'id': self.id,
            'value': self.value,
            'paid': self.paid,
            'bank_payment_id': self.bank_payment_id,
            'qrcode': self.qrcode,
            'expires_at': self.expires_at
        }