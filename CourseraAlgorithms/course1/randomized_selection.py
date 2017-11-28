import random
# import numpy as np


def load(filename):
    f = open(filename, 'r')
    numbers = []
    line = f.readline()
    while line:
        numbers.append(int(line))
        line = f.readline()
    f.close()
    return numbers


def randomized_selection(numbers, k):
    # find the k-th smallest number
    n = len(numbers)
    if n == 1:
        return numbers[0]
    else:
        index = random.choice(range(n))
        numbers[0], numbers[index] = numbers[index], numbers[0]
        pivot = numbers[0]
        i = 1
        for j in range(1, n):
            if numbers[j] < pivot:
                numbers[j], numbers[i] = numbers[i], numbers[j]
                i += 1
        numbers[0], numbers[i-1] = numbers[i-1], numbers[0]

        if i == k:
            return numbers[i-1]
        elif i > k:
            return randomized_selection(numbers[:i-1], k)
        else:
            return randomized_selection(numbers[i:], k-i)


if __name__ == '__main__':
    a = load('test_quick_sort.txt')
    print(randomized_selection(a, 10000))
