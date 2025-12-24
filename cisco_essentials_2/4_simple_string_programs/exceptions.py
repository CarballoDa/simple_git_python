"""
Práctica con excepciones
"""

def safe_int(value: str) -> int|str:
    try:
        return int(value)
    except ValueError:
        return 'Error: entrada no convertible a número entero.'
    
print(safe_int('4'))
print(safe_int('14'))
print(safe_int('a'))