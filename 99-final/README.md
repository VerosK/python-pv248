
# Bludiště

**Vytvořte malou  aplikaci (např. ve frameworku Flask), která 
bude umět hledat nejkratší cesty v bludišti.**

TL;DR: Bludiště je acyklický neorientovaný graf. 

Bludiště se skládá z pojmenovaných místností, mezi místnostmi jsou v 
chodby. Chodbami je možné procházet oběma směry. 
 
Bludiště má právě jeden začátek a jeden konec, oba se nachází v nějakých 
místnostech.

## Aplikace

Aplikace má po spuštění poslouchat na portu 5000/TCP, kde má odpovídat na 
HTTP požadavky.

* Na požadavek `GET /` má aplikace odpovědět odpovědí `200 OK`. 
Obsah stránky není definovaný, může tam být např.testovací formulář
nebo může být stránka prázdná.

* Na požadavek `POST /` má aplikace zpracovat poslaná JSON data a vrátit stavový 
kód `200 OK`, v těle odpovědi pak bude JSON výstup. Pokud data nejsou validní, má aplikace 
přesto vrátit `200 OK` a v těle odpovědi vrátit chybový stav.

* Na jiné požadavky `GET` a `POST` má aplikace vrátit `404 Not found`.

* Na metodu `HEAD` není chování definováno.

* Na jiné HTTP metody má API vrátit `405 Method Not Allowed`

## Vstup API

Aplikace na vstupu jako tělo požadavku očekává JSON objekt - 
slovník, který obsahuje klíče `start`, `end`, `rooms` a `corridors`.

Např.

```json
{
"start": "A",
"end": "E",
"rooms": ["A","B","C","D","E"],
"corridors": [ ["A","B"], ["B","E"], ["B","C"], ["C","E"] ]
}
```

  * Pod klíčem `rooms` je uložen seznam jmen místností. Jména místností jsou
  řetězce nebo čísla.
  
  * Pod klíčem `corridors` je seznam chodeb. Chodby jsou reprezentovány jako
  dvojice
  
  * Klíče `start` a `end` obsahují jména
  
## Výstup API

Pokud řešení existuje, aplikace vrátí slovník ve fomátu JSON , který obsahuje
v klíči `solution` jednu z nejkratších cest jako popis uzlů, kterými se 
musí projít. V klíči `status` může poslat zprávu, že se povedlo najít.  

```json
{"solution": [ "A", "B", "E"],
 "length": 3,
 "status": "OK"
 }
```

Pokud řešení neexistuje, vrátí aplikace v klíčích `solution` a `length`
hodnotu `None` a v klíči `status` pošle zprávu `No solution found`. 
HTTP odpověď bude přesto 200 OK.

```json
{"solution": null,
 "length": null,
 "status": "No solution found" 
}
```

Pokud je zadání nesmyslné (např. chceme postavit chodbu mezi 
neexistujícími místnostmi), vrátí aplikace v klíčích `solution` a `length` hodnotu `None` a 
v klíči `error` pošle zprávu *'Invalid input'*, případně detailnější 
výstup. HTTP odpověď bude přesto 200 OK.

```json
{"solution": null,
 "length": null,
 "error": "Invalid input" 
}
```

<!---

## Ukázkové řešení

Ukázkové řešené běží třeba na https://pv248.toaster.cz (HTTPS na 443), 
Vaše aplikace by ale měla poslouchat na http://localhost:5000/

-->

## Odevzdání

Do odevzdávárny na ISu nahrajte archiv (ZIP, tar.gz) zdrojových kódů 
aplikace. 

Pro řešení můžete použít libovovolné moduly (třeba pro BFS či 
Dijstrův algoritmus).  Pokud potřebujete nějaké speciální
moduly, nezpomeňte je přidat do `requirements.txt`.

Aplikaci budeme testovat ve virtuálním prostředí s Pythonem 3, před 
spuštěním se provede 

```bash
pip install -r requirements.txt
```   

Pro testy aplikace můžete použít přiložené testy - ty čekají, že 
aplikace poslouchá na portu 5000. 