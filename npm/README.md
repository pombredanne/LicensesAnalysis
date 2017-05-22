# NPM

1. `python fetchNpmPackages.py`
1.1 Produces `nodejspackages.json`

2. `python creteIndex.py`
2.1 Consumes `nodejspackages.json`
2.2 Produces `index`

3. `python npmJsonCrawler.py`
3.1 Consumes `index`
3.2 Produces `visitedPackages`
3.3 Produces `dependencyList.json`

4. `python getLicenses.py`
4.1 Consumes `dependencyList.json`
4.2 Produces `licenses.json`

5. Manually normalize licenses
5.1 Consumes `licenses.json`
5.2 Produces `normalizedLicenses.json`
5. Manually create strong copyleft index
5.1 Consumes `licenses.json`
5.2 Produces `permissivityIndex.json`

6. `python normalizeDependencyList.py`
6.1 Consumes `dependencyList.json`
6.2 Consumes `licenses.json`
6.3 Consumes `normalizedLicenses.json`
6.4 Produces `normalizedDependencyList.json`

7. `python getDistribution.py`
7.1 Consumes `normalizedDependencyList.json`
7.2 Produces `normalizedDistribution.json`
7. `python getIrregularEdges.py`
7.1 Consumes `normalizedDependencyList.json`
7.2 Consumes `permissivityIndex.json`
7.3 Produces `classifiedDependencyList.json`