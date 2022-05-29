import time
from lib.loss_in_site.checkboll.dont_dot.main_loca.fileOfHit.loca_county import *
from lib.loss_in_site.checkboll.dont_dot.main_loca.fileOfHit.pro_service import *
from lib.loss_in_site.checkboll.dont_dot.main_loca.fileOfHit.loca_geo import geomatry_loca, re_lat_off, re_lng_off
from lib.loss_in_site.checkboll.dont_dot.main_loca.fileOfHit.out_map import *
import os
import os.path
def sub_f_local ():
    if os.path.isfile('APIKEY.txt') == False:
        print ("""                
        ==============================================
        #               Create A file                #
        #               APIKEY.txt in                #
        #               Root Location                #
        ==============================================
        """)
        time.sleep(1.3)
        exit()
    else:
        #print ("yes File")
        f = open("APIKEY.txt")
        contents = f.readlines()
        f.close()
        keyline = ""
        for line in contents:
            keyline = line
        if len(keyline) <= 0 :
            print ("""                
        ==============================================
        #                                            #
        #                 No API KEY                 #
        #                                            #
        #   Go To The https://opencagedata.com/api   #
        #                                            #
        ==============================================
            """)
            time.sleep(0.5)
            exit()
        if len(keyline) >= 2 and len(keyline) <= 31 :
            print ("""                
        ==============================================
        #                                            #
        #            Not Belied API KEY              #
        #                                            #
        ==============================================
            """)
            time.sleep(0.5)
            exit()
        else:
            phoneNumber = "+8801998769191" #input("Enter Find Location ")
            #print(phoneNumber)
            #location lib
            #libbee()
            import phonenumbers
            import opencage
            import folium
            from phonenumbers import geocoder
            from phonenumbers import carrier
            from opencage.geocoder import OpenCageGeocode
            #main code
            #county location
            countyLoca(phoneNumber)
            location = r_ver_loca ()
            #service proviter
            s_pro_location(phoneNumber)
            geomatry_loca(location)
            lat = re_lat_off()
            lng = re_lng_off()
            output_map (lat, lng, location)