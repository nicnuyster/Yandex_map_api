#backend imports
import requests
import json

#local imports
from LocationData import Location   #class for data structure
from YandexKeys import KeyClass     #API key handler

#class for Yk geocoder
class Zapros():

    YK = KeyClass()
    API_KEY = YK.GetKey("geo")
    url = "https://geocode-maps.yandex.ru/v1/"

    # GET
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

    # Data Handl
    def JSONDump(self, data):
        with open('JSONDump.json', 'w') as f:
            json.dump(data, f, indent = 2)
        print("JSON Dumped")
    
    def JSONWrite(self, data):
        with open('JSONWrite.json', 'w') as f:
            f.write(data)
        print("JSON Written")

    def DataGeneral (self, data, debug = False):
        geo_obj = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
        components = geo_obj['metaDataProperty']['GeocoderMetaData']['Address']['Components']

        # точка инвертированна
        coords = geo_obj['Point']['pos']
        longitude, latitude = coords.split(" ")
        country = ""
        province = ""
        locality = ""
        district = ""

        for component in components:
            kind = component['kind']
            name = component['name']

            match kind:
                case 'country':
                    country = name
                case 'province':
                    province = name
                case 'locality':
                    locality = name
                case 'district':
                    district = name
                case _:
                    print("match case error in Zapros.DataWrap()")
        print("general params captured")
        if debug == True:
            print(f"Country - {country}")
            print(f"Province - {province}")
            print(f"Locality - {locality}")
            print(f"District - {district}")
            print(f"Positions - long: {latitude}, lati: {longitude}")
        datajson = {
            
            "country": country,
            "province": province,
            "locality": locality,
            "district": district,
            "latitude": latitude,
            "longitude": longitude,
        }
        return datajson

if __name__ == "__main__":

    Zp = Zapros()
    data = Zp.GetCords(0, 'Байкал')
    #Zp.JSONDump(data)

    datajson = Zp.DataGeneral(data, False)
    LD = Location()
    LD.JSONMake(datajson)
    print(datajson)
    #Zp.JSONDump(datajson)