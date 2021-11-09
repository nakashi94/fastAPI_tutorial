from typing import Optional
from fastapi import FastAPI
import uvicorn

app = FastAPI()


"""
@app.get("/countries/japan")
async def japan():  # asyncは非同期処理を実行するために必要
    return {"message": "This is Japan!"}


@app.get("/countries/{country_name}") # パスパラメータ
async def country(country_name: str):  # asyncは非同期処理を実行するために必要
    return {"country_name": country_name}

@app.get("/countries/")  # クエリパラメータ
async def country(country_name: str = "japan", country_num: int = 1):  # asyncは非同期処理を実行するために必要
    return {
        "country_name": country_name,
        "country_num": country_num
    }
"""


@app.get("/countries/")  # パスパラメータとクエリパラメータ
# asyncは非同期処理
async def country(country_name: Optional[str] = None, city_name: Optional[str] = None):
    return {
        "country_name": country_name,
        "city_name": city_name
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
