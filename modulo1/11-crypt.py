from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend

with open("public_key.pem", "rb") as public_file:
    public_key = serialization.load_pem_public_key(public_file.read(),
        backend=default_backend()
    )

message = "Esta é a mensagem original.".encode("utf-8")
encrypted_message = public_key.encrypt(
    message, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), 
                          algorithm=hashes.SHA256(), label=None))

with open("mensagem_encriptada.bin", "wb") as encrypted_file:
    encrypted_file.write(encrypted_message)