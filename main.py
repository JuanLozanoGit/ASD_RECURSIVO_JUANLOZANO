from logic import get_first, get_follow, get_predict

# Gramaticas de las diapositivas
g1 = {
    'S': [['A', 'uno', 'B', 'C'], ['S', 'dos']],
    'A': [['B', 'C', 'D'], ['A', 'tres'], ['ε']],
    'B': [['D', 'cuatro', 'C', 'tres'], ['ε']],
    'C': [['cinco', 'D', 'B'], ['ε']],
    'D': [['seis'], ['ε']]
}

g2 = {
    'S': [['A', 'B', 'uno']],
    'A': [['dos', 'B'], ['ε']],
    'B': [['C', 'D'], ['tres'], ['ε']],
    'C': [['cuatro', 'A', 'B'], ['cinco']],
    'D': [['seis'], ['ε']]
}

def run(name, g, start):
    print(f"\n--- {name} ---")
    fsts = {nt: get_first(nt, g, {}) for nt in g}
    flws = get_follow(g, fsts, start)
    preds = get_predict(g, fsts, flws)

    print("\nFIRST:")
    for k, v in fsts.items(): print(f" {k}: {v}")
    print("\nFOLLOW:")
    for k, v in flws.items(): print(f" {k}: {v}")
    print("\nPREDICCION:")
    for nt, r, p in preds: print(f" {nt} -> {' '.join(r)} | {p}")

if __name__ == "__main__":
    run("Ejercicio 1", g1, 'S')
    run("Ejercicio 2", g2, 'S')
