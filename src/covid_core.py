import requests
import time

class CovidCore:

    def __init__(self, base = 'https://api.covid19api.com/summary', debug=False):
        self.data = dict()
        self.base = base
        self.loaded = False
        self.debug = debug
        self.reloadData()

    def debug(self, msg):
        print("[CovidCore]", msg)

    def reloadData(self):
        before = int(time.time() * 1000)
        request = requests.get(url = self.base)
        self.data = request.json()
        self.loaded = 'Countries' in self.data
        if(self.debug):
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
                return country
        return None


