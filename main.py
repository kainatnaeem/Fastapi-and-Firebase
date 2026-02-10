#Uvicorn is the server that runs and serves FastAPI application to users.
import uvicorn
from fastapi import FastAPI
from routes.auth_routes import router as auth_router
from routes.item_routes import router as item_router
app = FastAPI(
    title="Firebase Auth with FastAPI"
)
#Attach all routes to app.
app.include_router(auth_router)
app.include_router(item_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload = True)