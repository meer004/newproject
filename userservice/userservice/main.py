from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlmodel import Session
from userservice.db import create_db_and_tables, get_session
from userservice.schemas import UserCreate, UserRead, TokenResponse, UserDataCreate, UserDataRead, TokenData
from userservices.crud import create_user, get_user_by_email, authenticate_user, create_user_data, get_user_data, refresh_access_token, validate_password
from userservice.auth import create_access_token
from userservice.dp import get_current_user
from userservice.models import User, UserData
from contextlib import asynccontextmanager
from slowapi import Limiter
from slowapi.util import get_remote_address
from userservice.kafka.producer import USER_TOPIC, KafkaProducer, get_kafka_producer
from userservice.kafka import _pb2
from typing import List
import asyncio
from userservice.kafka.consumer import run_consumer

limiter = Limiter(key_func=get_remote_address)

@app.post("/register_users/",response_model=UserRead)
def create_user( user: UserCreate,db:Session = Depends(get_session), kakaProducer: KafkaProducer = Depends(get_kafka_producer)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already exists")
    else:
        if len(user.password) < 6:
            raise HTTPException(status_code=400, detail="Password must be at least 6 characters long")
        else:
            new_user = create_user(db,user=user)
            user_registered = _pb2.UserRegistered(
                user_id = new_user.id,
                email = new_user.email,
                password = new_user.password,
            )
            kakaProducer.send(USER_TOPIC, value=user_registered)
@app.post("/login/", response_model=TokenResponse)
def user_login(request: Request, from_data:OAuth2PasswordRequestForm = Depends(),db:Session = Depends(get_session)):
    # Find the user by email
    user = authenticate_user(Session=db, email=from_data.username, password=from_data.password)
    # Verify the password
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return user
