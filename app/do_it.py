import google_api
import onelogin_api
import yam_api
import pdb_api
import pprint

pprint = pprint.PrettyPrinter()

db = pdb_api.pdb()

def create_users(verbose = False):
	jobs = db.get_pending_jobs()
	if verbose: pprint.pprint(jobs)

	for job in jobs:
		given_name = job['first_name']
		family_name = job['last_name']
		jid = job['job_number']
		account = job['account_id']
		password = "8675309Bitch"
		user_name = (given_name[:1] + family_name).lower()

		if account == 1:
			if verbose: print "Google for %s"% given_name
			try:
				goog = google_api.google()
				goog.create_user(user_name, family_name, given_name, password)
				goog.add_user_to_group(user_name, 'team')
				goog.add_user_to_group(user_name, 'eng')
				db.update_job(jid, 'Success')
				print "...good"
			except:
				print "...oops"

		if account == 2:
			if verbose: print "Onelogin for %s"% given_name
			onelog = onelogin_api.onelogin()
			onelog.create_user(user_name, family_name, given_name, password)
			user_id = onelog.get_user_id("%s@yamarrr.com"% user_name)
			onelog.add_roles(user_id, [14481])
			db.update_job(jid, 'Success')

		if account == 3:
			if verbose: print "Yammer for %s"% given_name
			yam = yam_api.yam()
			yam.create_user(user_name, family_name, given_name)
			db.update_job(jid, 'Success')

if __name__ == '__main__':
	create_users(verbose = True)