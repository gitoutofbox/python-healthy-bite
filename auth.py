from jose import jwt, JWTError, ExpiredSignatureError
from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv
load_dotenv()
import os
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2Schema = OAuth2PasswordBearer(tokenUrl="login")

JWT_SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRY_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRY_MINUTES"))

#token create
def createToken(data:dict):
    toEncode = data.copy()
    expiry = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRY_MINUTES)
    toEncode.update({"exp": expiry})
    encodedJWT = jwt.encode(toEncode, JWT_SECRET_KEY, algorithm=ALGORITHM)
    return encodedJWT

def verifyToken(token: str = Depends(oauth2Schema)):
    if not token:
        raise HTTPException(status_code=401, detail="Missing token")
    print ('token' + token)
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token JWT Error")
