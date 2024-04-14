import tkinter as tk
from tkinter import ttk
import random
import time

# Utility functions for sorting with time measurements
def selection_sort(data):
    start = time.time()
    arr = data[:]
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    end = time.time()
    return arr, end - start

def bubble_sort(data):
    start = time.time()
    arr = data[:]
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    end = time.time()
    return arr, end - start

def insertion_sort(data):
    start = time.time()
    arr = data[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    end = time.time()
    return arr, end - start

def merge_sort(data):
    start = time.time()
    arr = merge_sort_recursive(data)
    end = time.time()
    return arr, end - start

def merge_sort_recursive(data):
    if len(data) > 1:
        mid = len(data) // 2
        L = merge_sort_recursive(data[:mid])
        R = merge_sort_recursive(data[mid:])
        data = []
        while L and R:
            if L[0] < R[0]:
                data.append(L.pop(0))
            else:
                data.append(R.pop(0))
        data.extend(L or R)
    return data

def quick_sort(data):
    start = time.time()
    arr, _ = quick_sort_recursive(data)
    end = time.time()
    return arr, end - start

def quick_sort_recursive(data):
    if len(data) <= 1:
        return data, 0
    else:
        pivot = data[0]
        left = [x for x in data[1:] if x <= pivot]
        right = [x for x in data[1:] if x > pivot]
        left_sorted, left_time = quick_sort_recursive(left)
        right_sorted, right_time = quick_sort_recursive(right)
        return left_sorted + [pivot] + right_sorted, left_time + right_time

def heap_sort(data):
    start = time.time()
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i)
    for i in range(n - 1, 0, -1):
        data[0], data[i] = data[i], data[0]
        heapify(data, i, 0)
    end = time.time()
    return data, end - start

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[largest] < arr[left]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def comb_sort(data):
    start = time.time()
    gap = len(data)
    shrink = 1.3
    sorted = False
    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted = True
        i = 0
        while i + gap < len(data):
            if data[i] > data[i + gap]:
                data[i], data[i + gap] = data[i + gap], data[i]
                sorted = False
            i += 1
    end = time.time()
    return data, end - start

# Generates random colors for the rectangles
def generate_colors(n):
    return ['#' + ''.join(random.choices('0123456789ABCDEF', k=6)) for _ in range(n)]

# Draws rectangles on a canvas based on the array values
def draw_rectangles(canvas, arr, colors):
    canvas.delete("all")
    c_width = int(canvas.cget("width"))
    c_height = int(canvas.cget("height"))
    bar_width = c_width / len(arr)
    max_height = max(arr, default=1)
    for i, val in enumerate(arr):
        x0 = i * bar_width
        y0 = c_height - (val * c_height / max_height)
        x1 = (i + 1) * bar_width
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colors[i], outline='white')

# Handles user input, performs sorting, and updates UI
def sort_and_draw():
    numbers = list(map(int, numbers_entry.get().split()))
    if not numbers:
        result_label.config(text="Please enter numbers separated by spaces.")
        return
    colors = generate_colors(len(numbers))
    algorithm = algorithm_combobox.get()
    sorted_numbers, sort_time = globals()[algorithm.replace(" ", "_").lower()](numbers)
    draw_rectangles(canvas, sorted_numbers, colors)
    result_label.config(text=f"Sorted in {sort_time:.2f} seconds")
    print(f"{algorithm} sorting took {sort_time:.2f} seconds.")

# Setup the main application window
app = tk.Tk()
app.title("Sorting Algorithms Visualization")

canvas = tk.Canvas(app, width=600, height=400, bg='white')
canvas.pack()

algorithm_label = tk.Label(app, text="Choose a sorting algorithm:")
algorithm_label.pack()
algorithm_combobox = ttk.Combobox(app, values=[
    "Selection Sort", "Bubble Sort", "Insertion Sort", "Merge Sort",
    "Quick Sort", "Heap Sort", "Comb Sort"
])
algorithm_combobox.pack()

numbers_label = tk.Label(app, text="Enter numbers separated by spaces:")
numbers_label.pack()
numbers_entry = tk.Entry(app)
numbers_entry.pack()

sort_button = tk.Button(app, text="Sort and Visualize", command=sort_and_draw)
sort_button.pack()

result_label = tk.Label(app, text="Result:")
result_label.pack()

app.mainloop()


