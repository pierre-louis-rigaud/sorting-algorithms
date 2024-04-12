import time
import random

# Define the selection sort algorithm
def selection_sort(arr):
    # Iterate through each element in the array
    for i in range(len(arr)):
        # Assume the first element is the minimum
        min_idx = i
        # Check the rest of the array for a smaller element
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Define the bubble sort algorithm
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the array
    for i in range(n):
        # Last elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1 and swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Define the insertion sort algorithm
def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# Define the merge sort algorithm
def merge_sort(arr):
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr)//2
        # Dividing the array elements into 2 halves
        L = arr[:mid]
        R = arr[mid:]

        # Sorting the first half
        merge_sort(L)
        # Sorting the second half
        merge_sort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Define the quick sort algorithm
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        # Partitioning the array on the basis of pivot
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Define the heapify function for heap sort
def heapify(arr, n, i):
    largest = i # Initialize largest as root
    left = 2 * i + 1 # left = 2*i + 1
    right = 2 * i + 2 # right = 2*i + 2

    # See if left child of root exists and is greater than root
    if left < n and arr[largest] < arr[left]:
        largest = left

    # See if right child of root exists and is greater than the largest so far
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] # swap
        # Heapify the root
        heapify(arr, n, largest)

# Define the heap sort algorithm
def heap_sort(arr):
    n = len(arr)
    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # Extract elements one by one
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap
        heapify(arr, i, 0)
    return arr

# Define the comb sort algorithm
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

# Function to measure the execution time of sorting functions
def measure_sort_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr.copy())
    end_time = time.time()
    return end_time - start_time

# Generate a random list of real numbers
random_list = [random.random() for _ in range(1000)]

# Measure sort time for each sorting algorithm
time_selection = measure_sort_time(selection_sort, random_list)
time_bubble = measure_sort_time(bubble_sort, random_list)
time_insertion = measure_sort_time(insertion_sort, random_list)
time_merge = measure_sort_time(merge_sort, random_list)
time_quick = measure_sort_time(quick_sort, random_list)
time_heap = measure_sort_time(heap_sort, random_list)
time_comb = measure_sort_time(comb_sort, random_list)

# Print out the timing results
print(f"Selection Sort: {time_selection} seconds")
print(f"Bubble Sort: {time_bubble} seconds")
print(f"Insertion Sort: {time_insertion} seconds")
print(f"Merge Sort: {time_merge} seconds")
print(f"Quick Sort: {time_quick} seconds")
print(f"Heap Sort: {time_heap} seconds")
print(f"Comb Sort: {time_comb} seconds")
