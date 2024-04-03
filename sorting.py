# sorting.py

def tri_selection(arr):
    """
    Tri par sélection : à chaque itération, trouve l'élément minimum restant
    et le place à la bonne position
    """
    n = len(arr)
    for i in range(n):
        # Trouver l'index du minimum dans la sous-liste non triée
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Echanger l'élément minimum avec le premier élément de la sous-liste non triée
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def tri_bulles(arr):
    """
    Tri à bulles : à chaque itération, compare les éléments adjacents et les échange 
    s'ils sont dans le mauvais ordre
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]
                arr[j], arr[j+1] = arr[j]
    return arr




def tri_bulles(arr):
    # Implémentation du tri à bulles
    pass

def tri_insertion(arr):
    # Implémentation du tri par insertion
    pass

def tri_fusion(arr):
    # Implémentation du tri fusion
    pass

def tri_rapide(arr):
    # Implémentation du tri rapide
    pass

def tri_tas(arr):
    # Implémentation du tri par tas
    pass

def tri_peigne(arr):
    # Implémentation du tri à peigne
    pass
