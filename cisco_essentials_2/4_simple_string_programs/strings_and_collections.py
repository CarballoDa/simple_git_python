"""
Colección de ejercicios progresivos, claros, didácticos, y pensados para poder reutilizar los patrones en cualquier práctica o ejercicio.
Organizados por patrones de iteración:
- Iterar por pares
- Ventanas deslizantes (sliding windows)
- Bloques fijos
- Transformaciones de cadenas
- Manejo de excepciones
- Ejercicios mixtos de lógica
"""

# ====================================================
# Nivel 1 — Calentamiento (pares, básicos, sin trucos)
# ====================================================

"""
1. Iterar por pares (índices 0-1, 2-3, 4-5...)
Dada una lista de números, imprime la suma de cada par consecutivo.
[3, 8, 2, 7, 10, 1]  
→  
3+8  
2+7  
10+1
"""

test_list = [3, 8, 2, 7, 10, 1, 8]
for index in range(0, len(test_list), 2):
    print(sum(test_list[index:index + 2]))
    
"""
2. Extraer caracteres en posiciones pares e impares
Dada una cadena, crea dos nuevas cadenas:
- una con los caracteres en posiciones pares
- otra con los caracteres en posiciones impares
"""

txt = ''.join(chr(value) for value in range(ord("a"), ord("z") + 1))
        
print(f"Original: {txt}")
print(f"Pares: {txt[0::2]}") # igual que txt[::2]
print(f"Impares: {txt[1::2]}")

"""
3. Contar cuántos números son mayores que el anterior
Ejemplo:

[1, 3, 2, 5, 7, 4] → 3
"""

test_list = [1, 3, 2, 5, 7, 4]
contador = 0
for index, number in enumerate(test_list):
    if index > 0:
        if number > test_list[index-1]:
            contador += 1
print(f"Numeros mayores que el anterior en lista V1 {test_list} : {contador}")

# Ejercicio 3. V2
contador = 0
for index in range(1, len(test_list)):
    if test_list[index] > test_list[index - 1]:
            contador += 1
print(f"Numeros mayores que el anterior en lista V2 {test_list} : {contador}")

# Ejercicio 3. V3
contador = 0
contador = sum(1 for i in range(1, len(test_list)) if test_list[i] > test_list[i - 1])
print(f"Numeros mayores que el anterior en lista V3 {test_list} : {contador}")

# ================================================
# Nivel 2 — Ventanas deslizantes (sliding windows)
# ================================================

"""
4. Suma de ventanas de tamaño 3
Dada una lista: [1, 2, 3, 4, 5]
Produce:
1+2+3  
2+3+4  
3+4+5
"""

test_list = [1, 2, 3, 4, 5]
for index in range(0, (len(test_list) - 3) + 1):
    print(sum(test_list[index:index + 3]))

"""
5. Detectar si una cadena contiene tres vocales seguidas
Ejemplo:
"cooperación" → True
"murciélago" → False
"cauete" → True
"""

words = ["cooperación" ,"murciélago", "cauete"]
vowels = ["a","e","i","o","u"]
for word in words:
    found = False
    for i in range(len(word) - 2):
        if word[i] in vowels and word[i+1] in vowels and word[i+2] in vowels:
            found = True
            break
    print(f"{word}: {found}")

    
"""
6. Encontrar el máximo de cada ventana de tamaño 4
Ejemplo:
[2, 9, 3, 1, 7, 8]  
→ ventanas: [2,9,3,1], [9,3,1,7], [3,1,7,8]  
→ máximos: 9, 9, 8
"""

test_list = [2, 9, 3, 1, 7, 8]
for index in range(0, len(test_list) - 3):
    print(max(test_list[index:index + 4]))


# ========================================================
# Nivel 3 — Bloques fijos (como los cuadrantes del sudoku)
# ========================================================

"""
7. Dividir una lista en bloques de tamaño N
Ejemplo:
lista = [1,2,3,4,5,6,7,8,9]  
N = 3  
→ [[1,2,3], [4,5,6], [7,8,9]]
"""

N = 3
test_list = [1,2,3,4,5,6,7,8,9]
new_list = []
for index in range(0, len(test_list), N):
    new_list.append(test_list[index:index + N])
print(new_list)

"""
8. Extraer submatrices 2x2 de una matriz 4x4
Ejemplo:
[
 [1,2,3,4],
 [5,6,7,8],
 [9,1,2,3],
 [4,5,6,7]
]
Submatrices:
[[1,2],[5,6]]
[[3,4],[7,8]]
[[9,1],[4,5]]
[[2,3],[6,7]]
"""

matrix_test = [
            [1,2,3,4],
            [5,6,7,8],
            [9,1,2,3],
            [4,5,6,7]
            ]

for x in (0,2):
    for y in (0,2):
        new_matrix = []
        for row_index in range(x, x + 2):
            new_matrix.append(matrix_test[row_index][y:y + 2])
        print(new_matrix) 
        
"""
Versión función control dinámico de dimensión
"""

def get_submatrix(matrix: list, block_size: int) -> list:
    block_size = 2
    for row_start in range(0, len(matrix), block_size):
        for col_start in range(0, len(matrix[0]), block_size):
            block = []
            for r in range(row_start, row_start + block_size):
                block.append(matrix[r][col_start:col_start + block_size])
            break
    return block
            
