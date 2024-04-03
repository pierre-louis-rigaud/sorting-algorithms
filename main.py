# main.py
import sorting
import time
import tkinter as tk
import random
import concurrent.futures

def parallel_sorting(algorithm, arr):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(algorithm, arr)
        return future.result()

def draw_points(canvas, points):
    canvas.delete("all")
    for i, point in enumerate(points):
        x = 50 + i * 20
        y = 300 - point * 5
        canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="blue")

def animate_sorting(canvas, algorithm, points):
    for i in range(len(points)):
        for j in range[i] > points[j]:
            if points[i] > points[j]:
                points[i], points[j] = points[j], points[i]
                draw_points(canvas, points)
                canvas.update()
                time.sleep(0.1)

def main():
    root = tk.Tk()
    root.title("Tri d'algorithme")

    canvas = tk.Canvas(root, width=800, height=600)
    canvas.pack()

    # Générer une liste de nombre aléatoires
    points = [random.randint(1, 100) for _ in range(30)]
    draw_points(canvas, points)

    # Tri et animation
    animate_sorting(canvas, sorting.tri_selection, points)

    root.mainloop()

def measure_execution_time(algorithm, arr):
    start_time = time.time()
    sorted_arr = algorithm(arr)
    end_time = time.time()
    execution_time = end_time - start_time
    return sorted_arr, execution_time

def main():
    # Exemple d'utilisation
    liste = [5, 2, 9, 1, 5, 6]

    # Mesure du temps d'éxecution pour le tri par sélection
    sorted_list, execution_time = measure_execution_time(sorting.tri_selection, liste)
    print("Tri par sélection:", sorted_list)
    print("Temps d'éxécution:", execution_time, "secondes")

    # Mesure du temps d'éxécution pour le Tri à bulles
    sorted_list = measure_execution_time(sorting.tri_bulles, liste)
    print("Tri à bulles:", sorted_list)
    print("Temps d'éxécution:", execution_time, "secondes")

    # Mesure du temps d'éxécution pour le Tri par insertion
    sorted_list = measure_execution_time(sorting.tri_insertion, liste)
    print("Tri par insertion:", sorted_list)
    print("Temps d'éxécution:", execution_time, "secondes")

    # Mesure du temps d'éxécution pour le Tri par fusion
    sorted_list = measure_execution_time(sorting.tri_fusion, liste)
    print("Tri par fusion:", sorted_list)
    print("Temps d'éxécution:", execution_time, "secondes")

    # Mesure du temps d'éxécution pour le Tri rapide
    sorted_list = measure_execution_time(sorting.tri_rapide, liste)
    print("Tri rapide:", sorted_list)
    print("Temps d'éxécution:", execution_time, "secondes")

    # Mesure du temps d'éxécution pour le Tri par tas
    sorted_list = measure_execution_time(sorting.tri_tas, liste)
    print("Tri par tas:", sorted_list)
    print("Temps d'éxécution:", execution_time, "secondes")

    # Mesure du temps d'éxécution pour le Tri à peigne
    sorted_list = measure_execution_time(sorting.tri_peigne, liste)
    print("Tri à peigne:", sorted_list)
    print("Temps d'éxéctuion", execution_time, "secondes")

if __name__ == "__main__":
    main()


