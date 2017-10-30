# generátory

Na přednášce jsme ukázali, jak se v Pythonu používá generátor 
a iterátor.  

Rozšiřující čtení k tématu je např stránka
[Improve Your Python: 'yield' and Generators Explained][yield-explained], která 
ukazuje i použití generátorů pro coroutines.

## Vlastní generátor

Napište si vlastní generátor, který bude postupně vracet přirozená
čísla (stejně jako [itertools.count]).

Zabalte ho do jiného generátoru square, který bude z prvního
generátoru vybírat prvky a vrace jejich

Zkuste vypsat první 50 druhých mocnin generovaných generátorem.


```python

def count(start=1, step=1):
    "Returns numbers starting from start with step step" 
    yield 2
    yield 3
    ...
    
def square(src):
    ...
    
    
# vypíše prvních 50 druhých mocnin    
squares = square(count())
for i in range(100):
    s = next(square)
    print(s)
    
# alternativně (s použití enumerate())
for i,s in enumerate(square(count())):
    if i > 50: 
        break    
    print(s)

```

## Vestavěné generátory/iterátory

Jako generátory se mohou chovat i řetězce a další objekty. Zkuste 
to na řetězci.

Kromě generátoru `range()` je v Pythonu spousta užitečných generátorů
v modulu [`itertools`][itertools].  Je možné několik generátorů složit.

Zkuste v něm najít generátor, který z řetězců `"ABCDEFGH"` a `"12345678"`
vygeneruje kódy všech políček na šachovnici.

# Soubor jako generátor

I soubor se chová jako generátor. Otevřete textový soubor a vypište
z něho všechny řádky, které nejsou prázdné a/nebo nezačínají mřízkou.

Jako bonus pak můžete zkusit použít použít coroutines 
podle [odkazovaného článku][yield-explained]. 

[yield-explained]: https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/
[itertools.count]: https://docs.python.org/2/library/itertools.html#itertools.count
[itertools]: https://docs.python.org/2/library/itertools.html