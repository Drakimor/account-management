import urllib, urllib2
import urlparse

from json import JSONDecoder
from pprint import PrettyPrinter
from urllib2 import HTTPError

jsond = JSONDecoder()

class yam():
	def __init__(self):
		self.key="80GMZIMi2L7UhV3pvm1v5g"

	def __api_put(self, url, params, key=False, decode=True):
		if params:
			encodedParams = urllib.urlencode(params)
			req = urllib2.Request(url, data = encodedParams)
		else:
			req = urllib2.Request(url)
		if key:
			key_headers = req.add_header('Authorization', "Bearer %s"% key)
		conn = urllib2.urlopen(req)
		if decode:
			return jsond.decode(conn.read())
		else:
			return conn.read()
	
	def __api_post(self, url, params, decode=True):
		if params:
			encodedParams = urllib.urlencode(params)
			req = urllib2.Request(url, data = encodedParams)
		else:
			req = urllib2.Request(url)
		key_headers = req.add_header('Authorization', "Bearer %s"% self.key)
		req.get_method = lambda: 'POST'
		try:
			conn = urllib2.urlopen(req)
		except HTTPError, e:
				print e.code
				print e.read()
				print HTTPError.read()
		if decode:
				return jsond.decode(conn.read())
		else:
			return conn.read()

	def __api_get(self, url, params = False, decode=True, key=False):
		if params:
			encodedParams = urllib.urlencode(params)
			req = urllib2.Request(url, data = encodedParams)
		else:
			req = urllib2.Request(url)
		if key:
			key_headers = req.add_header('Authorization', "Bearer %s"% key)
		conn = urllib2.urlopen(req)
		if decode:
			return jsond.decode(conn.read())
		else:
			return conn.read()

	def create_user(self, user_name, family_name, given_name):
		url = "https://www.yammer.com/api/v1/users.json"
		params = {
		'full_name': "%s %s"% (given_name, family_name),
		'email': "%s@yamarrr.com"% user_name
		}
		user = self.__api_post(url, params, decode=False)
		print user

	def get_auth_key_for_user(self):
		url = "https://www.yammer.com/oauth2/access_token.json"
		params = {
			'client_id': "vTrlVfp0DV7ReHyZYxtQ",
			'client_secret': "0kBFejmH9mPIWuXSWZcppEHY9Hfg5NpZtuwnZYu94",
			'username': 'yadmin@yamarrr.com',
			'password': 'Y8mm3R!*'
		}
			
		content = self.__api_get(url, params = params)['access_token']['token']
		print content

if __name__ == '__main__':
	yam = yam()
	yam.create_user("test14", "Test", "Ten")