# Dekorátory

## Vlastní dekorátor 

Napište dekorátor, který zachytí volání funkce a uchová parametry 
volání funkce.

Pro počítání můžete s výhodou použít [`Counter`][Counter] z 
modulu [`collections`][collections]

----- 

Mějme naivní rekurzivní funkci na výpočet čísla z Fibonacciho posloupnosti

```python
def fib(n):
    "Return n-th Fibonacci number"
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)
```

Přidejte k funkci vlastní dekorátor a zjistěte, s jakými parametry
byla nejčastěji volána.

```python

class CallInspector:
    def __init__(self):
        pass
        
    def inspect(self, func):
        "this is decorator"
        pass
        
    def show_call_stats(self):
        "show some call statistics"
        print("Function was called {} times")
        print("Most frequently called parameter combinations was: ")
        

inspector = CallInspector()

@inspector.inspect
def fib(n):
    pass  # the original function should be here
    
# invoke function and show call statistics
fib(256)
inspector.show_call_stats()
```


## Dekorátor `cache`

Pomocí modulu [`timeit`][timeit] změřte, jak dlouho vykonávání `fib(256)`
trvá. Zkuste použít dekorátor [`@cache`][cache], a změřte, jestli se 
použitím cache výpočet zrychlí.

## Inspection

V REPL se podívejte, co si o funkci `fib()` myslí nápověda před dekorováním 
a po dekorování.

```pythonstub
>>> help(fib)
```

[Counter]: https://docs.python.org/3.5/library/collections.html#collections.Counter
[collections]: https://docs.python.org/3.5/library/collections.html
[timeit]: https://docs.python.org/3.5/library/timeit.html
[cache]: https://docs.python.org/3.5/library/functools.html#functools.lru_cache