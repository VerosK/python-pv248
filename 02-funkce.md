# Funkce a datové typy

Na přednášce jsme si ukázali, jak v Pythonu vypadají datové objekty, 
jak vypadají funkce a jak můžeme použít výchozí (default) parametry.

## Úkol
             
Zkuste přepsat modulna domeček z minulého cvičení tak, 
aby se domeček kreslil ve funkci, přičemž seznam tahů želvy
bude v seznamu (`list`) 


```python
HOUSE = [
    (0, 100), (90, 100), (90+45, 141),
    (45, -100), (90, 100), (90+45, 141/2),
    (90, 141/2), (90, 141)
]
```

Hlavička funkce pak bude vypadat nějak takle

```python
def draw_house(color='black', size=1., moves=HOUSE):
    """
    :param color:   barva domečku 
    :param size:    zvětšení domečku oproti základní velikosti
    :param moves    
    """
    
    pass
    
```


Vyzkoušejte, si, jak fungují defaultní a pojmenované parametry.

```python
draw_house(color='red')
draw_house(size=2)                    # large house
draw_house(size=0.5, color='green')   # small one
```