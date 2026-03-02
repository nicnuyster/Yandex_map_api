import requests
from YandexKeys import KeyClass
import json

class Zapros():

    YK = KeyClass()
    API_KEY = YK.GetKey("geo")

    address = "Москва, Кремль"
    url = "https://geocode-maps.yandex.ru/v1/"

    params = {
        "apikey": API_KEY,
        "geocode": address,
        "format": "json"
    }
    response = requests.get(url, params=params)
    data = response.json()

if __name__ == "__main__":

    Zp = Zapros()
    # resp = requests.get(Zp.url, params=Zp.params)
    # data = resp.json()
    print(Zp.data)

    # try:
    #     pos = Zapros.data["response"]["GeoObjectCollection"][0]["GeoObject"]["points"]["pos"]
    #     lon, lat = pos.split()
    #     print(f"Координаты: {lat}, {lon}")
    #     print("yes")
    # except:
    #     print("no")
