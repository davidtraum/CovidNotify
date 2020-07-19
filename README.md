### Simple Python API for corona data using covid19api.com
##Example

    from covid_core import *

    core = CovidCore()
    brazil = core.getCountry('brazil')
    print( brazi.getRFactor() )

    countryList = core.getCountryList().sortByRFactor()
    print("Lowest R-Factor", countryList.best())
