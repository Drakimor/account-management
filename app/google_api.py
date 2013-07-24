import gdata.apps.client
import gdata.apps.groups.client

email = 'yadmin@yamarrr.com'
passwd = 'h@ckd@y!'
domain = 'yamarrr.com'

class google():

	def add_user_to_group(self, member_id, group_id):
		groupClient = gdata.apps.groups.client.GroupsProvisioningClient(domain=domain)
		groupClient.ClientLogin(email=email, password=passwd, source='apps')
		groupClient.AddMemberToGroup(group_id, member_id)

	def create_user(self, user_name, family_name, given_name, password):
		appClient = gdata.apps.client.AppsClient(domain=domain)
		appClient.ssl = True
		appClient.ClientLogin(email=email, password=passwd, source='apps')
		appClient.CreateUser(user_name, family_name, given_name, password, suspended=False, admin=None, quota_limit=None, password_hash_function=None, change_password=None)

if __name__ == "__main__":
	print "Creating User!"
	create_user('test2', 'Two', 'Test', 'TwoTest!')
	print "Adding to group"
	add_user_to_group('test2', 'team')