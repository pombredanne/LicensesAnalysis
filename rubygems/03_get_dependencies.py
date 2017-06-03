import json


with open('versions.json') as data_file:    
    packages = json.load(data_file)

def parseData():
    index = 0
    for package in packages:
        registry = {}
        registry["package"] = package
        for atributes in packages[package]:
            registry["version"] = atributes["number"]
            registry["license"] = atributes["licenses"]
            nameObject = package+"@"+atributes["number"]+":{'index:'"
            print (nameObject)
            index += 1


def main():
    parseData()

main()