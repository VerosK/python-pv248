# Numpy

## Matice

V modulu [`numpy`][numpy] jsou nástroje pro práci s maticemi, matice 
je reprezentována datovým typ array.


```python
import numpy as np

m1 = np.array([[1,2,3],[3,4,5],[5,6,7], dtype='float')

print(m1)
print(m1.shape)
m1.shape[0,0]
```

## Nové matice

Novou matici je kromě přímé udělat pomocí `np.zeros()` a `np.ones()`.

Matici obsahující náhodná čísla s normálním rozložením pak pomocí: `np.random.uniform(-1,1, size=(4,4))`



## Lineární rovnice

V modulu [`numpy.linalg`][linalg] jsou nástroje pro práci 
s lineární algebrou.
 
Zkuste pomocí [linalg.solve][linalg] vyřešit systém rovnic.
```
    3x +  2y - z  =  1 
    1x -  2y + 4z = -2 
    -x + y/2 + z  =  0 
```


[numpy]: https://docs.scipy.org/doc/numpy-1.13.0/reference/index.html
[linalg]: https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.linalg.html
