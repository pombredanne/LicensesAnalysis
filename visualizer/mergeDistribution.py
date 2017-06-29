import json
import sys

ECOSSYSTEMS = {}
MERGED_ECOSSYSTEMS = {}

def appendEcossystem(ecossystem, filename):
	with open(filename) as distributionFile:
		distribution = json.load(distributionFile)
		ECOSSYSTEMS[ecossystem] = distribution

def appendLicenses(ecossystem):
	for license in ECOSSYSTEMS[ecossystem]:
		try:
			MERGED_ECOSSYSTEMS[license]
		except Exception as e:
			MERGED_ECOSSYSTEMS[license] = {}
		finally:
			MERGED_ECOSSYSTEMS[license][ecossystem] = ECOSSYSTEMS[ecossystem][license]

def mergeEcossystems():
	for ecossystem in ECOSSYSTEMS:
		appendLicenses(ecossystem)

def sumEcossystems():
	for license in MERGED_ECOSSYSTEMS:
		sumEcossystems = 0
		for ecossystem in MERGED_ECOSSYSTEMS[license]:
			sumEcossystems += MERGED_ECOSSYSTEMS[license][ecossystem]
		MERGED_ECOSSYSTEMS[license]["total"] = sumEcossystems

def toCSV():
	for license in MERGED_ECOSSYSTEMS:
		print(license.replace(",", ""), end=",")
		try:
			print(MERGED_ECOSSYSTEMS[license]["rubygems"], end=",")
		except Exception as e:
			print(0, end=",")
		try:
			print(MERGED_ECOSSYSTEMS[license]["cran"], end=",")
		except Exception as e:
			print(0, end=",")
		try:
			print(MERGED_ECOSSYSTEMS[license]["npm"], end=",")
		except Exception as e:
			print(0, end=",")
		print(MERGED_ECOSSYSTEMS[license]["total"])

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Usage:", sys.argv[0], "<output>")
		sys.exit(1)
	filenames = {
	"rubygems": "../rubygems/data/percentualDistribution.json",
	"cran": "../cran/data/normalizedDistribution.json",
	"npm": "../npm/data/normalizedDistribution.json"
	}
	for filename in filenames:
		appendEcossystem(filename, filenames[filename])
	mergeEcossystems()
	sumEcossystems()
	toCSV()
	with open(sys.argv[1], "w") as mergedDistribution:
		mergedDistribution.write(json.dumps(MERGED_ECOSSYSTEMS))