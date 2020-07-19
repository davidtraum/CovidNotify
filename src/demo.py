from covid_core import CovidCore,Country,CountryList

core = CovidCore()

#Country example
germany = core.getCountry('germany')
brasil = core.getCountry('brazil')

world = core.getWorld()

print("Growth germany", germany.getRate())
print("Growth brasil", brasil.getRate())
print("Growth world", world.getRate())

print()

#Country List example

sortedList = core.getCountryList().sortByRate()

print("Worst country", sortedList.worst().getName(), sortedList.worst().getRate())
print("Best country", sortedList.best().getName(), sortedList.best().getRate())





