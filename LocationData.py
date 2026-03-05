import json

class Location():
    
    latitude = ""
    longitude = ""
    
    country = ""
    province = ""
    locality = ""
    district = ""

    def JSONMake(self, data):

        data = {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "country": self.country,
            "province": self.province,
            "locality": self.locality,
            "district": self.district
        }
        jsonstr = json.dumps(data)
        return jsonstr
