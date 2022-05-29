from lib.loss_in_site.checkboll.dont_dot.main_loca.fileOfHit.lchack_port.keychack import *
import phonenumbers
import opencage
import folium
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
#API_KEY = 
def geomatry_loca(location):
    #geometry location opencageGeocoder
    #onpencageKay = "0ae14a7506fd43b28c4802c0fece048c"
    onpencageKay = "5efc91ba75de4e3eac3819bd50599726"
    geocoder = OpenCageGeocode(onpencageKay)
    query = str(location)
    results = geocoder.geocode(query)
    #print(results)
    global late
    global lnge
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    late = lat
    lnge = lng
    print("Location Code : {},{}\n".format(lat, lng))
    print("     Create a LocationFile.html\n\n")

def re_lat_off ():
        return late
def re_lng_off ():
        return lnge