"""
9. Detectar si una matriz contiene un bloque 3x3 con todos los números iguales
Ejemplo:
[
 [1,1,1,2],
 [1,1,1,2],
 [1,1,1,2],
 [3,3,3,3]
]
→ True"""

matrix_test = [
    [1,1,1,2],
    [1,1,1,2],
    [1,1,1,2],
    [3,3,3,3]
]

grid_size = 3
rows = len(matrix_test)
cols = len(matrix_test[0])
found = False

for row_start in range(rows - grid_size + 1):
    for col_start in range(cols - grid_size + 1):
        block = []
        for r in range(row_start, row_start + grid_size):
            block.extend(matrix_test[r][col_start:col_start + grid_size])
        if len(set(block)) == 1:
            found = True
            break
    if found:
        break

print(found)
        
# PEDNIENTE DESARROLO

# ========================================================
# Nivel 4 — Cadenas y transformaciones
# ========================================================


"""
10. Comprimir una cadena (run-length encoding simple)
Ejemplo:
"aaabbccccd" → "a3b2c4d1"
"""

txt = "aaabbccccd"
encoded_txt = ''
count = 1

for i in range(1, len(txt)):
    if txt[i] == txt[i - 1]:
        count += 1
    else:
        encoded_txt += txt[i - 1] + str(count)
        count = 1

encoded_txt += txt[-1] + str(count)  # último grupo
print(encoded_txt)

"""
11. Invertir palabras pero no el orden
Ejemplo:
"hola mundo desde python"  
→ "aloh odnum edsed nohtyp"
"""

txt = "hola mundo desde python" 
print(' '.join(word[::-1] for word in txt.split()))

"""
12. Detectar si dos cadenas son anagramas
Sin usar sorted().
"""

def are_anagrams(word_a: str, word_b: str) -> bool:
    if len(word_a) == len(word_b):
        for char in word_a:
            if word_a.count(char) != word_b.count(char):
                return False
    else:
        return False
    return True
    
word_a = "nave"
word_b = "vena"
print(f"{word_a} y {word_b} son anagramas?: {are_anagrams(word_a, word_b)}")
word_a = "naves"
word_b = "viena"
print(f"{word_a} y {word_b} son anagramas?: {are_anagrams(word_a, word_b)}")


# ========================================================
# Nivel 5 — Excepciones y lógica
# ========================================================


"""
13. Crear una función que convierta una cadena a entero
Debe:
- devolver el número si es válido
- lanzar ValueError si contiene letras
- lanzar OverflowError si el número tiene más de 10 dígitos
"""

def str_to_int(txt: str) -> int:
    if len(txt) > 10:
        raise OverflowError("el número es demasiado grande")
    if not txt.isdigit():
        raise ValueError("la cadena contiene caracteres no numéricos")
    return int(txt)

print(str_to_int("22222222"))
print(str_to_int("222222223333223"))
print(str_to_int("222a222"))


"""
14. Crear una calculadora segura
Debe manejar:
- división por cero
- tipos incorrectos
- operaciones no soportadas
"""

def calculator(a, b, op: str):
    try:
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            return a / b
        else:
            raise ValueError(f"Operación no soportada: {op}")
    except ZeroDivisionError:
        print("Error: división por cero")
    except TypeError:
        print("Error: tipos incompatibles")
    except ValueError as e:
        print(f"Error: {e}")
        
print(calculator(3,6,'+'))
print(calculator(9,6,'-'))
print(calculator(3,6,'*'))
print(calculator(12,6,'/'))
print(calculator(12,6,'()'))
    
"""
15. Crear una función que reciba una lista y devuelva la media
Debe lanzar:
- TypeError si algún elemento no es numérico
- ZeroDivisionError si la lista está vacía
"""

def med(values: list) -> float:
    if len(values) == 0:
        raise ZeroDivisionError("Error: la lista no puede estar vacía.")
    if not all(isinstance(v, (int, float)) for v in values):
        raise TypeError("Error: todos los elementos deben ser numéricos.")
    return sum(values) / len(values)

print(med([1,33,4,5,7,8]))
print(med([]))
print(med([1,"a",4,5,7,8]))

# ==================================================================
# Nivel 6 — Ejercicios mixtos (lógica + listas + cadenas + ventanas)
# ==================================================================


"""
16. Detectar si una lista contiene una secuencia creciente de longitud 4
Ejemplo:
[1, 3, 2, 4, 5, 6] → True (2,4,5,6)
"""



"""
17. Encontrar la palabra más larga que aparece como substring en todas las cadenas de una lista
Ejemplo:
["transmisión", "misión", "visión"] → "sión"
"""



"""
18. Validar un tablero de “tres en raya”
Comprobar:
- filas
- columnas
- diagonales
"""






"""
¿Cómo seguimos?
Puedo ayudarte de dos formas:
A) Te doy las soluciones paso a paso cuando tú quieras
Tú eliges un ejercicio y lo resolvemos juntos, con análisis y mejoras.
B) Te preparo un cuaderno de práctica progresiva
Con pistas, soluciones parciales y patrones reutilizables.
C) Te preparo un “mini‑curso” de patrones de iteración
Con teoría + ejercicios + ejemplos.
Tú decides el formato. ¿Qué te apetece más para avanzar con fuerza?

"""