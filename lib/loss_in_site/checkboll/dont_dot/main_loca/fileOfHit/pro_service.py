import phonenumbers
import opencage
import folium
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
def s_pro_location(phoneNumber):
    service_pro = phonenumbers.parse(phoneNumber)
    s_pro = carrier.name_for_number(service_pro, "en")
    print("Operator Name : {}".format(s_pro))
