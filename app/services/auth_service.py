from fastapi import Request, HTTPException
import base64

def hash_password(password: str) -> str:
    password_bytes = password.encode('utf-8')
    base64_bytes = base64.b64encode(password_bytes)
    base64_password = base64_bytes.decode('utf-8')
    return base64_password


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return hash_password(plain_password) == hashed_password


def get_user_id_by_cookie(request: Request) -> int:
    try:
        session_id = request.cookies.get("session_id")
        
        if session_id is None:
            raise ValueError("Session ID not found")
        
        user_id = base64.b64decode(session_id.encode()).decode('utf-8')
        
        return int(user_id)
    except Exception as e:
        raise HTTPException(status_code = 400, detail = f"Invalid session: {str(e)}")