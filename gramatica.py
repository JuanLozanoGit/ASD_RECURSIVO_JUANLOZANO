# Definicion de gramaticas y simbolos
# 'e' representa epsilon (vacio)

TERMINALES = {'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'id', 'igual', 'num', 'puntoycoma', '$'}

# Gramatica del Ejercicio 2 (La del Ejercicio 1 tiene recursividad y rompe el LL1)
EJERCICIO_2 = {
    'S': [['A', 'B', 'uno']],
    'A': [['dos', 'B'], ['e']],
    'B': [['C', 'D'], ['tres'], ['e']],
    'C': [['cuatro', 'A', 'B'], ['cinco']],
    'D': [['seis'], ['e']]
}

# Gramatica del Ejercicio 3 (Un IF o ASIGNACION simple)
EJERCICIO_3 = {
    'S': [['A', 'B']],
    'A': [['id', 'igual', 'E']],
    'B': [['puntoycoma'], ['e']],
    'E': [['num'], ['id']]
}
