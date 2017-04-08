import json
import os
import requests
# from pymongo import MongoClient
import MySQLdb

REGISTRY_URL = 'https://registry.npmjs.org'
DB_HOST = os.environ.get('DB_HOST','localhost')
DB_USER = os.environ.get('DB_USER','root')
DB_PASSWORD = os.environ.get('DB_PASSWORD','root')

def fetch_dependencies(package):
	try:
		# client = MongoClient()
		# db = client.npm_dependencies
		# collection = db.dependencies
		con = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD, db='npm_dependencies')
		c = con.cursor()
		req = requests.get(os.path.join(REGISTRY_URL, package))
		if req.status_code != 200:
			return
		metadata = json.loads(req.text)
		for version in metadata["versions"]:
			print("package:", package)
			print("version:", version)
			# registry = {}
			# registry["package"] = package
			# registry["version"] = version
			license = "NULL"
			try:
				print("license:", metadata["versions"][version]["license"])
				# registry["license"] = metadata["versions"][version]["license"]
				license = metadata["versions"][version]["license"]
			except Exception as e:
				print(e)
			c.execute("INSERT INTO Packages VALUES ('%s', '%s', '%s');"%(package, version, license))
			con.commit()
			try:
				print("dependencies:", metadata["versions"][version]["dependencies"])
				# registry["dependencies"] = metadata["versions"][version]["dependencies"]
				for dependency in metadata["versions"][version]["dependencies"]:
					c.execute("INSERT INTO Dependencies VALUES ('%s', '%s', '%s', '%s');"%(package, version, dependency, metadata["versions"][version]["dependencies"][dependency]))
					con.commit()
			except Exception as e:
				print(e)
			# collection.insert_one(registry)
			print()
	except Exception as e:
		print(e)
		return

if __name__ == '__main__':
	print("Reading JSON...")
	with open("nodejspackages_05.04.2017.4h.json") as file:
		packages = json.load(file)
		limit = 0
		for package in packages:
			print("Fetching", package, "dependencies...")
			fetch_dependencies(package)
			limit += 1
			if limit == 0:
				break;