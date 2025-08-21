from fastapi import APIRouter, HTTPException,Depends,Query
from services.user_check import user_login,user_add,pass_change

router= APIRouter()

@router.get("/login")
async def login(res:str=Depends(user_login())):
    return res

@router.get("/add_user")
async def add_user(adduser:str=Depends(user_add())):
    return adduser

@router.get("/password_change")
async def pass_ch(newpass:str=Depends(pass_change())):
    return newpass