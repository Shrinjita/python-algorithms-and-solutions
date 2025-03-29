def max_influence(n, animals):
    pig_influence = None
    nonpig = []
    for species, influence in animals:
        if species == "pig":
            if pig_influence is None or influence > pig_influence:
                pig_influence = influence
        else:
            nonpig.append(influence)
    if pig_influence is None:
        return 0
    validnonpig = [inf for inf in nonpig if inf < pig_influence]
    totinf = pig_influence + sum(validnonpig)
    return totinf

n = int(input()) 
animals = [input().split() for _ in range(n)]
animals = [(species, int(influence)) for species, influence in animals]
print(max_influence(n, animals))