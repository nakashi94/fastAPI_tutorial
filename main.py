from typing import Optional
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None


"""返り値の例
{
    "name": "T-shirt",
    "descrition": "This is a T-shirt",
    "price": 1000,
    "tax": 1.1,
}
"""

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


@app.get("/countries/")  # パスパラメータとクエリパラメータ
# asyncは非同期処理
async def country(country_name: Optional[str] = None, city_name: Optional[str] = None):
    return {
        "country_name": country_name,
        "city_name": city_name
    }
"""


@app.post("/item/")
async def create_item(item: Item):
    return {"message": f"{item.name}は税込み価格{int(item.price*item.tax)}"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
