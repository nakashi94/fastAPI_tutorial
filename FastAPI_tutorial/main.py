from typing import Optional, List
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel, Field

# classの定義


class ShopInfo(BaseModel):
    name: str
    location: str


class Item(BaseModel):
    name: str = Field(min_length=4, max_length=12)
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None


class Data(BaseModel):
    shop_info: Optional[ShopInfo]
    items: List[Item]


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

@app.post("/item/")
async def create_item(item: Item):
    return {"message": f"{item.name}は税込み価格{int(item.price*item.tax)}"}
"""


@app.post("/")
async def index(data: Data):
    return {"data": data}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
