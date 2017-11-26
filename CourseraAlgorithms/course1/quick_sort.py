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


def quick_sort(numbers, count, start=-1, end=-1):
    if start == -1:
        start = 0
        end = len(numbers)-1
    n = end - start + 1
    if n <= 1:
        return
    else:
        pivot = numbers[start]
        i = start + 1
        for j in range(start+1,end+1):
            count[0] += 1
            if numbers[j] < pivot:
                numbers[j], numbers[i] = numbers[i], numbers[j]
                i += 1
        numbers[start], numbers[i-1] = numbers[i-1], numbers[start]

        quick_sort(numbers, count, start, i-2)
        quick_sort(numbers, count, i, end)

if __name__ == '__main__':
    a = load('test_quick_sort.txt')
    count = [0]
    quick_sort(a, count)
    print(count[0])
