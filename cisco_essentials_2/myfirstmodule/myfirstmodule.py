"""A diferencia de muchos otros lenguajes de programación, Python no tiene medios para permitirte 
ocultar tales variables a los ojos de los usuarios del módulo.

Solo puedes informar a tus usuarios que esta es tu variable, que pueden leerla, pero que no deben 
modificarla bajo ninguna circunstancia.

Esto se hace anteponiendo al nombre de la variable _ (un guión bajo) o __ (dos guiones bajos), pero recuerda, 
es solo un acuerdo. Los usuarios de tu módulo pueden obedecerlo o no."""

__counter = 0

def suml(the_list):
  global __counter
  __counter += 1
  the_sum = 0
  for element in the_list:
   the_sum += element
  return the_sum
 
 
def prodl(the_list):
  global __counter
  __counter += 1
  prod = 1
  for element in the_list:
   prod *= element
  return prod
 
 
if __name__ == "__main__":
  print("Prefiero ser un módulo, pero puedo hacer algunas pruebas para usted.")
  my_list = [i+1 for i in range(5)]
  print(suml(my_list) == 15)
  print(prodl(my_list) == 120)

"""Podemos decir que:

Cuando se ejecuta un archivo directamente, su variable __name__ se establece a __main__;
Cuando un archivo se importa como un módulo, su variable __name__ se establece al nombre 
del archivo (excluyendo a .py)"""

