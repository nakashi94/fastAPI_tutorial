from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/countries/japan")
async def japan():  # asyncは非同期処理を実行するために必要
    return {"message": "This is Japan!"}


@app.get("/countries/{country_name}")
async def country(country_name: str):  # asyncは非同期処理を実行するために必要
    return {"country_name": country_name}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
