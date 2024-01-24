from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend
import os

def AES(key,iv):
    f=open(os.path.join(os.getcwd()+"/Segments","0.txt"),"r")
    content=f.read()
    f.close()
    content=content.encode()
    b=len(content)
    if(b%16!=0):
        while(b%16!=0):
            content+=" ".encode()
            b=len(content)
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    cont = encryptor.update(content) + encryptor.finalize()
    open(os.path.join(os.getcwd()+"/Segments","0.txt"),"wb").close()
    f=open(os.path.join(os.getcwd()+"/Segments","0.txt"),"wb")
    f.write(cont)
    f.close();

def generate_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    # Save private key
    with open(os.path.join(os.getcwd(), "private_key.pem"), "wb") as key_file:
        key_file.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))

    # Save public key
    public_key = private_key.public_key()
    with open(os.path.join(os.getcwd(), "public_key.pem"), "wb") as key_file:
        key_file.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

# Generate key pair
generate_key_pair()

def RSA(key, iv):
    # Load the public key
    with open(os.path.join(os.getcwd() + "/public_key.pem"), "rb") as key_file:
        public_key = serialization.load_pem_public_key(key_file.read(), backend=default_backend())

    f = open(os.path.join(os.getcwd() + "/Segments", "1.txt"), "r")
    content = f.read()
    f.close()

    # Encrypt the content with RSA
    encrypted_content = public_key.encrypt(
        content.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    open(os.path.join(os.getcwd() + "/Segments", "1.txt"), "wb").close()
    f = open(os.path.join(os.getcwd() + "/Segments", "1.txt"), "wb")
    f.write(encrypted_content)
    f.close()


def TrippleDES(key,iv):
    f=open(os.path.join(os.getcwd()+"/Segments","2.txt"),"r");
    content=f.read();
    f.close();
    content=content.encode()
    b=len(content);
    if(b%8!=0):
        while(b%8!=0):
            content+=" ".encode()
            b=len(content);
    backend = default_backend();
    cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv), backend=backend);
    encryptor = cipher.encryptor();
    cont = encryptor.update(content) + encryptor.finalize();
    open(os.path.join(os.getcwd()+"/Segments","2.txt"),"w").close();
    f=open(os.path.join(os.getcwd()+"/Segments","2.txt"),"wb");
    f.write(cont);
    f.close();


def HybridCryptKeys():
    pass


