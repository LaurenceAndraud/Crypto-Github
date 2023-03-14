from crypto_app.des_algo import DES

def test_des_encrypt():

    des_obj = DES()
    msg = "message"
    key = "secretke"

    encrypted_msg = des_obj.encrypt(msg, key)
    decrypted_msg = des_obj.decrypt(encrypted_msg, key)

    assert decrypted_msg == msg

