#Zadanie 11.1
import random
from math import sqrt


def randomList(n):
    return random.sample(range(n), n)


def partlyrandomList(n):
    result = []
    for i in range(n):
        result.append(i)
    for i in range(n-1):
        check = random.uniform(0, 1)
        if check > 0.8:
            result[i], result[i+1] = result[i+1], result[i]
    return result


def partlyRandomInvertList(n):
    result = []
    for i in range(n-1, -1, -1):
        result.append(i)
    for i in range(n-1):
        check = random.uniform(0, 1)
        if check > 0.8:
            result[i], result[i+1] = result[i+1], result[i]
    return result


def randomGaussList(n):
    result = []
    for i in range(n):
        result.append(random.gauss(0, 1))
    return result


def randomRepeatingList(n):
    result = []
    k = int(sqrt(n))
    for i in range(n):
        result.append(random.randint(0, k))
    return result
