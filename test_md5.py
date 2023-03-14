from crypto_app.md5_algo import MD5

def test_md5_encrypt():

    md5_obj = MD5()
    msg = "message"

    decrypted_msg = md5_obj.encrypt(msg)

    assert decrypted_msg == '78e731027d8fd50ed642340b7c9a63b3'