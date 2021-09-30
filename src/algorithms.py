from itertools import chain


def flat(source: list) -> list:
    return list(chain(*source))

def get_num_digits(value: list) -> int:
    return len(str(value))


def insertion_sort(source: list):
    loop_range = len(source)
    cloned = [*source]

    for i in range(1, loop_range):
        key = cloned[i]
        j = i - 1

        while j >= 0 and cloned[j] > key:
            cloned[j + 1] = cloned[j]
            j = j - 1

        cloned[j + 1] = key

    return cloned

def radix_sort(source: list) -> list:
    maximum = max(source)
    digits = get_num_digits(maximum)

    for digit in range(digits):
        bucket = [[] for _ in range(10)]

        for item in source:
            index = item // 10 ** digit % 10
            bucket[index].append(item)

        source = flat(bucket)

    return source


def bubble_sort(source: list) -> list:
    cloned = [*source]
    is_sorted = False

    while not is_sorted:
        is_sorted = True

        for i in range(len(cloned) - 1):
            if cloned[i] > cloned[i + 1]:
                cloned[i + 1], cloned[i] = cloned[i], cloned[i + 1]
                is_sorted = False

    return cloned

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
  
    for j in range(low, high):  
        if arr[j] <= pivot:  
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
  
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(source: list):
    cloned = [*source]
    _quick_sort(cloned, 0, len(cloned) -1)
    return cloned

def _quick_sort(source, low, high):
    if len(source) == 1:
        return source
    if low < high:
        partitioned = partition(source, low, high)
        _quick_sort(source, low, partitioned-1)
        _quick_sort(source, partitioned+1, high)


def merge_sort(source: list):
    cloned = [*source]
    _merge_sort(cloned)
    return cloned

def _merge_sort(source: list):
    if len(source) > 1:
  
         # Finding the mid of the array
        mid = len(source)//2
  
        # Dividing the array elements
        L = source[:mid]
  
        # into 2 halves
        R = source[mid:]
  
        # Sorting the first half
        _merge_sort(L)
  
        # Sorting the second half
        _merge_sort(R)
  
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                source[k] = L[i]
                i += 1
            else:
                source[k] = R[j]
                j += 1
            k += 1
  
        # Checking if any element was left
        while i < len(L):
            source[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            source[k] = R[j]
            j += 1
            k += 1