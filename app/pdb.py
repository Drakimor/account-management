import traceback
import MySQLdb
import pprint

pprint = pprint.PrettyPrinter()

class pdb():
	def __init__(self):
		self.__conn = MySQLdb.connect(host = 'localhost',
							   user = 'yamarrrU',
							   passwd = 'changeme',
							   db = "yamarrr")

	def __do_query(self, query, single=False, commit = False):
		cursor = self.__conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
		rows = cursor.execute(query)
		if single: records = cursor.fetchone()
		else: records = cursor.fetchall()
		cursor.close()
		if commit == True:
			self.__conn.commit()
		return (rows, records)

	def insert_user(self, first_name, last_name, middle, location, team, pemail, early, nda):
		wemail = "%s@yamarrr.com"% first_name[:1] + last_name
		query = "INSERT INTO new_hiries(team_id, first_name, middle_name, last_name, work_email, personal_email, signed_nda, early_access, location) \
		VALUES (%s,'%s','%s','%s','%s','%s',%s,%s,%s)"% (team, first_name, middle, last_name, wemail, pemail, nda, early, location)
		self.__do_query(query, commit=True)
		return True

	def get_user_que(self):
		query = "SELECT U.id, U.first_name, U.last_name, A.account_name, S.status FROM new_hiries U \
		JOIN hirie_account_statuses S ON (U.id = S.new_hire_id) \
		JOIN accounts A ON (S.account_id = A.id) \
		ORDER BY U.last_name, U.first_name"
		(row, results) = self.__do_query(query)
		return results

	def get_pending_jobs(self):
		query = "SELECT U.id AS user_id, U.first_name, U.last_name, S.id AS job_number, S.account_id AS account_id \
		FROM new_hiries U JOIN hirie_account_statuses S ON (U.id = S.new_hire_id) \
		WHERE S.status = 'Pending' ORDER BY U.last_name, U.first_name"
		(rows, results) = self.__do_query(query)
		return results

	def insert_job_start(self, users):
		accounts = {'Google Apps': 1, 'One Login': 2, 'Yammer': 3}
		for user in users:
			for account in range(1,4):
				query = "INSERT INTO hirie_account_statuses(new_hire_id, account_id, status) VALUES(%s, %d, 'Pending')"% (user, account)
				self.__do_query(query, commit=True)
		return True

	def update_job(self, jid, status):
		query = "UPDATE hirie_account_statuses SET status = '%s' WHERE id = %d"% (status, jid)
		(rows, results) = self.__do_query(query)
		return True

	def get_user_list(self):
		query = "SELECT id, first_name, last_name FROM new_hiries"
		(rows, results) = self.__do_query(query)
		return results

	def schedule_user_jobs(user_ids):
		pass
		#return success

if __name__ == '__main__':
	db = pdb()
	results = db.get_pending_jobs()
	for record in results:
		print pprint.pprint(record)