import requests
from YandexKeys import KeyClass

class Response():

    API_KEY = " "
    def __init__(self):
        YK = KeyClass()
        self.API_KEY = YK.GEO_API_KEY("geo")

    address = "Москва, Кремль"
    url = "https://geocode-maps.yandex.ru/1.x/"
    params = {
        "apikey": API_KEY,
        "geocode": address,
        "format": "json"
    }
    response = requests.get(url, params=params)
    data = response.json()

if __name__ == "__main__":

    Zapros = Response()
    try:
        pos = Zapros.data["response"]["GeoObjectCollection"][0]["GeoObject"]["points"]["pos"]
        lon, lat = pos.split()
        print(f"Координаты: {lat}, {lon}")
    except:
        print("No")