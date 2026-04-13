from gramatica import EJERCICIO_2, EJERCICIO_3
from calculadora_ll1 import CalculadoraLL1

def resolver_ejercicio(nombre, g):
    print(f"\n{'='*10} {nombre} {'='*10}")
    calc = CalculadoraLL1(g)
    calc.calcular_todo()
    calc.imprimir_tablas()
    
    # Explicacion de la condicion LL(1) segun el PDF
    print("\n[INFO] Verificando condicion LL(1)...")
    print("Si un simbolo aparece en dos conjuntos de prediccion del mismo NT, no es LL(1).")

if __name__ == "__main__":
    # El Ejercicio 1 suele omitirse en el solver automatico por la recursividad izquierda
    resolver_ejercicio("EJERCICIO 2", EJERCICIO_2)
    resolver_ejercicio("EJERCICIO 3", EJERCICIO_3)
