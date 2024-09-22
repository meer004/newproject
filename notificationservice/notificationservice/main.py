from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session

from notificationservice.db import create_db_and_tables, get_session
from notificationservice.schema  import  UserCreate, UserRead


from notificationservice.models import Notification


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating tables  for notification...")
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

# Initial empty lists to store user data
users = []
email = []
password = []

@app.post("/register_users/", response_model=UserRead)
async def create_user(user: UserCreate, db: Session = Depends(get_session)):
    # Check if email already exists
    if user.email in [user["email"] for user in users]:
        raise HTTPException(status_code=400, detail="Email already exists")
    else:
        #  to Validate password length
        if len(user.password) < 6:
            print("Password must be at least 6 characters long")
        else:
            # Create new user
            new_user = {
                "id": len(users) + 1,
                "email": user.email,
                "password": user.password,
            }
            users.append(new_user)

            return new_user


        

@app.post("/user_login/")
async def user_login(email: str, password: str, db: Session = Depends(get_session)):
    # Find the user by email
    user = await db.query(Notification).filter(Notification.email == email).first()
    if user:
        # Verify the password
        if password == user.password:
            print("Login successful")
            return True
        else:
            print("Invalid password")
            return False
    else:
        print("User not found")
        return False









