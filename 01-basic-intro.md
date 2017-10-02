# Úvod

Na přednášce jsme si ukázali, jak se v Pythonu
používají proměnné, jak použít [REPL] a jak použít modul [turtle].

## Úkoly

1. Napište v Pythonu klasický [Hello world], pojmenujte ho `hello.py`.    
   
   V Pythonu se pro vypsání objektu používá funkce `print()`
   
   Zkuste program napsat tak, ať ho můžete spustit z příkazové
   řádky, na Linuxu tedy:
   
       ./hello.py 
       
   Použijte Python 3.  ([shebang] `#!/usr/bin/env python3` )

              

2. Zkuste použít modul `turtle` a nakreslit nějaké obrázky - třeba
   domeček jedním tahem.      
     
   **nápověda:**
        
       import turtle             # importuje (připojí) modul pro želví grafiku
       turtle.shape('turtle')    # změní tvar želvy
       turtle.forward(42)        # posune želvu dopředu
       turtle.left(90)           # otočí želvu o π/2
       turtle.right(90)
       turtle.color('blue')      # kreslit modře
       turtle.color('#FF8080')   # kreslit růžovou   
       turtle.exitonclick()      # čeká na klik myši  



3. Použijte cyklus a fuknci pro opakování. Nakreslete třeba plot, 
   květinu nebo více domečků. 

   **nápověda:**
   
       def house():              # takhle vypadá definice funkce
            pass                
            
       house()                   # a takhle se volá
          
       for i in range(10):       # takhle vypadá cyklus   
            print(i, " bottles hanging on the wall")
   
   Pro generování náhodných čísel můžete z modulu [random] použít
   funkci [randint], např. `random.randint(10,100)`         


[turtle]: https://docs.python.org/3.5/library/frameworks.html
[REPL]: https://docs.python.org/3.5/tutorial/interpreter.html
[Hello world]: https://en.wikipedia.org/wiki/%22Hello,_World!%22_program
[shebang]: https://en.wikipedia.org/wiki/Shebang_(Unix)
[random]: https://docs.python.org/3.5/library/random.html
[randint]: https://docs.python.org/3.5/library/random.html#random.randint