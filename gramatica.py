# Definicion de terminales y no terminales para los ejercicios
# Usamos 'e' o 'epsilon' para la cadena vacia, una definicion aprendida en la clase del miercoles.

EJERCICIO_1 = {
    'S': [['A', 'uno', 'B', 'C'], ['S', 'dos']],
    'A': [['B', 'C', 'D'], ['A', 'tres'], ['ε']],
    'B': [['D', 'cuatro', 'C', 'tres'], ['ε']],
    'C': [['cinco', 'D', 'B'], ['ε']],
    'D': [['seis'], ['ε']]
}

EJERCICIO_2 = {
    'S': [['A', 'B', 'uno']],
    'A': [['dos', 'B'], ['ε']],
    'B': [['C', 'D'], ['tres'], ['ε']],
    'C': [['cuatro', 'A', 'B'], ['cinco']],
    'D': [['seis'], ['ε']]
}
