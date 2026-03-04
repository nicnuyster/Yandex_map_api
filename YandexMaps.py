import requests
import json

from LocationData import Location
from YandexKeys import KeyClass

class Zapros():

    YK = KeyClass()
    API_KEY = YK.GetKey("geo")
    url = "https://geocode-maps.yandex.ru/v1/"

    # 55.75116001409619, 37.6175783034896 - Московский Кремль
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

    
    def DataGeneral(self, data, debug = True):
        
        numb1 = Location()

        geo_obj = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
        components = geo_obj['metaDataProperty']['GeocoderMetaData']['Address']['Components']

        # точка инвертированна
        numb1.position = geo_obj['Point']['pos']
        
        for component in components:
            kind = component['kind']
            name = component['name']

            match kind:
                case 'country':
                    numb1.country = name
                case 'province':
                    numb1.province = name
                case 'locality':
                    numb1.locality = name
                case 'district':
                    numb1.district = name
                case _:
                    print("match case error in Zapros.DataWrap()")
        print("general params captured")
        if debug == True:
            print(f"Country - {numb1.country}")
            print(f"Province - {numb1.province}")
            print(f"Locality - {numb1.locality}")
            print(f"District - {numb1.district}")
            print(f"Position - {numb1.position}")

if __name__ == "__main__":

    Zp = Zapros()
    data = Zp.GetCords()
    #Zp.JSONDump(data)
    Zp.DataGeneral(data)