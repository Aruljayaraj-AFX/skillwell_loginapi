from database.db import session
from models.user_data import users
from fastapi import HTTPException, status, Request,Depends,Query
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from datetime import datetime, timedelta
from jose import JWTError, jwt

SECRET_KEY = "skillwell"  
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 10
ACCESS_otpEXPIRE_MINUTES = 1

class user_login:
    def __call__(self, email_id: str, password:str):
        try:
            result=session.query(users).filter(users.user_email==email_id).first()
            session.close()
            pas = password
            if pas == result.password:
                expire = datetime.utcnow() + timedelta(minutes=ACCESS_otpEXPIRE_MINUTES)
                payload = {
                "sub": password,
                "exp": expire
                }
                token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
                return {"message": "successfuly_login", "secret": token}
            else:
                return "invalid password"
        except Exception as e:
            session.rollback()
            session.commit()
            raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

class user_add:
     def __call__(self, email_id:str,password1:str):
            new_user = users(user_email = email_id,password=password1)
            try:
                session.add(new_user)
                session.commit()
                session.close() 
                return "successfully_added" 
            except Exception as e:
                session.rollback()  
                raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

class pass_change:
     def __call__(self, email_id:str,new_password:str):
        user = session.query(users).filter(users.user_email == email_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="No matching user found.")
        try:
            user.password=new_password
            session.commit() 
            session.close()
            return "successfully_changed"
        except Exception as e:
            session.rollback()
            raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
        

class c_Authorization(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(c_Authorization, self).__init__(auto_error=auto_error)
    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if not credentials:
            raise HTTPException(status_code=403, detail="Invalid authorization code")
        try:
            payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
            if "sub" not in payload:
                raise HTTPException(status_code=403, detail="Invalid token payload")
            token = payload["sub"]
            man_user = session.query(users).filter(users.password == token).first()
            if man_user is None:
                raise HTTPException(status_code=403, detail="User not found")
            return payload  
        except JWTError:
            raise HTTPException(status_code=403, detail="Invalid or expired token")
        finally:
            session.close()