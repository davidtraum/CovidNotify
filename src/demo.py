from covid_core import CovidCore,Country,CountryList

core = CovidCore()

#Country example
germany = core.getCountry('germany')
brasil = core.getCountry('brazil')

world = core.getWorld()

print("Growth germany", germany.getRFactor())
print("Growth brasil", brasil.getFactor())
print("Growth world", world.getRFactor())

print()

#Country List example

countryList = core.getCountryList()

countryList.sortByRate()
print("Worst country", countryList.worst().getName(), countryList.worst().getRFactor())
print("Best country", countryList.best().getName(), countryList.best().getRFactor())

print()

countryList.sortByValue('TotalDeaths')
print("Most deaths", countryList.worst().getName(), countryList.worst().value('TotalDeaths'))

print()

countryList.sortByValue('TotalConfirmed')
print("Most infections", countryList.worst().getName(), countryList.worst().value('TotalConfirmed'))








