from database.db import session
from models.user_data import users
from fastapi import HTTPException, status, Request,Depends,Query

class user_login:
    def __call__(self, email_id: str, password:str):
        try:
            result=session.query(users).filter(users.user_email==email_id).first()
            session.close()
            pas = password
            if pas == result.password:
                    return "successfully login"
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