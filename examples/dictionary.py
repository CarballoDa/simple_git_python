'''
1. Los diccionarios son *colecciones indexadas de datos, mutables y desordenadas. 
(*En Python 3.6x los diccionarios están ordenados de manera predeterminada.
'''

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
phone_numbers = {'jefe': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}
 
print(dictionary)
print(phone_numbers)
print(empty_dictionary)

dictionary = {"cat": "gato", "perro": "chien", "caballo": "cheval"}
words = ['gato', 'león', 'caballo']
 
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "no está en el diccionario")
 
# Sangria Francesa : modo de escritura para diccionarios largos 
       
# Ejemplo 1:
dictionary = {
              "gato": "chat",
              "perro": "chien",
              "caballo": "cheval"
}
# Ejemplo 2:
phone_numbers = {'jefe': 5551234567,
              'Suzy': 22657854310
}

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
for spanish, french in dictionary.items():
    print(spanish, "->", french)
 
for french in dictionary.values():
    print(french)   
    
for key in sorted(dictionary.keys()): # or sorted(dictionary.values())
    print(key)
    
dictionary['cisne'] = 'cygne'
print(dictionary.get('cisne')) # cygne - uso de dict.get(key) para obtener el valor de una clave
dictionary.update({"pato": "canard"}) # uso de dict.update(key:value) para añadir un nuevo par al diccionario
print(dictionary)

del dictionary['perro']
print(dictionary)

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
dictionary.popitem() # uso de dict.popitem() que borra el ultimo par key - value : "caballo": "cheval"
print(dictionary) # salida: {'gato': 'chat', 'perro': 'chien'}

dictionary.clear() # uso e dict.clear() para elimnar todos los elementos. Dicinario vacío.

dictionary_copy = dictionary.copy() # uso e dict.copy() para copiar todos los elementos en un nuevo diccionario