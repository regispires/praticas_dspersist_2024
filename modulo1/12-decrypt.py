
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend

with open("private_key.pem", "rb") as private_file:
    private_key = serialization.load_pem_private_key(
        private_file.read(),
        password=b"minha_senha_forte",  # Senha usada para proteger a chave privada
        backend=default_backend()
    )
encrypted_message = open("mensagem_encriptada.bin", "rb").read()

decrypted_message = private_key.decrypt(
    encrypted_message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("Mensagem decriptada:", decrypted_message.decode())