from lxml import etree
import base64
import urllib2
import urllib
from pprint import PrettyPrinter
pprint = PrettyPrinter()
import xml.dom.minidom
from django.utils import simplejson as sjson
from json import JSONDecoder
from lxml.cssselect import CSSSelector

class onelogin():

  def __init__(self):
    self.auth_string = "Basic %s"% base64.b64encode("3357b42dfebcd175f8508f677793dc20c3feab3b:x")
    self.jsond = JSONDecoder()

  def __api_put(self, url, params):
    if params:
      req = urllib2.Request(url, data = params)
    else:
      req = urllib2.Request(url)
    req.add_header("Authorization", self.auth_string)
    req.add_header("Content-type", "application/xml")
    req.get_method = lambda: 'PUT'
    conn = urllib2.urlopen(req)
    return conn.read()
 
  def __api_post(self, url, params):
    if params:
      req = urllib2.Request(url, data = params)
    else:
      req = urllib2.Request(url)
    req.add_header("Authorization", self.auth_string)
    req.add_header("Content-type", "application/xml")
    req.get_method = lambda: 'POST'
    conn = urllib2.urlopen(req)
    return conn.read()

  def __api_get(self, url, params = False):
    if params:
      encodedParams = urllib.urlencode(params)
      req = urllib2.Request("%s?%s"% (url, encodedParams))
    else:
      req = urllib2.Request(url)
    req.add_header("Authorization", self.auth_string)
    req.get_method = lambda: 'GET'
    conn = urllib2.urlopen(req)
    return conn.read()

  def create_user(self, user_name, family_name, given_name, password):
    url = "https://app.onelogin.com/api/v1/users.xml"
    user_xml = "<user>"
    user_xml += "<email>%s@yamarrr.com</email>"% user_name
    user_xml += "<firstname>%s</firstname>"% given_name
    user_xml += "<lastname>%s</lastname>"% family_name
    user_xml += "</user>"
    print self.__api_post(url, user_xml)

  def get_user_id(self, email):
    url = "https://app.onelogin.com/api/v1/users.xml"
    user_list = self.__api_get(url)
    tree = etree.fromstring(user_list)
    emails = map(lambda x: x.text, tree.xpath("//users/user/email"))
    ids = map(lambda x: x.text, tree.xpath("//users/user/id"))
    for i in range(len(emails)):
        if emails[i] == email:
          return ids[i]
    else:
      return False

  def add_roles(self, user_id, roles):
    url = "https://app.onelogin.com/api/v1/users/%s.xml"% user_id
    role_xml = "<user>"
    role_xml += "<roles type='array'>"
    for role in roles:
      role_xml += "<role>%s</role>"% role
    role_xml += "</roles>"
    role_xml += "</user>"
    self.__api_put(url, role_xml)

if __name__ == "__main__":
  user_name="test3"
  given_name="Three"
  family_name="Test"
  password="TestThree!"

  onelog = onelogin_api()
  create_user('test3', 'Test', 'Three', 'ThreeTest!')
  id = onelog.get_user_id("test2@yamarrr.com")
  onelog.add_roles(id, ["Engineering"])
