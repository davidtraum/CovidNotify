import requests

class CovidCore:

    def __init__(self, base = 'https://api.covid19api.com/summary'):
        self.data = dict()
        self.base = base
        self.loaded = False
        self.reloadData()

    def reloadData(self):
        request = requests.get(url = self.base)
        self.data = request.json()
        self.loaded = 'Countries' in self.data

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


