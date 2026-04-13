def calcular_first(simbolo, gramatica, cache):
    if simbolo in cache: return cache[simbolo]
    if simbolo not in gramatica: return {simbolo}
    
    resultado = set()
    for prod in gramatica[simbolo]:
        if prod == ['ε'] or prod == ['e']:
            resultado.add('ε')
        else:
            for s in prod:
                f_s = calcular_first(s, gramatica, cache)
                resultado.update(f_s - {'ε'})
                if 'ε' not in f_s: break
            else: resultado.add('ε')
    cache[simbolo] = resultado
    return resultado

def calcular_follow(gramatica, firsts, inicial):
    follow = {nt: set() for nt in gramatica}
    follow[inicial].add('$')
    
    while True:
        cambio = False
        for nt, producciones in gramatica.items():
            for p in producciones:
                for i, simbolo in enumerate(p):
                    if simbolo in gramatica:
                        size_antes = len(follow[simbolo])
                        resto = p[i+1:]
                        if not resto:
                            follow[simbolo].update(follow[nt])
                        else:
                            f_resto = set()
                            for s in resto:
                                f_s = firsts.get(s, {s})
                                f_resto.update(f_s - {'ε'})
                                if 'ε' not in f_s: break
                            else: f_resto.add('ε')
                            follow[simbolo].update(f_resto - {'ε'})
                            if 'ε' in f_resto: follow[simbolo].update(follow[nt])
                        if len(follow[simbolo]) > size_antes: cambio = True
        if not cambio: break
    return follow

def calcular_predict(gramatica, firsts, follows):
    prediccion = []
    for nt, producciones in gramatica.items():
        for p in producciones:
            f_prod = set()
            for s in p:
                f_s = firsts.get(s, {s})
                f_prod.update(f_s - {'ε'})
                if 'ε' not in f_s: break
            else: f_prod.add('ε')
            
            p_set = f_prod - {'ε'}
            if 'ε' in f_prod: p_set.update(follows[nt])
            prediccion.append((nt, p, p_set))
    return prediccion
