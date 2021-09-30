from json import dumps
from random import randint
from time import perf_counter
from algorithms import bubble_sort, insertion_sort, radix_sort, quick_sort, merge_sort

def get_times(iteration_range: int, algorithms: list):
    source = [randint(0, 1_000_000) for _ in range(iteration_range)]
    times = {
        "list_size": iteration_range,
        "times": {}
    }

    for algorithm in algorithms:
        start = perf_counter()
        algorithm(source)
        end = perf_counter()
        times["times"][algorithm.__name__] = end - start

    return times

times = []

for i in range(2, 7):
    full_list = [bubble_sort, insertion_sort, merge_sort, radix_sort, quick_sort]
    fastest_list = [merge_sort, radix_sort, quick_sort]
    times.append(get_times(10 ** i, full_list if 10 ** i <= 10_000 else fastest_list))

with open("benchmark.json", "w") as file:
    file.write(dumps(times, indent=4))