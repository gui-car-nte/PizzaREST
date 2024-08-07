import base64

def hash_password(password: str) -> str:
    password_bytes = password.encode('utf-8')
    base64_bytes = base64.b64encode(password_bytes)
    base64_password = base64_bytes.decode('utf-8')
    return base64_password

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return hash_password(plain_password) == hashed_password
