import phonenumbers
import opencage
import folium
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
latt = ""
lngg = ""
locationn = ""

file_local = ""
def output_map (lat, lng, location): 

    global latt, lngg, locationn
    latt = lat
    lngg = lng
    locationn = location
    global file_local
    #file_local = myMap

def outmapfile ():
    myMap = folium.Map(location = [latt, lngg], zoom_start= 9)
    folium.Marker([latt, lngg], popup=locationn).add_to(myMap)
    return myMap.save('loactionFile.html') 