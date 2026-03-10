from YandexMaps import Zapros
from LocationData import Location
from DataBaseHandler import DataBaseEvents

if __name__ == "__main__":
    
    Zp = Zapros()
    data = Zp.GetCords()
    #Zp.JSONDump(data)

    datajson = Zp.DataGeneral(data, False)
    LD = Location()
    LD.JSONMake(datajson)
    print(datajson)
    #Zp.JSONDump(datajson)