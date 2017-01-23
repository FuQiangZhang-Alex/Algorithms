from generate import generate


def elementary_sort(lst):
    length = len(lst)
    i = 0
    while i < length:
        for j in range(i + 1, length):
            if lst[i] > lst[j]:
                swap = lst[i]
                lst[i] = lst[j]
                lst[j] = swap
        i += 1

generate(10)
data = list(map(lambda n: int(n) if n.isnumeric() else 0, open(file='numbers.data', mode='r').readline().split(',')))
print(data)
quick_sort(data)
print(data)
