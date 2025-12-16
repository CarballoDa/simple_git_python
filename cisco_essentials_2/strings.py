"""capitalize(): cambia todas las letras de la cadena a mayúsculas.
center(): centra la cadena dentro de una longitud conocida.
count(): cuenta las ocurrencias de un carácter dado.
join(): une todos los elementos de una tupla/lista en una cadena.
lower(): convierte todas las letras de la cadena en minúsculas.
lstrip(): elimina los caracteres en blanco al principio de la cadena.
replace(): reemplaza una subcadena dada con otra.
rfind(): encuentra una subcadena comenzando por el final de la cadena.
rstrip(): elimina los caracteres en blanco al final de la cadena.
split(): divide la cadena en una subcadena usando un delimitador dado.
strip(): elimina los espacios en blanco iniciales y finales.
swapcase(): intercambia las mayúsculas y minúsculas de las letras.
title(): hace que la primera letra de cada palabra sea mayúscula.
upper(): convierte todas las letras de la cadena en mayúsculas.


El contenido de las cadenas se puede determinar mediante los siguientes métodos (todos devuelven valores booleanos):

endswith(): ¿La cadena termina con una subcadena determinada?
isalnum(): ¿La cadena consta solo de letras y dígitos?
isalpha(): ¿La cadena consta solo de letras?
islower(): ¿La cadena consta solo de letras minúsculas?
isspace(): ¿La cadena consta solo de espacios en blanco?
isupper(): ¿La cadena consta solo de letras mayúsculas?
startswith(): ¿La cadena consta solo de letras mayúsculas?

def mysplit(str):
    result = []
    index = 0
    while(True):
        index = str.find(" ")
        if index >= 0:
            result.append(str[0:index])
            str = str[index + 1:]
        elif index == -1 and str != "":
            result.append(str)
            break
        else:
            break
    return result

print(mysplit("Ser o no ser, esa es la cuestión"))
print(mysplit("Ser o no ser, esa es la cuestión"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))


Methods:
capitalize(): changes all letters in the string to uppercase.
center(): centers the string within a known length.
endswith(): does the string end with a given substring?
find(): finds a substring starting from the beginning of the string.
isalnum(): does the string consist only of letters and digits?
isalpha(): does the string consist only of letters?
isDigit(): does the string consist only of digits?
islower(): does the string consist only of lowercase letters?
isspace(): does the string consist only of whitespace?
isupper(): does the string consist only of uppercase letters?       
join(): joins all elements of a tuple/list into a string.
lower(): converts all letters in the string to lowercase.
lstrip(): removes whitespace characters at the beginning of the string.
replace(): replaces a given substring with another.
rfind(): finds a substring starting from the end of the string.
rstrip(): removes whitespace characters at the end of the string.
split(): divide la cadena y crea una lista de todas las subcadenas detectadas.
startswith() es un espejo del método endswith(), comprueba si una cadena dada comienza con la subcadena especificada.
strip() combina los efectos causados por rstrip() y lstrip(), crea una nueva cadena que carece de todos los espacios en blanco iniciales y finales.
swapcase() crea una nueva cadena intercambiando todas las letras por mayúsculas o minúsculas dentro de la cadena original: los caracteres en mayúscula se convierten en minúsculas y viceversa.
title() realiza una función algo similar cambia la primera letra de cada palabra a mayúsculas, convirtiendo todas las demás a minúsculas.
upper() hace una copia de la cadena de origen, reemplaza todas las letras minúsculas con sus equivalentes en mayúsculas, y devuelve la cadena como resultado.


Las cadenas en Python pueden ser comparadas usando el mismo conjunto de operadores que se emplean con los números.

Observa estos operadores, también sirven para comparar cadenas (compara valores de puntos de código, carácter por carácter):

==
!=
>
>=
<
<=

'alpha' == 'alpha' -> True
'alpha' != 'Alpha' -> True
'alpha' < 'alphabet' -> True

La comparación de cadenas siempre distingue entre mayúsculas y minúsculas (las letras mayúsculas se consideran menores en comparación con las minúsculas).

'beta' > 'Beta' -> True

Aún si una cadena contiene solo dígitos, todavía no es un número. Se interpreta como lo que es, como cualquier otra cadena regular, y su aspecto numérico 
(potencial) no se toma en cuenta, en ninguna manera. Ordenando ASC el valor '8' está antes que el '20', luego '8' es mayor que '20'

print('10' == '010') -> False
print('10' > '010') -> True
print('10' > '8') -> False
print('20' < '8') -> True
print('20' < '80') -> True

El comparar cadenas con los números generalmente es una mala idea.

Las únicas comparaciones que puede realizar con impunidad son aquellas simbolizadas por los operadores == y !=. El primero siempre devuelve False (falso), 
mientras que el segundo siempre devuelve True (verdadero).
El uso de cualquiera de los operadores de comparación restantes generará una excepción TypeError.

print('10' == 10) -> False
print('10' != 10) -> True
print('10' == 1) -> False
print('10' != 1) -> True
print('10' > 10) -> TypeError exception

Ordenar listas que contienen cadenas: 
Con func sorted() genera una nueva lista ordenada:

first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)

Con func sort() no se genera una nueva lista ordenada, sino que se ordena la propia lista:

second_greek = ['omega', 'alpha', 'pi', 'gamma']
second_greek.sort()

La conversión de cadena a número es simple, ya que siempre es posible. 
Se realiza mediante una función llamada str():

itg = 13
flt = 1.3
si = str(itg)
sf = str(flt)

La conversión inversa solo es posible cuando la cadena representa un número válido. Si no se cumple la condición, espera una excepción ValueError.
Se realiza mediante una función llamada int(), float():

si = '13'
sf = '1.3'
itg = int(si)
flt = float(sf)

Cuestinario:

'smith' > 'Smith' -> True
'Smiths' < 'Smith'
'Smith' > '1000' -> True
'11' < '8' -> True


s1 = '¿Dónde están las nieves de antaño?'
s2 = s1.split()
s3 = sorted(s2)
print(s3[1]) -> de


s1 = '12.8' -> El código genera una excepción ValueError.
i = int(s1)
s2 = str(i)
f = float(s2)
print(s1 == s2)

"""