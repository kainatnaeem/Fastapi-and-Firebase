
import uvicorn
from fastapi import FastAPI
from routes.auth_routes import router as auth_router

app = FastAPI(
    title="Firebase Auth with FastAPI"
)

app.include_router(auth_router)



if __name__ == "__main__":
    uvicorn.run("main:app", reload = True)