import math


def cerinta_1(lista):
    """
    Să se determine ultimul (din punct de vedere alfabetic)
    cuvânt care poate apărea într-un text care conține mai multe cuvinte separate prin ” ” (spațiu).
    Complexitatea globala : O(n log n)
    De ex. ultimul (dpdv alfabetic) cuvânt din ”Ana are mere rosii si galbene” este cuvântul "si".
    :param lista: The input string
    :return:
    """
    cuvinte = lista.split()  # O(n)
    cuvinte.sort()  # O(n log n)
    return cuvinte[-1]  # O(1)


assert cerinta_1("Ana are mere rosii si galbene") == "si"
assert cerinta_1("zebra apple banana") == "zebra"
assert cerinta_1("apple banana apple") == "banana"


def cerinta_2(locatie1, locatie2):
    """
    Să se determine distanța Euclideană între două locații identificate prin perechi de numere.
    De ex. distanța între (1,5) și (4,1) este 5.0
    Complexitate timp: O(d)
    :param locatie1: The first location
    :param locatie2: The second location
    :return:
    """
    distanta = 0.0
    for i in range(len(locatie1)):  # O(d) - dimensiunea vectorilor
        distanta += (locatie2[i] - locatie1[i]) ** 2
    return math.sqrt(distanta)  # O(1)


assert cerinta_2([1, 5], [4, 1]) == 5.0
assert cerinta_2([0, 0], [3, 4]) == 5.0
assert cerinta_2([1, 2, 3], [4, 5, 6]) == math.sqrt(27)


def cerinta_4(sir):
    """
   Să se determine cuvintele unui text care apar exact o singură dată în acel text.
    De ex. cuvintele care apar o singură dată în ”ana are ana are mere rosii ana" sunt: 'mere' și 'rosii'.
    Complexitate timp: O(n)
    :param sir: The input string
    :return:
    """
    cuvinte = sir.split()  # O(n) - n lungimea sirului
    frec = {
    }
    for cuvant in cuvinte:  # O(n) - n nr de cuvinte
        if cuvant in frec:  # O(1)
            frec[cuvant] += 1
        else:
            frec[cuvant] = 1

    cuvant_unic = []
    for cuvant, count in frec.items():  # O(n) - n nr de cuvinte unice
        if count == 1:
            cuvant_unic.append(cuvant)  # O(1)

    return cuvant_unic


assert cerinta_4("ana are ana are mere rosii") == ["mere", "rosii"]
assert cerinta_4("this is a test this is only a test") == ["only"]
assert cerinta_4("unique words only") == ["unique", "words", "only"]


def cerinta_5(sir):
    """
    Pentru un șir cu n elemente care conține valori din mulțimea {1, 2, ..., n - 1} astfel încât o singură valoare
    se repetă de două ori, să se identifice acea valoare care se repetă.
    De ex. în șirul [1,2,3,4,2] valoarea 2 apare de două ori.
    :param sir: List of numbers
    :return:
    """
    elems = sir
    frec = {}
    for elem in elems:
        if elem in frec:
            frec[elem] += 1
        else:
            frec[elem] = 1

    elems_uniq = []
    for elem, count in frec.items():
        if count == 2:
            elems_uniq.append(elem)

    return elems_uniq


assert cerinta_5([1, 2, 3, 4, 2]) == [2]
assert cerinta_5([1, 1, 3, 4, 2]) == [1]
assert cerinta_5([5, 5, 5, 5, 5]) == []


def cerinta6(sir):
    """
    Pentru un șir cu n numere întregi care conține și duplicate, să se determine elementul majoritar
    (care apare de mai mult de n / 2 ori).
    De ex. 2 este elementul majoritar în șirul [2,8,7,2,2,5,2,3,1,2,2].
    :param sir: List of numbers
    :return:
    """
    numbers = len(sir)
    frec = {}

    for number in sir:
        if number in frec:
            frec[number] += 1
        else:
            frec[number] = 1

    max_frec = []
    for number, count in frec.items():
        if count > (numbers / 2):
            max_frec.append(number)

    return max_frec


assert cerinta6([2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2]) == [2]
assert cerinta6([3, 3, 4, 2, 4, 4, 2, 4, 4]) == [4]
assert cerinta6([1, 1, 1, 1, 2, 2, 2]) == [1]


def cerinta_7(lista, a):
    """
    Să se determine al k-lea cel mai mare element al unui șir de numere cu n elemente (k < n).
    De ex. al 2-lea cel mai mare element din șirul [7,4,6,3,9,1] este 7.

    :param lista: List of numbers
    :param a: The k-th position (1-based index)
    :return: The k-th largest element
    """
    lista.sort(reverse=True)  # O(n log n)
    return lista[a - 1]  # O(1)


assert cerinta_7([7, 4, 6, 3, 9, 1], 2) == 7
assert cerinta_7([1, 2, 3, 4, 5], 1) == 5
assert cerinta_7([10, 20, 30, 40, 50], 3) == 30


def cerinta_8(n):
    """
    Să se genereze toate numerele (în reprezentare binară) cuprinse între 1 și n.
    De ex. dacă n = 4, numerele sunt: 1, 10, 11, 100.
    Complexitate timp: O(n log n)
    :param n: The upper limit
    :return:
    """

    m = []
    for i in range(1, n + 1):  # O(n)
        binary = bin(i)[2:]  # O(log i)
        m.append(binary)  # O(1)

    return m


assert cerinta_8(4) == ["1", "10", "11", "100"]
assert cerinta_8(2) == ["1", "10"]
assert cerinta_8(5) == ["1", "10", "11", "100", "101"]
