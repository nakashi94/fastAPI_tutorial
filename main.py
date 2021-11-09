from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def index():  # asyncは非同期処理を実行するために必要
    return {"message": "Hello World", "user": "test"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
