from covid_core import CovidCore,Country

#Prints total covid-19 cases in germany
core = CovidCore()
germany = core.getCountry('de')

print("Growth factor:", germany.getRate())