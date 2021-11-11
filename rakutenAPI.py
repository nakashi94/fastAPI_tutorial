import requests
import os
from dotenv import load_dotenv

# .envファイルの内容を読み込みます
load_dotenv()

# os.environを用いて環境変数を表示させます
print(os.environ['APP_ID'])

URL = 'https://app.rakuten.co.jp/services/api/Travel/KeywordHotelSearch/20170426'
APP_ID = os.environ['APP_ID']

params = {
    'applicationId': APP_ID,
    'keyword': '沖縄'
}

res = requests.get(URL, params)
print(res.status_code)
# print(res.json()['hotels'])
hotels = res.json()['hotels']
hotel = hotels[0]['hotel'][0]['hotelBasicInfo']
print(hotel['hotelName'])
print(hotel['access'])
address = hotel['address1'] + hotel['address2']
print(address)
