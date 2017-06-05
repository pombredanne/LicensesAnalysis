#encoding: utf-8
import json
import os
import requests

DEPENDENCY_LIST = None

PACKAGES = {}

def get_dependencies():
    file_versions = open('data/versions.csv', 'r')

    DEPENDENCY_LIST = open("data/dependencyList.json", "w")
    DEPENDENCY_LIST.write("{")

    index = 0
    for package in file_versions:
        package_versions = package.split(',')
        nome_package = package_versions[0]

        del package_versions[-1]
        del package_versions[0]

        for version in package_versions: #passa por todas as versoes do pacote
            req = requests.get(os.path.join("https://rubygems.org/api/v2/rubygems/"+nome_package+"/versions/", version))
            if req.status_code != 200:
                raise Exception
            metadata = json.loads(req.text)
            registry = {}
            registry["package"] = nome_package
            registry["version"] = version
            try:
                registry["license"] = metadata["licenses"]
            except Exception as e:
                registry["license"] = None
            dependencies = metadata["dependencies"]
            registry["dependencies"] = dependencies["runtime"]
            registry["index"] = index
            if index > 0:
                    DEPENDENCY_LIST.write(",")
                    DEPENDENCY_LIST.write("\n")
            DEPENDENCY_LIST.write("\""+registry["package"]+"@"+registry["version"]+"\":")
            DEPENDENCY_LIST.write(json.dumps(registry))
            index += 1
    DEPENDENCY_LIST.write("}")
    DEPENDENCY_LIST.close()
    file_versions.close()



if __name__ == '__main__':
    try:
        get_dependencies()
    except Exception as e:
        print(e)