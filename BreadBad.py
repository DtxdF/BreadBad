# Created by: DtxdF
# -*- coding: utf-8 -*-

import requests
import os
from json import loads
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
	
	green = Fore.GREEN
	yellow = Fore.YELLOW
	red = Fore.RED
	ble = Fore.BLUE+"["+Fore.RESET+"*"+Fore.BLUE+"]"+Fore.RESET+" "
	adv = Fore.YELLOW+"["+Fore.RESET+"!"+Fore.YELLOW+"]"+Fore.RESET+" "
	error = Fore.RED+"["+Fore.RESET+"-"+Fore.RED+"]"+Fore.RESET+" "
	reset = Fore.RESET
	
class geoip:

	def __init__(self, ipaddr, localsh=False):
		
		if not localsh:
			self.ipaddr = ipaddr
		else:
			self.ipaddr = ""
		
	def locate(self):
		
		try:
		
			get_geo = requests.get("http://ip-api.com/json/"+self.ipaddr).text
			
			ass = loads(get_geo)['as']
			country = loads(get_geo)['country']
			city = loads(get_geo)['city']
			countryCode = loads(get_geo)['countryCode']
			isp = loads(get_geo)['isp']
			lat = loads(get_geo)['lat']
			lon = loads(get_geo)['lon']
			org = loads(get_geo)['org']
			query = loads(get_geo)['query']
			region = loads(get_geo)['region']
			regionName = loads(get_geo)['regionName']
			timezone = loads(get_geo)['timezone']
			
			list_isp_query = {country,city,countryCode,isp,org,lat,lon,query,ass,region,regionName,timezone}
			
			for i in list_isp_query:
				if i == '':
					i = None
			
			print "\n"
			print "\tCountry(%s) \t\t:: %s" % (str(countryCode.encode("utf-8")),str(country.encode("utf-8")))
			print "\tCity \t\t\t:: %s" % (str(city.encode("utf-8")))
			print "\tISP \t\t\t:: %s" % (str(isp.encode("utf-8")))
			print "\tOrganization \t\t:: %s" % (str(org.encode("utf-8")))
			print "\tLatitude \t\t:: %s" % (str(lat))
			print "\tLongitude \t\t:: %s" % (str(lon))
			print "\tQuery \t\t\t:: %s" % (str(query.encode("utf-8")))
			print "\tAssociation \t\t:: %s" % (str(ass.encode("utf-8")))
			print "\tRegion \t\t\t:: %s" % (str(region.encode("utf-8")))
			print "\tRegion Name \t\t:: %s" % (str(regionName.encode("utf-8")))
			print "\tTime Zone \t\t:: %s" % (str(timezone.encode("utf-8")))
			print "\n"
				
		except requests.exceptions.ConnectionError:
			print color.error+"Error in the connection ..."
		except requests.exceptions.MissingSchema:
			print color.adv+"I miss the protocol"
		except Exception as a:
			print color.error+"Unknown error: %s" % str(a)
			
	def country(self):
	
		get_geo = requests.get("http://ip-api.com/json/"+self.ipaddr).text
		
		country = loads(get_geo)['country'].encode("utf-8")
		
		if country == '':
			country = None
			
		return country
			
	def city(self):
		
		get_geo = requests.get("http://ip-api.com/json/"+self.ipaddr).text
		
		city = loads(get_geo)['city'].encode("utf-8")
		
		if city == '':
			city = None
			
		return city
		
	def code(self):
	
		get_geo = requests.get("http://ip-api.com/json/"+self.ipaddr).text
		
		countryCode = loads(get_geo)['countryCode'].encode("utf-8")
		
		if countryCode == '':
			countryCode = None
			
		return countryCode
		
	def isp(self):
	
		get_geo = requests.get("http://ip-api.com/json/"+self.ipaddr).text
		
		isp = loads(get_geo)['isp'].encode("utf-8")
		
		if isp == '':
			isp = None
			
		return isp
		
	def org(self):
	
		get_geo = requests.get("http://ip-api.com/json/"+self.ipaddr).text
		
		org = loads(get_geo)['org'].encode("utf-8")
		
		if org == '':
			org = None
			
		return org
		
	def lat(self):
	
		get_geo = requests.get("http://ip-api.com/json/"+self.ipaddr).text
		
		lat = loads(get_geo)['lat']
		
		if lat == '':
			lat = None
			
		return lat
		
	def lon(self):
	
		get_geo = requests.get("http://ip-api.com/json/"+self.ipaddr).text
		
		lon = loads(get_geo)['lon']
		
		if lon == '':
			lon = None
			
		return lon
		
	def query(self):
	
		get_geo = requests.get("http://ip-api.com/json/"+self.ipaddr).text
		
		query = loads(get_geo)['query'].encode("utf-8")
		
		if query == '':
			query = None
			
		return query
		
	def aso(self):
	
		get_geo = requests.get("http://ip-api.com/json/"+self.ipaddr).text
		
		ass = loads(get_geo)['as'].encode("utf-8")
		
		if ass == '':
			ass = None
			
		return ass
		
	def region(self):
	
		get_geo = requests.get("http://ip-api.com/json/"+self.ipaddr).text
		
		region = loads(get_geo)['region'].encode("utf-8")
		
		if region == '':
			region = None
			
		return region
		
	def regionName(self):
	
		get_geo = requests.get("http://ip-api.com/json/"+self.ipaddr).text
		
		regionName = loads(get_geo)['regionName'].encode("utf-8")
		
		if regionName == '':
			regionName = None
			
		return regionName
		
	def timezone(self):
	
		get_geo = requests.get("http://ip-api.com/json/"+self.ipaddr).text
		
		timezone = loads(get_geo)['timezone'].encode("utf-8")
		
		if timezone == '':
			timezone = None
			
		return timezone

