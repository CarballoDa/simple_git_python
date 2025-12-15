"""
import random
random.seed(42) # establece la semilla para la generación de números aleatorios
print([random.randint(1, 10) for _ in range(5)])
# Siempre dará la misma lista si la semilla es 42
random.seed(42)
print([random.randint(1, 10) for _ in range(5)])
random.seed(40)
print([random.randint(1, 10) for _ in range(5)])


random.seed()  # usa la hora actual como semilla
print([random.randint(1, 10) for _ in range(5)])

random.seed('a') # usa una cadena como semilla
print([random.randint(1, 10) for _ in range(5)])
"""
import random
from random import randrange, randint

def reset_seed(seed_value=None):
    random.seed(seed_value)

def two_rands(seed_value=None, list_style='-'):
    reset_seed(seed_value)
    for i in range(5):
        print(f"{list_style} {random.random()}")

def three_lists():
    for i in range(3):
        print([random.randint(1, 100) for c in range(4)])

# Ejecución
two_rands(7)
two_rands(7, '+')
two_rands(list_style='*')
reset_seed()   # volver a usar entropía del sistema
three_lists()

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))

"""Las funciones choice y sample
Como puedes ver, esta no es una buena herramienta para generar números para la lotería. Afortunadamente, existe una mejor solución que escribir tu propio código para verificar la singularidad de los números "sorteados".

Es una función con el nombre de choice:

choice(secuencia)
sample(secuencia, elementos_a_elegir=1)
La primera variante elige un elemento "aleatorio" de la secuencia de entrada y lo devuelve.
El segundo crea una lista (una muestra) que consta del elemento elementos_a_elegir (que por defecto es 1) «sorteado» de la secuencia de entrada."""

from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))


