from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .. import models, schemas, utils, oauth2
from ..database import get_db

router = APIRouter(
  tags=["Authentication"]
)

@router.post('/login', response_model=schemas.Token)
def login(user_credentials : OAuth2PasswordRequestForm = Depends(),db : Session = Depends(get_db)):
  user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
  if not user:
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Invalid credentials')
  
  if not utils.verify(user_credentials.password , user.password):
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
  
  #create a token 
  access_token = oauth2.create_access_token(data = {"user_id": user.id})
  #return token 
  return {"access_token" : access_token, "token_type" : "bearer"}