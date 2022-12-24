import requests
from requests import get

class Utils:

    def getiP():
        return get('https://api.ipify.org').content.decode('utf8')

    def getLocation(ip, info):
        response = requests.get(f'https://ipapi.co/{ip}/json/').json()
        if info == 'city':
            city = response.get("city")
            return city
        elif info == 'country_calling_code':
            country_calling_code = response.get("country_calling_code")
            return country_calling_code