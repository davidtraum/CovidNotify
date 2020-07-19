### Simple Python API for corona data using covid19api.com

# Example: Getting country data

    from covid_core import *

    core = CovidCore()
    country = core.getCountry('germany')

    print( country.getRFactor() )
    print( country.value('TotalRecovered') )
    print( country.value('TotalConfirmed') )

# Example: Sorting

    from covid_core import * 

    core = CovidCore()
    countryList = core.getCountryList()
    
    countryList.sortByValue('TotalConfirmed')
    print("Most confirmed cases:", countryList.worst().getName())

    countryList.sortByRFactor()
    print("Lowest R-Factor:", countryList.best().getName())

# Example: Worldwide

    from covid_core import *
    
    core = CovidCore()
    world = core.getWorld()
    brazil = core.getCountry('brazil')

    print("Portion of worldwide cases in brazil:", int( ( brazil.value('TotalConfirmed') / world.value('TotalConfirmed) ) * 100 ), "%")

