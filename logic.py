def get_first(sym, grammar, memo):
    if sym in memo: return memo[sym]
    if sym not in grammar: return {sym}
    
    res = set()
    for prod in grammar[sym]:
        if prod == ['ε']:
            res.add('ε')
        else:
            for s in prod:
                f_s = get_first(s, grammar, memo)
                res.update(f_s - {'ε'})
                if 'ε' not in f_s: break
            else: res.add('ε')
    memo[sym] = res
    return res

def get_follow(grammar, firsts, start):
    follow = {nt: set() for nt in grammar}
    follow[start].add('$')
    
    while True:
        changed = False
        for nt, rules in grammar.items():
            for r in rules:
                for i, sym in enumerate(r):
                    if sym in grammar:
                        prev_len = len(follow[sym])
                        rest = r[i+1:]
                        if not rest:
                            follow[sym].update(follow[nt])
                        else:
                            f_rest = set()
                            for s in rest:
                                f_s = firsts.get(s, {s})
                                f_rest.update(f_s - {'ε'})
                                if 'ε' not in f_s: break
                            else: f_rest.add('ε')
                            follow[sym].update(f_rest - {'ε'})
                            if 'ε' in f_rest: follow[sym].update(follow[nt])
                        if len(follow[sym]) > prev_len: changed = True
        if not changed: break
    return follow

def get_predict(grammar, firsts, follows):
    predicts = []
    for nt, rules in grammar.items():
        for r in rules:
            f_prod = set()
            for s in r:
                f_s = firsts.get(s, {s})
                f_prod.update(f_s - {'ε'})
                if 'ε' not in f_s: break
            else: f_prod.add('ε')
            
            p_set = f_prod - {'ε'}
            if 'ε' in f_prod: p_set.update(follows[nt])
            predicts.append((nt, r, p_set))
    return predicts
