import pdb
import onelogin_api
import google_api

user_name="test10"
given_name="Ten"
family_name="Test"
password="TestTen!"

print "Creating Google"
goog = google_api.google()
goog.create_user(user_name, family_name, given_name, password)
goog.add_user_to_group(user_name, 'team')

print "Creating Onelogin"
onelog = onelogin_api.onelogin()
print "...user"
onelog.create_user(user_name, family_name, given_name, password)
print "...id"
user_id = onelog.get_user_id("%s@yamarrr.com"% user_name)
print "...roles"
onelog.add_roles(user_id, [14481])

print "Drink!!"