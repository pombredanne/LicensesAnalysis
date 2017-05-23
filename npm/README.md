# NPM

1. `python fetchNpmPackages.py`
    1. Produces `nodejspackages.json`
    
2. `python creteIndex.py`
    1. Consumes `nodejspackages.json`
    2. Produces `index`
    
3. `python npmJsonCrawler.py`
    1. Consumes `index`
    2. Produces `visitedPackages`
    3. Produces `dependencyList.json`

4. `python getLicenses.py`
    1. Consumes `dependencyList.json`
    2. Produces `licenses.json`

5. Manually
    1. Normalize licenses
        1. Consumes `licenses.json`
        2. Produces `normalizedLicenses.json`
    2. Create strong copyleft index
        1. Consumes `licenses.json`
        2. Produces `permissivityIndex.json`
    
6. `python normalizeDependencyList.py`
    1. Consumes `dependencyList.json`
    2. Consumes `licenses.json`
    3. Consumes `normalizedLicenses.json`
    4. Produces `normalizedDependencyList.json`

7. Analyze
    1. `python getDistribution.py`
        1. Consumes `normalizedDependencyList.json`
        2. Produces `normalizedDistribution.json`
    2. `python3.5 getIrregularEdges.py`
        1. Consumes `normalizedDependencyList.json`
        2. Consumes `permissivityIndex.json`
        3. Produces `classifiedDependencyList.json`
