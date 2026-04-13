class CalculadoraLL1:
    def __init__(self, gramatica):
        self.g = gramatica
        self.non_terminals = list(gramatica.keys())
        self.first = {nt: set() for nt in self.non_terminals}
        self.follow = {nt: set() for nt in self.non_terminals}
        self.predict = {} # (NoTerminal, NumRegla) -> Conjunto

    def obtener_first(self, simbolo):
        if simbolo not in self.non_terminals:
            return {simbolo}
        
        res = set()
        for regla in self.g[simbolo]:
            if regla[0] == 'e':
                res.add('e')
            else:
                for s in regla:
                    f = self.obtener_first(s)
                    res.update(f - {'e'})
                    if 'e' not in f:
                        break
                else:
                    res.add('e')
        return res

    def calcular_todo(self):
        # 1. Calcular FIRST
        for nt in self.non_terminals:
            self.first[nt] = self.obtener_first(nt)

        # 2. Calcular FOLLOW (Simplificado para el ejercicio)
        self.follow[self.non_terminals[0]].add('$')
        
        # Iteracion basica de Follow
        cambio = True
        while cambio:
            antes = str(self.follow)
            for nt, reglas in self.g.items():
                for regla in reglas:
                    for i, simbolo in enumerate(regla):
                        if simbolo in self.non_terminals:
                            restante = regla[i+1:]
                            if not restante:
                                self.follow[simbolo].update(self.follow[nt])
                            else:
                                first_restante = self.obtener_first(restante[0])
                                self.follow[simbolo].update(first_restante - {'e'})
                                if 'e' in first_restante:
                                    self.follow[simbolo].update(self.follow[nt])
            cambio = antes != str(self.follow)

    def imprimir_tablas(self):
        print("\n--- CONJUNTOS FIRST ---")
        for nt, s in self.first.items():
            print(f"FIRST({nt}) = {s}")
            
        print("\n--- CONJUNTOS FOLLOW ---")
        for nt, s in self.follow.items():
            print(f"FOLLOW({nt}) = {s}")
