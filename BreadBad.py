# Created by: DtxdF
# Version: 1.2
# -*- coding: utf-8 -*-

import os
import geoip
from time import sleep
try:
	from colorama import *
	init()
except:
	print "[!] Error, Installing colorama, since it does not have it ..."
	os.system("pip install colorama")
	print "[!] Run again, BreadBad"
	exit()
	
# Config vars
	
debug_logo = "BreadBad"
ipadress = None
geoipamy = True
	
# Colors

class color:
	
	green = Fore.LIGHTGREEN_EX
	yellow = Fore.LIGHTYELLOW_EX
	red = Fore.LIGHTRED_EX
	ble = Fore.LIGHTBLUE_EX+"["+Fore.RESET+"*"+Fore.LIGHTBLUE_EX+"]"+Fore.RESET+" "
	adv = Fore.LIGHTYELLOW_EX+"["+Fore.RESET+"!"+Fore.LIGHTYELLOW_EX+"]"+Fore.RESET+" "
	error = Fore.LIGHTRED_EX+"["+Fore.RESET+"-"+Fore.LIGHTRED_EX+"]"+Fore.RESET+" "
	reset = Fore.RESET

print "\n"
		
print color.yellow+"BreadBad: " + color.reset + "An ip geolocation tool by means of a console, written in python and fully functional thanks to the api of: http://ip-api.com/json/\n"

print color.ble+"Created by: " + color.yellow+"DtxdF"+color.reset+"\n"
		
print "Help Main:"
print "#### ####"

print """
	IPAddress \t::\t The command to define the ip to geolocate
	Country \t::\t See the country of the defined ip
	City \t\t::\t See the city of the defined ip
	Country_Code \t::\t See the country code of the defined ip
	ISP \t\t::\t See the internet service protocol (ISP) of the defined ip
	ORG \t\t::\t See the company organization of the defined ip
	latitude \t::\t See the latitude of the defined ip
	longitude \t::\t See the length of the defined ip
	Query \t\t::\t See the query of the defined ip
	Association \t::\t See the association of the company of the defined ip
	region \t\t::\t See the region of the defined ip
	region_name \t::\t See the name belonging to the defined ip
	TimeZone \t::\t See the time zone of the defined ip
	Google_Maps \t::\t Show the link of google maps
	zipCode \t::\t Show the zip code
	all_information ::\t Show the all information from the ip address
"""
		
print "\nGeolocation to you:"
print "########### ## ###"
		
try:
		
	get_geo = geoip.geolocation("localme")
	get_geo.start()
			
	ass = get_geo.association()
	country = get_geo.country()
	city = get_geo.city()
	countryCode = get_geo.countryCode()
	isp = get_geo.isp()
	lat = get_geo.latitude()
	lon = get_geo.longitude()
	org = get_geo.organization()
	query = get_geo.query()
	region = get_geo.region()
	regionName = get_geo.regionName()
	timezone = get_geo.timezone()
	zipcode = get_geo.zipCode()
	google_maps = get_geo.google_maps()
	
	list_isp_query = {country,city,countryCode,isp,org,lat,lon,query,ass,region,regionName,timezone,zipcode,google_maps}
			
	for i in list_isp_query:
		if i == '':
			i = None
			
	print "\n"
	print "\tCountry(%s) \t\t:: %s" % (str(countryCode),str(country))
	print "\tCity \t\t\t:: %s" % (str(city))
	print "\tISP \t\t\t:: %s" % (str(isp))
	print "\tOrganization \t\t:: %s" % (str(org))
	print "\tLatitude \t\t:: %s" % (str(lat))
	print "\tLongitude \t\t:: %s" % (str(lon))
	print "\tQuery \t\t\t:: %s" % (str(query))
	print "\tAssociation \t\t:: %s" % (str(ass))
	print "\tRegion \t\t\t:: %s" % (str(region))
	print "\tRegion Name \t\t:: %s" % (str(regionName))
	print "\tTime Zone \t\t:: %s" % (str(timezone))
	print "\tZip Code \t\t:: %s" % (str(zipcode))
	print "\tGoogle maps \t\t:: %s" % (str(google_maps))
	print "\n"
				
except EOFError:
	print color.adv+"Error in the connection ..."
except Exception as a:
	print color.error+"Unknown error: %s" % str(a)
		