print "\n"
		
print color.yellow+"BreadBad: " + color.reset + "An ip geolocation tool by means of a console, written in python and fully functional thanks to the api of: http://ip-api.com/json/\n"

print color.ble+"Created by: " + color.yellow+"DtxdF"+color.reset+"\n"
		
print "Help Main:"
print "#### ####"

print """
	IPAdress \t::\t The command to define the ip to geolocate
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
"""
		
print "\nGeolocation to you:"
print "########### ## ###"
		
geoip(ipaddr=ipadress,localsh=geoipamy).locate()
		
while True:
	
	try:
		
		debug = raw_input(color.yellow + "[" + debug_logo + "]" + color.red + " > " + color.reset)
		
		if not debug:
			continue
			
		if debug.split()[0].lower() == 'ipadress':
			ipadress = debug.split()[1]
			geoip(ipaddr=ipadress).locate()
		
		if ipadress:
			if debug.split()[0].lower() == 'country':
				print color.ble+"\tCountry: %s" % color.green+str(geoip(ipaddr=ipadress).country())+color.reset
			elif debug.split()[0].lower() == 'city':
				print color.ble+"\tCity: %s" % color.green+str(geoip(ipaddr=ipadress).city())+color.reset
			elif debug.split()[0].lower() == 'country_code':
				print color.ble+"\tCountry Code: %s" % color.green+str(geoip(ipaddr=ipadress).code())+color.reset
			elif debug.split()[0].lower() == 'isp':
				print color.ble+"\tISP: %s" % color.green+str(geoip(ipaddr=ipadress).isp())+color.reset
			elif debug.split()[0].lower() == 'org':
				print color.ble+"\tOrganization: %s" % color.green+str(geoip(ipaddr=ipadress).org())+color.reset
			elif debug.split()[0].lower() == 'latitude':
				print color.ble+"\tLatitude: %s" % color.green+str(geoip(ipaddr=ipadress).lat())+color.reset
			elif debug.split()[0].lower() == 'longitude':
				print color.ble+"\tLongitude: %s" % color.green+str(geoip(ipaddr=ipadress).lon())+color.reset
			elif debug.split()[0].lower() == 'query':
				print color.ble+"\tQuery: %s" % color.green+str(geoip(ipaddr=ipadress).query())+color.reset
			elif debug.split()[0].lower() == 'association':
				print color.ble+"\tAssociation: %s" % color.green+str(geoip(ipaddr=ipadress).aso())+color.reset
			elif debug.split()[0].lower() == 'region':
				print color.ble+"\tRegion: %s" % color.green+str(geoip(ipaddr=ipadress).region())+color.reset
			elif debug.split()[0].lower() == 'region_name':
				print color.ble+"\tRegion name: %s" % color.green+str(geoip(ipaddr=ipadress).regionName())+color.reset
			elif debug.split()[0].lower() == 'timezone':
				print color.ble+"\tTime Zone: %s" % color.green+str(geoip(ipaddr=ipadress).timezone())+color.reset
			
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
