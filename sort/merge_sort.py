from generate import generate


def merge(lst, lo, mid, hi):
    print(lst)
    aux = lst.copy()
    i, j = lo, mid + 1
    for k in range(lo, hi + 1):
        if i > mid:
            lst[k] = aux[j]
            j += 1
        elif j > hi:
            lst[k] = aux[i]
            i += 1
        elif aux[i] < aux[j]:
            lst[k] = aux[i]
            i += 1
        else:
            lst[k] = aux[j]
            j += 1
    return lst

def merge_sort(lst, lo, hi):
    if hi <= lo:
        return
    mid = lo + int((hi - lo) / 2)
    merge_sort(lst, lo, mid)
    merge_sort(lst, mid + 1, hi)
    merge(lst, lo, mid, hi)

generate(10)
data = list(map(lambda n: int(n) if n.isnumeric() else 0, open(file='numbers.data', mode='r').readline().split(',')))
print(data)
index = len(data) - 1
merge_sort(data, 0, index)
print(data)
