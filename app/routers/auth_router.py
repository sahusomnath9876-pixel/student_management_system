from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from app.database import get_db
from app.services import Authentication
from app.schemas import AuthReg, AuthLogin, SignUpResponse, UpdatePassword
import jwt
from app.repos import UserRepo


auth_router = APIRouter(prefix="/auth", tags=["Authentication"])
Oauth_2barer = OAuth2PasswordBearer(tokenUrl="auth/signin")


@auth_router.post("/signin", )
def SignIn(user : AuthLogin, db=Depends(get_db)):
    auth = Authentication(db)

    check_user = auth.SignIn(user.username, user.password)
    token = auth.create_token(check_user)
    return{
        "access_token" : token,
        "token_type" : "Bearer",
        "role" : {check_user.role}
        }


def verify_token(token : str = Depends(Oauth_2barer), db=Depends(get_db)):
    auth = Authentication(db)
    payload = auth.verify_token(token)
    return payload
    

@auth_router.get("/getuser", response_model= SignUpResponse)
def get_user_date(current_user=Depends(verify_token), db=Depends(get_db)):
    user_repo = UserRepo(db)

    user_data = user_repo.get_user(current_user.get("username"))

    return user_data

@auth_router.post("/signup", response_model=SignUpResponse, status_code=201)
def user_signup(user_details : AuthReg, db=Depends(get_db)):
    auth = Authentication(db)

    new_user = auth.SignUp(
        user_details.username, user_details.mobile_no, user_details.email, user_details.name, user_details.city, user_details.password
    )

    return new_user


@auth_router.patch("/reset/password")
def reset_user_password(user : UpdatePassword, db=Depends(get_db)):
    auth = Authentication(db)

    update_password = auth.reset_password(user.username, user.old_password, user.new_password)
    return update_password

