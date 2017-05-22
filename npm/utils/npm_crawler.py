import json
import os
import requests
import MySQLdb

REGISTRY_URL = 'https://registry.npmjs.org'
DB_HOST = os.environ.get('DB_HOST','localhost')
DB_USER = os.environ.get('DB_USER','root')
DB_PASSWORD = os.environ.get('DB_PASSWORD','root')

def fetch_dependencies(package):
        con = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD,db='npm_dependencies')
        c = con.cursor()
        try:
                req = requests.get(os.path.join(REGISTRY_URL, package))
                if req.status_code != 200:
                        raise Exception
                metadata = json.loads(req.text)
                for version in metadata["versions"]:
                        license = "NULL"
                        try:
                                license = metadata["versions"][version]["license"]
                        except Exception as e:
                                print(e)
                        c.execute("INSERT INTO Packages VALUES ('%s', '%s', '%s');"%(package, version, license))
                        con.commit()
                        try:
                                for dependency in metadata["versions"][version]["dependencies"]:
                                        c.execute("INSERT INTO Dependencies VALUES ('%s', '%s', '%s', '%s');"%(package, version, dependency, metadata["versions"][version]["dependencies"][dependency]))
                                        con.commit()
                        except Exception as e:
                                print(e)
        except Exception as e:
                print(e)
        finally:
                c.close()
                con.close()

if __name__ == '__main__':
        visitedPackages = open("visitedPackages", "a")
        with open("index") as packages:
                for package in packages:
                        package = package[:-1]
                        fetch_dependencies(package)
                        visitedPackages.write(package)
                        visitedPackages.write("\n")
                visitedPackages.close()