"""
ZADANIE 3.1
Czy podany kod jest poprawny składniowo w Pythonie?

x = 2 ; y = 3 ;
if (x > y):
    result = x; #poprawny ale niepotrzebna instrukcja warunkowa ( z góry wiadomy przebieg), niepotrzebne średniki
else:
    result = y;
for i in "qwerty": if ord(i) < 100: print(i) # instrukcja warunkowa powinna być w kolejnej linii

for i in "axby": print(ord(i) if ord(i) < 100 else i) #kod poprawny składniowo
"""
"""
ZADANIE 3.2
Co jest złego w kodzie:
L = [3, 5, 4] ; L = L.sort() #fcja sort nie zwraca wyniku, dziala na przekazanej liscie
x, y = 1, 2, 3 # Dla dwóch zmiennych przekazywane trzy wartości
X = 1, 2, 3 ; X[1] = 4 # x nie jest listą
X = [1, 2, 3] ; X[3] = 4 #Listy nie można rozszerzać w ten sposób
X = "abc" ; X.append("d") # String traktowany jako lista
map(pow, range(8)) # Zła liczba argumentów do funkcji pow() - potrebuje dwóch
"""
"""
ZADANIE 3.3
Wypisać w pętli liczby od 0 do 30 z wyjątkiem liczb podzielnych przez 3.
"""
print("---Zadanie 3.3---")
nums = []
for i in range(31):
    if i % 3:
        nums.append(i)
print(nums)
"""
ZADANIE 3.4
Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x i wypisujący parę x i trzecią potęgę x.
 Zatrzymanie programu następuje po wpisaniu z klawiatury stop.
  Jeżeli użytkownik wpisze napis zamiast liczby, to program ma wypisać komunikat o błędzie i kontynuować pracę.
"""
print("---Zadanie 3.4---")
while True:
    try:
        z = input("Podaj liczbę rzeczywistą: ")
        x = float(z)
        print("%f %f" % (x, pow(x, 3)))
        break
    except ValueError:
        if z == "stop":
            break
        print("Podano bledny argument. Sprobuj ponownie...")


"""
ZADANIE 3.5
Napisać program rysujący "miarkę" o zadanej długości. Należy prawidłowo obsłużyć liczby składające się z kilku cyfr.
 Należy zbudować pełny string, a potem go wypisać.

|....|....|....|....|....|....|....|....|....|....|....|....|
0    1    2    3    4    5    6    7    8    9   10   11   12
"""
# %[(nazwa)][opcje][szerokość][.precyzja]kod_typu
#print("int %d float %f str %s" % (5, 3.14159, "napis"))
#print("%-10s %-10s" % ("napis1", "napis2"))

print("---Zadanie 3.5---")
length = 23 #dlugosc miarki
pattern = "|...."
linear = ['', '0']
linijka = ''
for i in range(length):
    linear[0] += pattern
    linear[1] += "%5s" % (i + 1)
linear[0] += "|"
linijka = linear[0] + '\n' + linear[1]
print(linijka)
"""
ZADANIE 3.6
Napisać program rysujący prostokąt zbudowany z małych kratek. Należy zbudować pełny string, a potem go wypisać.
 Przykładowy prostokąt składający się 2x4 pól ma postać:
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
"""
print("---Zadanie 3.6---")
row = "+---"
column = "|   "
SIZE = [12, 3] #dlugosc wiersza x dlugosc kolumny
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
print(board)
"""
ZADANIE 3.8
Dla dwóch sekwencji znaleźć: (a) listę elementów występujących w obu sekwencjach (bez powtórzeń),
(b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).
"""
print("---Zadanie 3.8---")
b = [(0, 5, 1, 9), (3, 4), (5, 67, 7)]
a = [[4, 5, 9], (13, 2), [3, 4], (5, 6, 7)]
new_a = set()
new_b = set()

for el in a:
    new_a.update(set(el))


for el in b:
    new_b.update(set(el))


print(new_a.intersection(new_b))
print(new_a.union(new_b))

"""
ZADANIE 3.9
Mamy daną listę sekwencji (listy lub krotki) różnej długości zawierających liczby.
Znaleźć listę zawierającą sumy liczb z tych sekwencji.
Przykładowa sekwencja [[],[4],(1,2),[3,4],(5,6,7)], spodziewany wynik [0,4,3,7,18].
"""
print("---Zadanie 3.9---")
elements = [[], [4, 5, 9], (13, 2), [3, 4], (5, 6, 7)]
print(list(map(lambda x: sum(x), elements)))
"""
ZADANIE 3.10
Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim (z literami I, V, X, L, C, D, M) na liczby arabskie
(podać kilka sposobów tworzenia takiego słownika). Mile widziany kod tłumaczący całą liczbę [funkcja roman2int()].
"""
print("---Zadanie 3.10---")


def roman2int(rzymska):
    res = 0
    slownik = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i in range(len(rzymska)):
        if i > 0 and slownik[rzymska[i]] > slownik[rzymska[i - 1]]:
            res += slownik[rzymska[i]] - 2 * slownik[rzymska[i - 1]]
        else:
            res += slownik[rzymska[i]]
    return res


print(roman2int("MCMXXIV"))
