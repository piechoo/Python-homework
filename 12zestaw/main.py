# zadanie 12.1
import random

def randomRepeatingList(n=100, k=10):
    result = []
    for i in range(n):
        result.append(random.randint(0, k-1))
    return result


def findAppearancesInList(items, k=10):
    result = []
    y = random.randint(0, k-1)
    print("Wylosowana liczba to: ",y)
    for i in range(len(items)):
        if items[i] == y:
            result.append(i)
    return result


# zadanie 12.3
def mediana_sort(L, left, right):
    # Dzieki kopiowaniu listy nie naruszamy pierwotnej listy
    result = L[left:right+1]
    result.sort()
    return result[(len(result) // 2)]


array = randomRepeatingList()
appearances = findAppearancesInList(array)
print("Znalezione wystąpienia na indeksach: ", appearances)
medianaList = randomRepeatingList(100, 30)
mediana = mediana_sort(medianaList, 7, 43)
print("Mediana: ", mediana)
