"""
ZADANIE 4.2
Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać w postaci funkcji,
które zwracają pełny string przez return.
"""


print("---Zadanie 4.2---")


#3.5
def make_linijka(length):
    pattern = "|...."
    linear = ['', '0']
    linijka = ''
    for i in range(length):
        linear[0] += pattern
        linear[1] += "%5s" % (i + 1)
    linear[0] += "|"
    linijka = linear[0] + '\n' + linear[1]
    return linijka


print(make_linijka(12))
#3.6
def make_siatka(x,y):
    row = "+---"
    column = "|   "
    SIZE = [x, y] #dlugosc wiersza x dlugosc kolumny y
    board = ''

    def generate_el(pattern, end_cap):
        result = ''
        for j in range(SIZE[0]):
            result += pattern
            if j == SIZE[0] - 1:
                result += end_cap + '\n'
        return result
    for _ in range(SIZE[1]):
        board += generate_el(row, '+')
        board += generate_el(column, '|')
    board += generate_el(row, '+')
    return board


print(make_siatka(3,4))
"""
ZADANIE 4.3
Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.
"""
print("---Zadanie 4.3---")


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


assert factorial(5) == 120
"""
ZADANIE 4.4
Napisać iteracyjną wersję funkcji fibonacci(n) 
obliczającej n-ty wyraz ciągu Fibonacciego.
"""
print("---Zadanie 4.4---")


def fibonacci(n):
    a, b = 1, 1
    for i in range(0, n-1):
        a, b = b, a + b
    return a


assert fibonacci(8) == 21


"""
ZADANIE 4.5
Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów 
na liście od numeru left do right włącznie. 
Lista jest modyfikowana w miejscu (in place). Rozważyć wersję iteracyjną i rekurencyjną.
"""
print("---Zadanie 4.5---")


def iter_odwracanie(L, left, right):
    assert left in range(len(L)) and right in range(len(L))
    if right < left:
        left, right = right, left
    if  ((right - left) % 2) != 0:
        zakres = (right - left + 1) // 2
    else:
        zakres = (right - left) // 2
    for i in range(zakres):
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1


def rek_odwracanie(L, left, right):
    L[left], L[right] = L[right], L[left]
    left, right = left + 1, right - 1
    if left < right:
        return rek_odwracanie(L, left, right)
    else:
        return True


L = [1, 2, 3, 4, 5, 6, 7, 8]
left = 1
right = 7
print(L)
iter_odwracanie(L, left, right)
print(L)
rek_odwracanie(L, left, right)
print(L)

"""
ZADANIE 4.6
Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji, 
która może zawierać zagnieżdżone podsekwencje. 
Wskazówka: rozważyć wersję rekurencyjną, 
a sprawdzanie, czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).
"""
print("---Zadanie 4.6---")
sequence = [(1, 2), 3, (4, [5, 6], (7, 8, (9, 10, 11)))]


def sum_seq(sequence):
    sum = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            sum += sum_seq(item)
        else:
            sum += item
    return sum


assert sum_seq(sequence) == 66

"""
ZADANIE 4.7
Mamy daną sekwencję, w której niektóre z elementów mogą okazać się podsekwencjami, 
a takie zagnieżdżenia mogą się nakładać do nieograniczonej głębokości. 
Napisać funkcję flatten(sequence), która zwróci spłaszczoną listę wszystkich elementów sekwencji. 
Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie czy element jest sekwencją, 
wykonać przez isinstance(item, (list, tuple)).
seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print flatten(seq)            # [1,2,3,4,5,6,7,8,9]
"""
print("---Zadanie 4.7---")


def flatten(sequence):
    L = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            L.extend(flatten(item))
        else:
            L.append(item)
    return L

sequence = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print(flatten(sequence))
