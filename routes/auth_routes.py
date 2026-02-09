from fastapi import APIRouter, HTTPException
from schemas.auth_schema import SignUpSchema, SignInSchema
from core.firebase import firebase_auth_admin, firebase_auth

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/signup")
async def signup(data: SignUpSchema):
    try:
        firebase_auth_admin.create_user(
            email=data.email,
            password=data.password
        )
        return {"message": "User created successfully"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login")
async def login(data: SignInSchema):
    try:
        user = firebase_auth.sign_in_with_email_and_password(
            data.email,
            data.password
        )

        return {"token": user["idToken"]}

    except:
        raise HTTPException(status_code=400, detail="Invalid credentials")