import myfirstmodule
print(myfirstmodule.__counter)

from myfirstmodule import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))

""" 
Añadir directorios a la lista de paths usando el modulo sys y así encontrar modulos en carpetas personalizadas.

Ya que una diagonal invertida se usa para escapar de otros caracteres, si deseas obtener solo una diagonal invertida, 
debes escapar.

Hemos utilizado el nombre relativo de la carpeta: esto funcionará si inicia el archivo main.py directamente desde la 
carpeta de inicio, y no funcionará si el directorio actual no se ajusta a la ruta relativa; siempre puedes usar una 
ruta absoluta, como esta:

path.append('C:\\Users\\user\\py\\modules')



from sys import path
 
path.append('..∖∖modules')
 
import module
 
zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))
"""