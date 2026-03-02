import requests
from YandexKeys import KeyClass
import json

class Zapros():

    YK = KeyClass()
    API_KEY = YK.GetKey("geo")
    url = "https://geocode-maps.yandex.ru/v1/"

    def GetCords(self, Cords = 0, Addr = "Москва, Кремль"):
        
        params = {
            "apikey": self.API_KEY,
            "geocode": Addr,
            "format": "json"
        }
        response = requests.get(self.url, params=params)
        print("request send")
        return response.json() #returns dict

    def JSONDump(self, data):
        with open('JSONDump.json', 'w') as f:
            json.dump(data, f, indent = 2)
        print("JSON Dumped")
    
    def JSONWrite(self, data):
        with open('JSONWrite.json', 'w') as f:
            f.write(data)
        print("JSON Written")

    def DataWrap(self, data):
        print("yes ."
        "")

if __name__ == "__main__":

    Zp = Zapros()
    data = Zp.GetCords()
    Zp.JSONDump(data)