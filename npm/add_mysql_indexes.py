import os
import MySQLdb

DB_HOST = os.environ.get('DB_HOST','localhost')
DB_USER = os.environ.get('DB_USER','root')
DB_PASSWORD = os.environ.get('DB_PASSWORD','root')

def updateIndex(package, version, index):
	con = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD,db='npm_dependencies')
	cursor = con.cursor()
	cursor.execute("UPDATE Packages SET package_index=%s WHERE package='%s' AND version='%s';"%(index, package, version))
	con.commit()
	cursor.close()
	con.close()


if __name__ == '__main__':
	con = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD,db='npm_dependencies')
	cursor = con.cursor()
	index = 0
	cursor.execute("SELECT * FROM Packages;")
	for row in cursor:
		package = row[0]
		version = row[1]
		updateIndex(package, version, index)
		index += 1
	cursor.close()
	con.close()