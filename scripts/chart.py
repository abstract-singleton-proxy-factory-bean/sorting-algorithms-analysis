import matplotlib.pyplot as plt
from json import loads


def map(callback, source):
    mapped = []

    for item in source:
        mapped.append(callback(item))

    return mapped


with open("results.json", "r") as file:
    data = loads("".join(file.readlines()))

    for set in data:
        filename = f"list-{set['list_size']}.png"
        keys = list(set['times'].keys())
        data = map(lambda key: set['times'][key], keys)

        figure, axes = plt.subplots()
        axes.bar(keys, data)
        axes.set_xlabel("Algorithm")
        axes.set_ylabel("Time (seconds)")
        plt.savefig(f"images/{filename}")
