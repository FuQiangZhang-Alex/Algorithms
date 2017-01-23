from random import randint

def generate(N=10):
	file = open(file='test.data', mode='w', encoding='utf-8')
	file.write(str(N) + '\n')
	for i in range(0, N):
		a, b = randint(0, N - 1), randint(0, N - 1)
		file.write(str(a) + ',' + str(b) + '\n')
	file.close()
