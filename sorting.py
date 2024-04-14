import time
import random

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


def heapify(arr, n, i):
    largest = i 
    left = 2 * i + 1 
    right = 2 * i + 2 

 
    if left < n and arr[largest] < arr[left]:
        largest = left

    
    if right < n and arr[largest] < arr[right]:
        largest = right

    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] 
        
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def comb_sort(arr):
    gap = len(arr)
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = int(gap // shrink)
        if gap <= 1:
            gap = 1
            sorted = True
        i = 0
        while i + gap < len(arr):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False
            i += 1
    return arr


def measure_sort_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr.copy())
    end_time = time.time()
    return end_time - start_time


random_list = [random.random() for _ in range(1000)]

time_selection = measure_sort_time(selection_sort, random_list)
time_bubble = measure_sort_time(bubble_sort, random_list)
time_insertion = measure_sort_time(insertion_sort, random_list)
time_merge = measure_sort_time(merge_sort, random_list)
time_quick = measure_sort_time(quick_sort, random_list)
time_heap = measure_sort_time(heap_sort, random_list)
time_comb = measure_sort_time(comb_sort, random_list)


print(f"Selection Sort: {time_selection} seconds")
print(f"Bubble Sort: {time_bubble} seconds")
print(f"Insertion Sort: {time_insertion} seconds")
print(f"Merge Sort: {time_merge} seconds")
print(f"Quick Sort: {time_quick} seconds")
print(f"Heap Sort: {time_heap} seconds")
print(f"Comb Sort: {time_comb} seconds")
