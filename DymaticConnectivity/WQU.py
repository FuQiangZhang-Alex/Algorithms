from generate_test_data import generate


class UF:
    def __init__(self, n):
        self.id = list(range(0, n, 1))
        self.sz = [1] * n

    def connected(self, a, b):
        return (self.root(a) == self.root(b))

    def root(self, i):
    	while self.id[i] != i:
    		i = self.id[i]
    	return i

    def union(self, a, b):
        a_root = self.root(a)
        b_root = self.root(b)
        if self.sz[a_root] < self.sz[b_root]:
            self.id[a_root] = b_root  # make a be b's child
            self.sz[b_root] += self.sz[a_root]
        else:
            self.id[b_root] = a_root
            self.sz[a_root] += self.sz[b_root]

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