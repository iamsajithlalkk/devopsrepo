from botocore.signers import CloudFrontSigner
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from datetime import datetime, timedelta

KEY_ID = "KV8OSSG5FF654"

with open("private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None
    )

def rsa_signer(message):
    return private_key.sign(
        message,
        padding.PKCS1v15(),
        hashes.SHA1()
    )

cloudfront_signer = CloudFrontSigner(
    KEY_ID,
    rsa_signer
)

url = "https://d3jo45972w4roh.cloudfront.net/KFS_0050000660.pdf"

signed_url = cloudfront_signer.generate_presigned_url(
    url,
    date_less_than=datetime.utcnow() + timedelta(hours=3)
)

print(signed_url)