# Knihovna `requests` a `ElementTree`

Python je vhodný nástroj pro práci se službami třetích stran.

## Motivace

[METAR] je formát pro předávání informací o počasí v letectví. 
Na  některých letištích se pravidelně zjištuje stav počasí a 
některé webové služby ho přes API poskytují.  

## Úkol

Zkuste napsat program, který zobrazí poslední zjištěnou teplotu na 
letišti v Brně-Tuřanech. Stav počasí si stáhněte přes HTTP API 
z nějaké veřejné služby. 

Pro stažení použijte modul [requests]  

Odkazy:
- [aviationweather.gov] - veřejně dostupná služba poskytovaná [NOAA] 
- [LKTB] - XML export z letiště v Brně-Tuřanech

```python
import requests

response = requests.get('http://some.uri.dev/')
print(response.content)
```

Pro rozparsování XML použijte např. modul [ElementTree]. 

V XML dodávaném službou aviationweather.gov  je několik měření, zobrazte jen to 
nejčerstvější.  

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