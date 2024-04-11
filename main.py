#Enlevez le pychache 
# main.py

import sorting  
import random
import time

def generate_random_list(size):
    """Génère une liste de nombres entiers aléatoires."""
    return [random.randint(1, 100) for _ in range(size)]

def execute_sorting(algorithm, arr):
    """Exécute l'algorithme de tri et mesure le temps d'exécution."""
    start_time = time.time()
    sorted_arr = algorithm(arr)
    end_time = time.time()
    return sorted_arr, end_time - start_time

def main():
    print("Algorithmes de tri disponibles :")
    print("1. Tri par sélection")
    print("2. Tri à bulles")
    print("3. Tri par insertion")
    print("4. Tri fusion")
    print("5. Tri rapide")
    print("6. Tri par tas")
    print("7. Tri à peigne")
    
    choice = int(input("Choisissez un algorithme de tri (1-7): "))
    
    algorithms = {
        1: sorting.tri_selection,
        2: sorting.tri_bulles,
        3: sorting.tri_insertion,
        4: sorting.tri_fusion,
        5: sorting.tri_rapide,
        6: sorting.tri_tas,
        7: sorting.tri_peigne,
    }
    
    if choice not in algorithms:
        print("Choix non valide.")
        return
    
    size = int(input("Entrez la taille de la liste à trier: "))
    arr = generate_random_list(size)
    
    print("Liste non triée :", arr)
    
    sorted_arr, time_taken = execute_sorting(algorithms[choice], arr.copy())
    
    print("Liste triée :", sorted_arr)
    print(f"Temps d'exécution : {time_taken:.5f} secondes.")

if __name__ == "__main__":
    main()