while True:
	
	try:
		
		debug = raw_input(color.yellow + "[" + debug_logo + "]" + color.red + " > " + color.reset)
		
		if not debug:
			continue
			
		if debug.split()[0].lower() == 'ipaddress':
			ipadress = debug.split()[1]
			iptolocate = geoip.geolocation(ipadress)
			try:
				iptolocate.start()
			except geoip.statusip as a:
				print color.error+"Error: %s" % (str(a))
		
		if ipadress:
			if debug.split()[0].lower() == 'country':
				print color.ble+"\tCountry: %s" % color.green+str(iptolocate.country())+color.reset
			elif debug.split()[0].lower() == 'city':
				print color.ble+"\tCity: %s" % color.green+str(iptolocate.city())+color.reset
			elif debug.split()[0].lower() == 'country_code':
				print color.ble+"\tCountry Code: %s" % color.green+str(iptolocate.countryCode())+color.reset
			elif debug.split()[0].lower() == 'isp':
				print color.ble+"\tISP: %s" % color.green+str(iptolocate.isp())+color.reset
			elif debug.split()[0].lower() == 'org':
				print color.ble+"\tOrganization: %s" % color.green+str(iptolocate.organization())+color.reset
			elif debug.split()[0].lower() == 'latitude':
				print color.ble+"\tLatitude: %s" % color.green+str(iptolocate.latitude())+color.reset
			elif debug.split()[0].lower() == 'longitude':
				print color.ble+"\tLongitude: %s" % color.green+str(iptolocate.longitude())+color.reset
			elif debug.split()[0].lower() == 'query':
				print color.ble+"\tQuery: %s" % color.green+str(iptolocate.query())+color.reset
			elif debug.split()[0].lower() == 'association':
				print color.ble+"\tAssociation: %s" % color.green+str(iptolocate.association())+color.reset
			elif debug.split()[0].lower() == 'region':
				print color.ble+"\tRegion: %s" % color.green+str(iptolocate.region())+color.reset
			elif debug.split()[0].lower() == 'region_name':
				print color.ble+"\tRegion name: %s" % color.green+str(iptolocate.regionName())+color.reset
			elif debug.split()[0].lower() == 'timezone':
				print color.ble+"\tTime Zone: %s" % color.green+str(iptolocate.timezone())+color.reset
			elif debug.split()[0].lower() == 'google_maps':
				print color.ble+"\tGoogle maps: %s" % color.green+str(iptolocate.google_maps())+color.reset
			elif debug.split()[0].lower() == 'zipcode':
				print color.ble+"\tZip Code: %s" % color.green+str(iptolocate.zipCode())+color.reset
			elif debug.split()[0].lower() == 'all_information':
				welcome = "\nGeolocation to %s:" % (str(ipadress))
				print welcome
				welcome_char = ""
				for i in range(int(len(welcome))-1):
					welcome_char += "#"
				print welcome_char+"\n"
							
				ass = iptolocate.association()
				country = iptolocate.country()
				city = iptolocate.city()
				countryCode = iptolocate.countryCode()
				isp = iptolocate.isp()
				lat = iptolocate.latitude()
				lon = iptolocate.longitude()
				org = iptolocate.organization()
				query = iptolocate.query()
				region = iptolocate.region()
				regionName = iptolocate.regionName()
				timezone = iptolocate.timezone()
				zipcode = iptolocate.zipCode()
				google_maps = iptolocate.google_maps()
					
				list_isp_query = {country,city,countryCode,isp,org,lat,lon,query,ass,region,regionName,timezone,zipcode,google_maps}
							
				for i in list_isp_query:
					if i == '':
						i = None
							
				print "\n"
				print "\tCountry(%s) \t\t:: %s" % (str(countryCode),str(country))
				print "\tCity \t\t\t:: %s" % (str(city))
				print "\tISP \t\t\t:: %s" % (str(isp))
				print "\tOrganization \t\t:: %s" % (str(org))
				print "\tLatitude \t\t:: %s" % (str(lat))
				print "\tLongitude \t\t:: %s" % (str(lon))
				print "\tQuery \t\t\t:: %s" % (str(query))
				print "\tAssociation \t\t:: %s" % (str(ass))
				print "\tRegion \t\t\t:: %s" % (str(region))
				print "\tRegion Name \t\t:: %s" % (str(regionName))
				print "\tTime Zone \t\t:: %s" % (str(timezone))
				print "\tZip Code \t\t:: %s" % (str(zipcode))
				print "\tGoogle maps \t\t:: %s" % (str(google_maps))
				print "\n"
		else:
			print color.adv+"The ip address is not defined."
			
	except EOFError:
		print color.adv+"Invalid key ..."
	except IndexError:
		print color.adv+"A value in some variable is missing ..."
	except KeyboardInterrupt:
		print color.adv+"CTRL-C ... Quiting."
		try:
			sleep(3.5)
			quit()
		except KeyboardInterrupt:
			quit()
	except Exception as a:
		print color.error+str(a)
