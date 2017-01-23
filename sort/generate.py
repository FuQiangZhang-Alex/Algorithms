from random import randint


def generate(n):
    f = open(file='numbers.data', mode='w')
    numbers = ''
    for i in range(0, n):
        numbers += str(randint(0, 100)) + ','
    f.write(numbers.rstrip(','))
