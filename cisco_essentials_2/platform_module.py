from platform import platform, machine, processor, system, version

"""El módulo platform permite acceder a los datos de la plataforma subyacente, es decir, 
hardware, sistema operativo e información sobre la versión del intérprete.

Existe también una función que puede mostrar todas las capas subyacentes en un solo vistazo, llamada platform. 
Simplemente devuelve una cadena que describe el entorno; por lo tanto, su salida está más dirigida a los humanos 
que al procesamiento automatizado (lo verás pronto)."""

print(platform(aliased = False, terse = False))

print(platform())
print(platform(False))
print(platform(True, False))
print(platform(True, True))

"""La función machine

En ocasiones, es posible que solo se desee conocer el nombre genérico del procesador que ejecuta el sistema operativo 
junto con Python y el código, una función llamada machine() te lo dirá. Como anteriormente, la función devuelve una cadena."""

print(machine())

"""La función processor() devuelve una cadena con el nombre real del procesador (si lo fuese posible).
"""

print(processor())

"""Una función llamada system() devuelve el nombre genérico del sistema operativo en una cadena.
"""

print(system())

"""La versión del sistema operativo se proporciona como una cadena por la función version()."""

print(version())

"""
python_implementation() → devuelve una cadena que denota la implementación de Python 
(espera CPython aquí, a menos que decidas utilizar cualquier rama de Python no canónica).
python_version_tuple() → devuelve una tupla de tres elementos la cual contiene:
La parte mayor de la versión de Python.
La parte menor.
El número del nivel de parche."""

from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)
