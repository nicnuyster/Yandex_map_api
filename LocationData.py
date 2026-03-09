import json

class Location():
    
    address = ""
    latitude = ""
    longitude = ""
    
    country = ""
    province = ""
    locality = ""
    district = ""

    def JSONMake(self, data):

        data = {
            "address": self.address,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "country": self.country,
            "province": self.province,
            "locality": self.locality,
            "district": self.district
        }
        jsonstr = json.dumps(data)
        return jsonstr
