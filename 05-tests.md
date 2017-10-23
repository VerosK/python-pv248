# unittest a pytest

Na přednášce jsme ukázali, jaké nástroje jsou v Pythonu 
k dispozici pro testy.

Zkuste napsat objekt `Graph`, který bude reprezentovat 
orientovaný graf. Zkuste k němu připravit i testy.

Šablona modulu `graph.py` a základní testy jsou
v adresáři [05-tests][tests_stub].


## py.test

Je možné, že budete muset nainstalovat `py.test` pomocí
`pip install pytest`. Instalovat je samozřejmě vhodné do 
virtuálního prostředí.

Nejčastější parametry pro py.test
```commandline
py.test                         # spustí test
py.test -x                      # skončit při první chybě
py.test test_graph.py           # použít testcases z jednoho souboru 
```

[tests_stub]: https://github.com/VerosK/python-pv248/tree/master/05-tests