import requests
import sys
import os

REGISTRY_URL = 'https://rubygems.org/'

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Usage:", sys.argv[0], "<output>")
		sys.exit(1)
	req = requests.get(os.path.join(REGISTRY_URL, 'versions'))
	if req.status_code == 200:
		with open(sys.argv[1], 'wb') as f:
			f.write(req.text.encode('utf-8'))