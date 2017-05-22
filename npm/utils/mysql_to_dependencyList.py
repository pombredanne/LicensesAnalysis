import json
import os
import MySQLdb

DB_HOST = os.environ.get('DB_HOST','localhost')
DB_USER = os.environ.get('DB_USER','root')
DB_PASSWORD = os.environ.get('DB_PASSWORD','root')

def getDependencies(package, version):
	con = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD,db='npm_dependencies')
	cursor = con.cursor()
	cursor.execute("SELECT package_depends_to_package, package_dependency_version FROM Dependencies WHERE package_package = '%s' AND package_version = '%s';"%(package, version))
	dependencies = cursor
	cursor.close()
	con.close()
	return dependencies

if __name__ == '__main__':
	with open("dependencyList.json", "w") as dependencies:
		dependencies.write("{")
		con = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD,db='npm_dependencies')
		cursor = con.cursor()
		index = 0
		cursor.execute("SELECT * FROM Packages;")
		for row in cursor:
			package = row[0]
			version = row[1]
			license = row[2]
			dependenciesArray = []
			dependenciesRows = getDependencies(package, version)
			if dependenciesRows:
				for dependencyRow in dependenciesRows:
					dependency = dependencyRow[0]
					dependencyVersion = dependencyRow[1]
					dependenciesArray.append(dependency+"@"+dependencyVersion)
			if index != 0:
				dependencies.write(",")
				dependencies.write("\n")
			dependencies.write("\""+package+"@"+version+"\":")
			dependencies.write("{")
			dependencies.write("\"index\":"+str(index)+",")
			dependencies.write("\"package\":\""+package+"\",")
			dependencies.write("\"version\":\""+version+"\",")
			dependencies.write("\"license\":\""+license+"\",")
			dependencies.write("\"dependencies\":"+json.dumps(dependenciesArray))
			dependencies.write("}")
			index += 1
		cursor.close()
		con.close()
		dependencies.write("}")