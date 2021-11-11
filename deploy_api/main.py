from fastapi import FastAPI
from pydantic import BaseModel
# import uvicorn


class Data(BaseModel):
    x: int
    y: int


app = FastAPI()


@app.get('/')
def index():
    return {"message": "Hello Data!"}


@app.post('/')
def calc(data: Data):
    z = data.x * data.y
    return {"result": z}


# if __name__ == "__main__":
    # uvicorn.run(app, host="127.0.0.1", port=5000)
