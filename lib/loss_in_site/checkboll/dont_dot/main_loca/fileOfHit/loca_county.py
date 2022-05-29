import phonenumbers
import opencage
import folium
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
def countyLoca(phoneNumber):
        pepnumber = phonenumbers.parse(phoneNumber)
        global location
        location = geocoder.description_for_number(pepnumber, "en")
        print("County Name   : {}".format(location))

def r_ver_loca ():
    return location