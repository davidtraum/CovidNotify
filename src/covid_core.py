import requests
import time

class Country:
    def __init__(self, data):
        self.data = data

    def getRate(self):
        return self.data['NewConfirmed'] / self.data['NewRecovered']

    def getInfected(self):
        return self.data['TotalConfirmed'] - self.data['TotalRecovered']

    def getData(self):
        return self.data

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
        before = int(time.time() * 1000)
        request = requests.get(url = self.base)
        self.data = request.json()
        self.loaded = 'Countries' in self.data
        after = int(time.time() * 1000) - before
        self.debug("Data loaded in " + str(after) + " ms")

    def getCountry(self, name):
        if(not self.loaded):
            return None
        searchCode = len(name) == 2
        if(searchCode):
            name = name.lower()
        for country in self.data['Countries']:
            if(searchCode and country['CountryCode'].lower() == name or not searchCode and country['Country'] == name):
                return Country(country)
        return None


