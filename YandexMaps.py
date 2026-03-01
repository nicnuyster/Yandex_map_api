import requests
from YandexKeys import KeyClass

class Response():

    YK = KeyClass()
    API_KEY = YK.GetKey("geo")

    address = "Москва, Кремль"
    url = "https://geocode-maps.yandex.ru/v1/"

    params = {
        "apikey": API_KEY,
        "geocode": address,
        "format": "json"
    }

if __name__ == "__main__":

    Zapros = Response()

    response = requests.get(Zapros.url, params=Zapros.params)
    data = response.json()
    print("yes")
    
    # try:
    #     pos = Zapros.data["response"]["GeoObjectCollection"][0]["GeoObject"]["points"]["pos"]
    #     lon, lat = pos.split()
    #     print(f"Координаты: {lat}, {lon}")
    #     print("yes")
    # except:
    #     print("no")
