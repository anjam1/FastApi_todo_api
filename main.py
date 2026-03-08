from fastapi import FastAPI
from routes import todos, users, auth
import models
from database import engine



models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title = "To Do Application"
)
app.include_router(todos.router)
app.include_router(users.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Welcome to Todo Application Built by Anjam Haseeb"}
