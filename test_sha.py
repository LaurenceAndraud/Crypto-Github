from crypto_app.sha_algo import SHA


def test_sha_encrypt():

    sha_obj = SHA()
    msg = "message"
    expected_encrypted = "f8daf57a3347cc4d6b9d575b31fe6077e2cb487f60a96233c08cb479dbf31538cc915ec6d48bdbaa96ddc1a16db4f4f96f37276cfcb3510b8246241770d5952c"
    encrypted = sha_obj.encrypt(msg)

    assert encrypted == expected_encrypted

def test_sha_encrypt_error():

    sha_obj = SHA()
    message = 12345
    expected_result = False
    result = sha_obj.encrypt(message)

    assert result == expected_result

