from generate_test_data import generate


class UF:
    def __init__(self, n):
        self.id = list(range(0, n, 1))

    def connected(self, a, b):
        return (self.id[a] == self.id[b])

    def union(self, a, b):
        aid = self.id[a]
        bid = self.id[b]
        for i in range(0, len(self.id)):
            if self.id[i] == aid:
                self.id[i] = bid

generate(1000000)
input = open(file='test.data', mode='r', encoding='utf-8')
str_N = input.readline().rstrip('\n')
N = int(str_N) if str_N.isnumeric() else 0
if N <= 1:
    print('error')
else:
    uf = UF(N)
    lines = input.readlines()
    p, q = tuple(map(lambda item: int(item) if item.isnumeric() else 0, lines[-1].rstrip('\n').split(',')))
    for line in lines[:-1]:
        connection = tuple(map(lambda item: int(item) if item.isnumeric() else 0, line.rstrip('\n').split(',')))
        a, b = connection
        uf.union(a, b)
        # do union operation
    print(uf.connected(p, q))
