import json

with open('versions.json') as data_file:    
    packages = json.load(data_file)

def version():
	versions = open("versions.csv", "w")
	for package in packages:
		column = package+";"
		for atributes in packages[package]:
			column+= atributes["number"]+";"
			column+= atributes["authors"]+";"
			column+= atributes["built_at"]+";"
			column+= atributes["created_at"]+";"
			column+= str(atributes["downloads_count"])+";"
			column+= str(atributes["licenses"])+";"
			versions.write(str(column))
			versions.write("\n")
			

def main():

	version()

main()