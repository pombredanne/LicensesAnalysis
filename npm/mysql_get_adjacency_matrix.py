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

def getIndex(package, version):
	con = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD,db='npm_dependencies')
	cursor = con.cursor()
	cursor.execute("SELECT package_index FROM Packages WHERE package='%s' AND version='%s';"%(package, version))
	index = cursor.fetchone()
	cursor.close()
	con.close()
	return index

if __name__ == '__main__':
	with open("adjacencies.csv", "w") as adjacencies:
		con = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD,db='npm_dependencies')
		cursor = con.cursor()
		cursor.execute("SELECT * FROM Packages limit 10000;")
		for row in cursor:
			package = row[0]
			version = row[1]
			dependencyIndexes = []
			dependenciesRows = getDependencies(package, version)
			if dependenciesRows:
				for dependencyRow in dependenciesRows:
					dependency = dependencyRow[0]
					dependencyVersion = dependencyRow[1]
					index = getIndex(dependency, version)
					if index:
						dependencyIndexes.append(index[0])
			dependencyIndexes.sort()
			i = 0
			j = 0
			while i < cursor.rowcount:
				if j < len(dependencyIndexes) and i == dependencyIndexes[j]:
					adjacencies.write("1")
					j += 1
				else:
					adjacencies.write("0")
				i += 1
				if i != cursor.rowcount:
					adjacencies.write(",")
			adjacencies.write("\n")