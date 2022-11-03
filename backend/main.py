import uvicorn
from fastapi import FastAPI
from core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)


@app.get("/")
def hello_api():
    return {"msg": "Hello API"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8000)
