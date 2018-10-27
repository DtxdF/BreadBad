# -*- coding: UTF-8 -*-

import urllib
from json import loads

def function_notdefined():
	raise ValueError("Error, the values is not defined.")
	
class statusip(Exception): pass

class geolocation:
	def __init__(self, ip):
		self.ip = ip
		self.init = False
	def start(self):
		if not self.ip == 'localme':
			self.api_data = loads(urllib.urlopen("http://ip-api.com/json/"+self.ip).read())
		else:
			self.api_data = loads(urllib.urlopen("http://ip-api.com/json").read())
		if self.api_data['status'] == 'fail':
			raise statusip("Error, This IP Addr is invalid.")
		self.init = True
	def read(self):
		if not self.init:
			function_notdefined()
		return self.api_data
	def query(self):
		if not self.init:
			function_notdefined()
		return self.api_data['query']
	def association(self):
		if not self.init:
			function_notdefined()
		return self.api_data['as'].encode("UTF-8")
	def city(self):
		if not self.init:
			function_notdefined()
		return self.api_data['city'].encode("UTF-8")
	def country(self):
		if not self.init:
			function_notdefined()
		return self.api_data['country'].encode("UTF-8")
	def countryCode(self):
		if not self.init:
			function_notdefined()
		return self.api_data['countryCode'].encode("UTF-8")
	def isp(self):
		if not self.init:
			function_notdefined()
		return self.api_data['isp'].encode("UTF-8")
	def latitude(self):
		if not self.init:
			function_notdefined()
		return self.api_data['lat']
	def longitude(self):
		if not self.init:
			function_notdefined()
		return self.api_data['lon']
	def organization(self):
		if not self.init:
			function_notdefined()
		return self.api_data['org'].encode("UTF-8")
	def region(self):
		if not self.init:
			function_notdefined()
		return self.api_data['region'].encode("UTF-8")
	def regionName(self):
		if not self.init:
			function_notdefined()
		return self.api_data['regionName'].encode("UTF-8")
	def timezone(self):
		if not self.init:
			function_notdefined()
		return self.api_data['timezone'].encode("UTF-8")
	def zipCode(self):
		if not self.init:
			function_notdefined()
		return self.api_data['zip'].encode("UTF-8")
	def google_maps(self):
		if not self.init:
			function_notdefined()
		return 'https://www.google.com/maps/place/'+str(self.api_data['lat'])+','+str(self.api_data['lon'])+'/@'+str(self.api_data['lat'])+','+str(self.api_data['lon'])+',16z'.encode("UTF-8")