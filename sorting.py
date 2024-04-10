# Implémentation de différents algorithmes de tri en Python

def tri_selection(arr):
    # Parcours de chaque élément du tableau
    for i in range(len(arr)):
        # Trouver le minimum dans le reste du tableau
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Échanger le minimum trouvé avec le premier élément
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def tri_bulles(arr):
    n = len(arr)
    # Parcourir tous les éléments du tableau
    for i in range(n):
        for j in range(0, n-i-1):
            # Échanger si l'élément trouvé est plus grand que le suivant
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def tri_insertion(arr):
    # Parcourir de 1 à la taille du tableau
    for i in range(1, len(arr)):
        key = arr[i]
        # Déplacer les éléments de arr[0..i-1], qui sont plus grands que key,
        # à une position en avant de leur position actuelle
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    return arr

def tri_fusion(arr):
    if len(arr) > 1:
        # Trouver le milieu du tableau
        mid = len(arr)//2
        # Diviser le tableau en deux moitiés
        L = arr[:mid]
        R = arr[mid:]
        # Trier chaque moitié
        tri_fusion(L)
        tri_fusion(R)
        i = j = k = 0
        # Copier les données dans les tableaux temporaires L[] et R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # Vérifier s'il reste des éléments
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def partition(arr, low, high):
    # Élément pivot
    pivot = arr[high]
    i = (low-1)
    for j in range(low, high):
        # Si l'élément actuel est plus petit que le pivot
        if arr[j] < pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def tri_rapide(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        # pi est l'index de partitionnement, arr[p] est maintenant à la bonne place
        pi = partition(arr, low, high)
        # Trier séparément les éléments avant et après la partition
        tri_rapide(arr, low, pi-1)
        tri_rapide(arr, pi+1, high)
    return arr

def tri_tas(arr):
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1  # gauche
        r = 2 * i + 2  # droite
        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # échange
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # échange
        heapify(arr, i, 0)
    return arr

def tri_peigne(arr):
    gap = len(arr)
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / shrink)
        if gap > 1:
            sorted = False
        else:
            gap = 1
            sorted = True

        i = 0
        while i + gap < len(arr):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False
            i += 1
    return arr

# Test de fonctionnalité pour chaque algorithme de tri
test_arr = [64, 34, 25, 12, 22, 11, 90]

print("Input:", test_arr)
print("Tri par sélection:", tri_selection(test_arr.copy()))
print("Tri à bulles:", tri_bulles(test_arr.copy()))
print("Tri par insertion:", tri_insertion(test_arr.copy()))
print("Tri fusion:", tri_fusion(test_arr.copy()))
print("Tri rapide:", tri_rapide(test_arr.copy(), 0, len(test_arr)-1))
print("Tri par tas:", tri_tas(test_arr.copy()))
print("Tri à peigne:", tri_peigne(test_arr.copy()))

