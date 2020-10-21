
"""
ZADANIE 2.10
Mamy dany napis wielowierszowy line. Podać sposób obliczenia liczby wyrazów w napisie.
Przez wyraz rozumiemy ciąg "czarnych" znaków,
oddzielony od innych wyrazów białymi znakami (spacja, tabulacja, newline).
"""

print("---Zad 2.10---")
line = """jeden dwa trzy
cztery piec 	szesc 		siedem

osiem
dziewiec GvR"""
word_num = len(line.split())
print("Number of words in line file: ", word_num)

"""
ZADANIE 2.11
Podać sposób wyświetlania napisu word tak, aby jego znaki były rozdzielone znakiem podkreślenia.
"""
print("---Zad 2.11---")
word = "slowobezpodkreslnikow"
new_word = ""
for char in word:
    if len(new_word) == 2*len(word)-2:
        new_word += char
        break
    new_word += char + "_"
print(new_word)

"""
ZADANIE 2.12
Zbudować napis stworzony z pierwszych znaków wyrazów z wiersza line. 
Zbudować napis stworzony z ostatnich znaków wyrazów z wiersza line.
"""

print("---Zad 2.12---")


def get_words_from_sights_starting_with(from_which_digit):
    word_from_single_line = ''
    for single_line in line.splitlines():
        for single_word in single_line.split():
            word_from_single_line += single_word[from_which_digit]
        print(word_from_single_line)
        word_from_single_line = ''


get_words_from_sights_starting_with(0)
print("\n")
get_words_from_sights_starting_with(-1)

"""
ZADANIE 2.13
Znaleźć łączną długość wyrazów w napisie line. Wskazówka: można skorzystać z funkcji sum().
"""
print("---Zad 2.13---")
words = line.split()
all_words = "".join(words)
char_num = len(all_words)
print("Number of chars in line file: ", char_num)

"""
ZADANIE 2.14
Znaleźć: (a) najdłuższy wyraz, (b) długość najdłuższego wyrazu w napisie line.
"""
print("---Zad 2.14---")
the_longest_word_in_file = ''
for single_line in line.splitlines():
    for single_word in single_line.split():
        if len(single_word) > len(the_longest_word_in_file):
            the_longest_word_in_file = single_word

print("the longest word in file is:", the_longest_word_in_file)
print("Length = ", len(the_longest_word_in_file))

"""
ZADANIE 2.15
Na liście L znajdują się liczby całkowite dodatnie. 
Stworzyć napis będący ciągiem cyfr kolejnych liczb z listy L.
"""
print("---Zad 2.15---")
L = [203, 12, 7, 442, 23, 683, 25, 50, 8436, 1, 44, 73, 2, 43, 25, 6, 199, 2, 47, 381]
word_from_list = "".join(str(x) for x in L)
print(word_from_list)

"""
ZADANIE 2.16
W tekście znajdującym się w zmiennej line zamienić ciąg znaków "GvR" na "Guido van Rossum".
"""
print("---Zad 2.16---")
line2 = "George V (GvR) was King of the United Kingdom and the British Dominions,GvR and Emperor of India, from 6 May 1910 until GvR death in 1936."
line2 = line2.replace("GvR", "Guido van Rossum")
print(line2)

"""
ZADANIE 2.17
Posortować wyrazy z napisu line raz alfabetycznie, a raz pod względem długości. 
Wskazówka: funkcja wbudowana sorted().
"""
print("---Zad 2.17---")
words_list = []
with open("line.txt", 'r') as file:
    for single_line in file:
        for single_word in single_line.split():
            words_list.append(single_word)
print(len(words_list))
words_list.sort(key=str.casefold)
print("sorted_list: ", words_list)
words_list.sort(key=len)
print("sorted list when key is length: ", words_list)

"""
ZADANIE 2.18
Znaleźć liczbę cyfr zero w dużej liczbie całkowitej. Wskazówka: zamienić liczbę na napis.
"""
print("---Zad 2.18---")
L = [203, 12, 7, 442, 23, 683, 25, 50, 8436, 1, 44, 73, 2, 43, 25, 6, 199, 2, 47, 381]
big_number = "".join(str(x) for x in L)
print("Number of zeros in the number: ", big_number.count('0'))

"""
ZADANIE 2.19
Na liście L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie. 
Chcemy zbudować napis z trzycyfrowych bloków, gdzie liczby jedno- 
i dwucyfrowe będą miały blok dopełniony zerami, np. 007, 024. Wskazówka: str.zfill().
"""
print("---Zad 2.19---")
L = [203, 12, 7, 442, 23, 683, 25, 50, 8436, 1, 44, 73, 2, 43, 25, 6, 199, 2, 47, 381]
big_number = ", ".join(str(x).zfill(3) for x in L)
print(big_number)
