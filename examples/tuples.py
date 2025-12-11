# HAce falta la coma al final cuando tiene solo un valor. en caso contrario no será una tupla.
tuple_zero = (1,)

tuple_a = (1, 2, 3)
tuple_b = 1,2,3,4
tuple_c = tuple_a + tuple_b
tuple_d = tuple_a * 3

'''
print(tuple_a)
print(tuple_b)
print(tuple_C)
print(tuple_c)
print(tuple_d)

print(type(tuple_a))
print(isinstance(tuple_b, tuple))

print(1 in tuple_c)
print(1 not in tuple_c)

print(tuple_b[0])
print(tuple_b[:-2])

print(len(tuple_b))

for elem in tuple_a:
    print(elem)
    
'''

var = 123

t1 = (1,)
t2 = (2,)
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

'''
print(t1, t2, t3)
'''

x = 10
y = 20
t = (x + y, x * y)

'''
print(t)  # (30, 200)
'''

my_tuple = (1, 2, True, "una cadena", (3, 4), [5, 6], None)
print(my_tuple)

one_elem_tuple_1 = ("uno", ) # Paréntesis y una coma.
one_elem_tuple_2 = "uno", # Sin paréntesis, solo la coma.

my_tuple_2 = 1 # Esto no es una tupla.
print(type(my_tuple_2)) # salida: <class 'int'>

my_tuple = 1, 2, 3,
del my_tuple
# print(my_tuple) # NameError: name 'my_tuple' is not defined

# convertir un iterable en una lista con la funcion list()
tup = 1, 2, 3,
my_list = list(tup)
print(type(my_list)) # salida: <class 'list'>