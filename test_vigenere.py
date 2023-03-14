from crypto_app.vigenerecipher_algo import VigenereCipher

def client():
    app = VigenereCipher()
    with app.test_client() as client:
        yield client

def test_vigenere_cipher_homepage(client):
    """Test the homepage of the Vigenere Cipher blueprint."""
    response = client.get('/vigenerecipher')
    assert response.status_code == 200
    assert "Vigenère Cipher" in response.data

def test_vigenere_cipher_encryption(client):
    msg = "Hello world"
    key = "key"
    response = client.post('/vigenerecipher/encryption', data={'message': msg, 'key_area': key})
    assert response.status_code == 200
    assert b"Encrypted message:" in response.data

def test_vigenere_cipher_decryption(client):
    msg = "Sgmae Sxqmd"
    key = "key"
    response = client.post('/vigenerecipher/decryption', data={'message': msg, 'key_area': key})
    assert response.status_code == 200
    assert b"Decrypted message:" in response.data
