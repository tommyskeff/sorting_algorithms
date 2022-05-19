import random
import matplotlib.pyplot as plt
from algorithms.bubble_sort import bubble_sort
from algorithms.merge_sort import merge_sort
from algorithms.quick_sort import quick_sort

MIN_NUMBER = 0
MAX_NUMBER = 1000

MIN_TEST = 0
MAX_TEST = 50
INCREMENT_TEST = 1

REPEATS = 100

def random_list(length):
    lst = []
    for _ in range(length):
        lst.append(random.randint(MIN_NUMBER, MAX_NUMBER))

    return lst


def create_line(function):
    x = []
    y = []

    for i in range(MIN_TEST, MAX_TEST, INCREMENT_TEST):
        comparisons = []
        for _ in range(REPEATS):
            comparisons.append(function(random_list(i))[1])

        x.append(i)
        y.append(sum(comparisons) / len(comparisons))

    return [x, y]


functions = [["Bubble Sort", bubble_sort], ["Merge Sort", merge_sort], ["Quick Sort", quick_sort]]
for f in functions:
    line = create_line(f[1])
    plt.plot(line[0], line[1], label=f[0])

plt.xlabel("Elements")
plt.ylabel("Comparisons")

plt.title("Sorting Algorithms")
plt.legend()
plt.show()
