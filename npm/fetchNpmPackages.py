import requests
import os

REGISTRY_URL = 'https://registry.npmjs.org'

def fetchPackageList(dest):
    """
    Fetch cran package list, store the result in dest
    """
    req = requests.get(os.path.join(REGISTRY_URL, '-/all'))
    if req.status_code == 200:
        with open(dest, 'wb') as f:
            f.write(req.text.encode('utf-8'))

if __name__ == '__main__':
	fetchPackageList("data/nodejspackages.json")
