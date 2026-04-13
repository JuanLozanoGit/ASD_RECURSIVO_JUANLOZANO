from gramatica import EJERCICIO_1, EJERCICIO_2
from algoritmos import calcular_first, calcular_follow, calcular_predict

def mostrar_resultados(titulo, g, inicio):
    print(f"\n{'#'*30}\n# {titulo}\n{'#'*30}")
    
    # 1. Calcular FIRST
    primeros = {nt: calcular_first(nt, g, {}) for nt in g}
    print("\n[+] CONJUNTOS FIRST:")
    for nt, v in primeros.items(): print(f"    FIRST({nt}) = {v}")
    
    # 2. Calcular FOLLOW
    siguientes = calcular_follow(g, primeros, inicio)
    print("\n[+] CONJUNTOS FOLLOW:")
    for nt, v in siguientes.items(): print(f"    FOLLOW({nt}) = {v}")
    
    # 3. Calcular PREDICT
    predicciones = calcular_predict(g, primeros, siguientes)
    print("\n[+] CONJUNTOS DE PREDICCION:")
    for nt, p, res in predicciones:
        print(f"    P({nt} -> {' '.join(p)}) = {res}")

if __name__ == "__main__":
    # Ejecutar para Ejercicio 1
    try:
        mostrar_resultados("EJERCICIO 1 - DIAPO 34", EJERCICIO_1, 'S')
    except RecursionError:
        print("\n[!] Error: La Gramatica 1 tiene recursividad izquierda directa.")

    # Ejecutar para Ejercicio 2
    mostrar_resultados("EJERCICIO 2 - DIAPO 35", EJERCICIO_2, 'S')
