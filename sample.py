import requests
import json


def main():
    url = 'https://2fu3kg.deta.dev/'
    data = {
        "x": 10,
        "y": 5
    }
    res = requests.post(url, json.dumps(data))
    print(res.json())


if __name__ == "__main__":
    main()
