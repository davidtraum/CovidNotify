import requests
import time

class Country:
    def __init__(self, name, data):
        self.data = data
        self.name = name

    def getName(self):
        return self.name

    def getRFactor(self):
        if(self.data['NewRecovered'] == 0):
            return self.data['NewConfirmed']
        return self.data['NewConfirmed'] / self.data['NewRecovered']

    def getInfected(self):
        return self.data['TotalConfirmed'] - self.data['TotalRecovered']

    def getData(self):
        return self.data

    def value(self, key):
        return self.data[key]

    def compare(self, country):
        return country.getRFactor() < self.getRFactor()

class CountryList:

    def __init__(self, data):
        self.list = data.values()
        self.worstFirst = True

    def worst(self):
        if(self.worstFirst):
            return self.list[0]
        else:
            return self.list[-1]

    def best(self):
        if(self.worstFirst):
            return self.list[-1]
        else:
            return self.list[0]

    def sortByRFactor(self):
        sorted = list()
        origin = list(self.list)
        for i in range(len(self.list)): 
            index = 0
            max = origin[0]
            for entry in origin:
                if(entry.getRFactor() > max.getRFactor()):
                    maxIndex = index
                    max = entry
                index += 1
            sorted.append(max)
            origin.remove(max)
        self.worstFirst = True
        self.list = sorted
        return self

    def sortByValue(self, value):
        sorted = list()
        origin = list(self.list)
        for i in range(len(self.list)): 
            index = 0
            max = origin[0]
            for entry in origin:
                if(entry.getData()[value] > max.getData()[value]):
                    maxIndex = index
                    max = entry
                index += 1
            sorted.append(max)
            origin.remove(max)
        self.worstFirst = True
        self.list = sorted
        return self
            
        



class CovidCore:

    def __init__(self, base = 'https://api.covid19api.com/summary', debug=False):
        self.data = dict()
        self.base = base
        self.loaded = False
        self.printDebug = debug
        self.reloadData()

    def debug(self, msg):
        if(self.printDebug):
            print("[CovidCore]", msg)

    def dataIsDifferent(self, d1, d2):
        return d1['Countries']!=d2['Countries']

    def pollMeasurement(self):
        self.dataBefore = self.data.copy()
        self.reloadData()
        if(self.dataIsDifferent(self.dataBefore, self.data)):
            pass

    def reloadData(self):
        self.countries = dict()
        self.world = None
        before = int(time.time() * 1000)
        request = requests.get(url = self.base)
        self.data = request.json()
        self.loaded = 'Countries' in self.data
        after = int(time.time() * 1000) - before
        for country in self.data['Countries']:
            self.countries[country['Country'].lower()] = Country(country['Country'], country)
        self.world = Country('World', self.data['Global'])
        self.debug("Data loaded in " + str(after) + " ms")

    def getCountry(self, name):
        if(name in self.countries):
            return self.countries[name]

    def getCountryList(self):
        return CountryList(self.countries)

    def getWorld(self):
        return self.world


