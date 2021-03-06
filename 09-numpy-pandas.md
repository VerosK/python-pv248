# Numpy

## Pole

V modulu [`numpy`][numpy] jsou nástroje pro práci s maticemi/poly, které
jsou reprezentovány datovým typ array.


```python
import numpy as np

m1 = np.array([[1,2,3],[3,4,5],[5,6,7]], dtype='float')

print(m1)
print(m1.shape)
m1[0,0]  # Co dělá tohle?
m1[:,0]  # a tohle?
m1[1,:]  # a tohle?
```

## Manipulace s maticemi

```python
10 * m1             # skalární operace
m1 % 2              
                    
selector = (m1 % 2 == 0)
m1[selector]        # co udělá tohle?        
```

Matici je možné změnit velikost `m.reshape()`.

## Nové pole

Nové pole je kromě přímého zadání možné udělat pomocí 
`np.zeros()` a `np.ones()`.

Pole obsahující náhodná čísla s normálním rozložením pak pomocí: 
`np.random.uniform(-1,1, size=(4,4))`


## Lineární rovnice

V modulu [`numpy.linalg`][linalg] jsou nástroje pro práci 
s lineární algebrou.
 
Zkuste pomocí [linalg.solve][linalg] vyřešit systém rovnic.
```
    3x +  2y - z  =  1 
    2x -  2y + 4z = -2 
    -x + y/2 - z  =  0 
```

Řešením by mělo být `+1, -2, -2` 


[numpy]: https://docs.scipy.org/doc/numpy-1.13.0/reference/index.html
[linalg]: https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.linalg.html
