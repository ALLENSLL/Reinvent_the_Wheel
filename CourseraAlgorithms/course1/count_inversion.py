def load(filename):
    f = open(filename, 'r')
    numbers = []
    line = f.readline()
    while line:
        numbers.append(int(line))
        line = f.readline()
    f.close()
    return numbers


def merge_sort(numbers):
    n = len(numbers)
    if n == 1:
        return numbers
    else:
        cut = n // 2
        n1 = merge_sort(numbers[:cut])
        n2 = merge_sort(numbers[cut:])
        n = []
        l1, l2 = len(n1), len(n2)
        i, j = 0, 0
        while True:
            if i == l1:
                n += n2[j:]
                break
            if j == l2:
                n += n1[i:]
                break
            a, b = n1[i], n2[j]
            if a < b:
                n.append(a)
                i += 1
            else:
                n.append(b)
                j += 1

        return n


def count_inversion(numbers):
    n = len(numbers)
    if n == 1:
        return numbers, 0
    else:
        cut = n // 2
        n1, c1 = count_inversion(numbers[:cut])
        n2, c2 = count_inversion(numbers[cut:])
        c = c1 + c2
        n = []
        l1, l2 = len(n1), len(n2)
        i, j = 0, 0
        while True:
            if i == l1:
                n += n2[j:]
                break
            if j == l2:
                n += n1[i:]
                break
            a, b = n1[i], n2[j]
            if a < b:
                n.append(a)
                i += 1
            else:
                n.append(b)
                j += 1
                c += l1 - i
        return n, c


if __name__ == '__main__':
    a = load('test_count_inversion.txt')
    s, c = count_inversion(a)
    print(c)