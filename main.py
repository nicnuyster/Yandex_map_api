from YandexMaps import Zapros
from LocationData import Location
from DataBaseHandler import DataBaseEvents

if __name__ == "__main__":
    
    Zp = Zapros()
    data = Zp.GetCords(0, "Иркутск")
    #Zp.JSONDump(data)

    LD = Location()
    datajson = Zp.DataGeneral(data, LD, False)
    #LD.JSONMake(datajson)
    #print(datajson)
    #Zp.JSONDump(datajson)

    DBHdlr = DataBaseEvents()
    DBHdlr.createtable()
    DBHdlr.insertiteration(LD)
    #DBHdlr.deletetable("locations")