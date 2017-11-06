# DB-API

Vytvořit skript, který bude stahovat letecká data 
o počasí a ukládat teplotu do relační databáze pro další
zpracování.

Připravte druhý skript, který z té databáze přečte poslední teplotu
a vypíše ji.  

Jako relační databázi použijte [sqlite][sqlite3]. 

Pro zjednodušení můžete uložit časovou značku jako UNIX timestamp. 


```python
import sqlite3

class TemperatureStorage:
    def __init__(self, fname='temperatures.db'):
        """Temperature storage"""
        self.db = sqlite3.connect(fname)
        self._setup_tables()
        
    def _setup_tables(self):        
        """Create table when needed"""
        query = """
                CREATE TABLE IF NOT EXISTS notes( 
                    timestamp int primary key, 
                    value float
                );"""
        c = self.db.cursor()
        c.execute(query)
        self.db.commit()

    def put_value(self, timestamp, value):
        "put some measurement inside"
        
    def get_value(self, timestamp):
        "get some measurement inside"
        
    def get_latest_values(self):
        "return latest value"
```

## Vstupní data

[METAR] je formát pro předávání informací o počasí v letectví. 
Na  některých letištích se pravidelně zjištuje stav počasí a 
některé webové služby ho přes API poskytují.  

Stav počasí do databáze můžete stáhnout přes HTTP z veřejného API. 

Pro stažení použijte modul [requests].

Odkazy:
- [aviationweather.gov] - veřejně dostupná služba poskytovaná [NOAA] 
- [LKTB] - XML export z letiště v Brně-Tuřanech

```python
import requests

response = requests.get('http://some.uri.dev/')
print(response.content)
```

## Zpracování XML

Data z [NOAA][aviationweather.gov] jsou v XML formátu, 
vyberte z něho teplotu. 

Pro rozparsování XML použijte např. modul [ElementTree]. 

V XML dodávaném službou aviationweather.gov  je několik měření.

```python
import xml.etree.ElementTree as etree

tree = etree.fromstring(xml_string)
for element in tree.findall('.//data/METAR'):
    temperature = element.find('./temp_c').text
```

## `Unable to import requests` 

Pokud chybí  modul requests, je možné použít  alternativu [urllib.request]. 
Na fakultních strojích by měl nicméně být modul `requests`  přítomný.

```python
from urllib.request import urlopen

url = urlopen('http://ifconfig.co/json')
response_body = url.read() 
```



[METAR]: https://en.wikipedia.org/wiki/METAR
[aviationweather.gov]: https://aviationweather.gov/adds/dataserver
[LKTB]: https://aviationweather.gov/adds/dataserver_current/httpparam?dataSource=metars&requestType=retrieve&format=xml&stationString=LKTB&hoursBeforeNow=2
[NOAA]: http://www.noaa.gov/
[requests]: http://docs.python-requests.org/en/master/
[ElementTree]: https://docs.python.org/3.5/library/xml.etree.elementtree.html
[urllib.request]: https://docs.python.org/3.5/library/urllib.request.html#module-urllib.request
[sqlite3]: https://docs.python.org/3.5/library/sqlite3.html