import uuid
import qrcode

class Pix:
    def __init__(self):
        pass

    def create_payment(self):
        # create payment in financial institution
        bank_payment_id = str(uuid.uuid4())
    
        # qrcode string
        hash_payment = f'hash_payment_{bank_payment_id}'

        # qrcode image
        qrcode_image = qrcode.make(hash_payment)
        # save qrcode image
        qrcode_image.save(f'static/img/qrcode_{bank_payment_id}.png')

        return {
            'bank_payment_id': bank_payment_id,
            'qrcode_url': f'qrcode_{bank_payment_id}',
        }