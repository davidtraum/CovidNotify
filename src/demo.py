from covid_core import CovidCore

#Prints total covid-19 cases in germany
core = CovidCore()
print("Total cases in germany:", core.getCountry('de')['TotalConfirmed'])