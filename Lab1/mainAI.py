import math


# 1. Ultimul cuvânt alfabetic dintr-un text
def ultimul_cuvant_alfabetic(text):
    """
    Determină ultimul cuvânt din punct de vedere alfabetic dintr-un text.

    Complexitate temporală: O(n log n), unde n este numărul de cuvinte
    Complexitate spațială: O(n), pentru stocarea cuvintelor

    :param text: string - textul de analizat
    :return: string - ultimul cuvânt din punct de vedere alfabetic
    """
    cuvinte = text.split()  # O(n) - n fiind lungimea textului
    cuvinte.sort()  # O(n log n) - n fiind numărul de cuvinte
    return cuvinte[-1]  # O(1)


# 2. Distanța Euclideană între două locații


def distanta_euclidiana(loc1, loc2):
    """
    Calculează distanța Euclideană între două puncte în plan.

    Complexitate temporală: O(1) - operații constante, indiferent de intrare
    Complexitate spațială: O(1) - folosește doar variabile simple

    :param loc1: tuple - coordonatele primului punct (x1, y1)
    :param loc2: tuple - coordonatele celui de-al doilea punct (x2, y2)
    :return: float - distanța Euclideană
    """
    x1, y1 = loc1  # O(1)
    x2, y2 = loc2  # O(1)
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)  # O(1)


# 3. Cuvintele care apar exact o singură dată într-un text
# from collections import Counter


def cuvinte_unice(text):
    """
    Determină cuvintele care apar exact o singură dată într-un text.

    Complexitate temporală: O(n), unde n este numărul de cuvinte din text
    Complexitate spațială: O(m), unde m este numărul de cuvinte unice

    :param text: string - textul de analizat
    :return: list - lista cuvintelor care apar exact o singură dată
    """
    cuvinte = text.split()  # O(n) - n fiind lungimea textului
    count = Counter(cuvinte)  # O(n) - parcurge toate cuvintele o dată
    return [cuvant for cuvant, frecventa in count.items() if frecventa == 1]  # O(m) - m fiind numărul de cuvinte unice


# 4. Identificarea valorii care se repetă într-un șir
def valoare_repetata(sir):
    """
    Identifică valoarea care se repetă de două ori într-un șir.

    Complexitate temporală: O(n²), unde n este dimensiunea șirului
    Complexitate spațială: O(1)

    Notă: Această implementare nu este optimă. Metoda count() are complexitate O(n),
    iar folosirea ei în interiorul altei bucle conduce la complexitate O(n²).

    :param sir: list - șirul de numere
    :return: valoarea care se repetă de două ori
    """
    for numar in sir:  # O(n)
        if sir.count(numar) == 2:  # O(n) pentru fiecare iterație
            return numar


# 5. Determinarea elementului majoritar într-un șir
from collections import Counter


def element_majoritar(sir):
    """
    Determină elementul care apare de mai mult de n/2 ori într-un șir.

    Complexitate temporală: O(n), unde n este dimensiunea șirului
    Complexitate spațială: O(k), unde k este numărul de elemente unice

    :param sir: list - șirul de numere
    :return: elementul majoritar
    """
    count = Counter(sir)  # O(n)
    for numar, frecventa in count.items():  # O(k) - k fiind numărul de elemente unice
        if frecventa > len(sir) // 2:  # O(1)
            return numar


# 6. Al k-lea cel mai mare element dintr-un șir
def al_klea_cel_mai_mare(sir, k):
    """
    Determină al k-lea cel mai mare element dintr-un șir.

    Complexitate temporală: O(n log n) din cauza sortării
    Complexitate spațială: O(1) - nu folosește structuri de date suplimentare

    :param sir: list - șirul de numere
    :param k: int - poziția k (indexare de la 1)
    :return: int - al k-lea cel mai mare element
    """
    sir.sort(reverse=True)  # O(n log n)
    return sir[k - 1]  # O(1)


# 7. Generarea numerelor în reprezentare binară între 1 și n
def numere_binare(n):
    """
    Generează reprezentările binare ale numerelor de la 1 la n.

    Complexitate temporală: O(n log n) - pentru fiecare număr i (1 la n),
    conversia în binar necesită O(log i) operații
    Complexitate spațială: O(n log n) - pentru stocarea tuturor reprezentărilor binare

    :param n: int - limita superioară
    :return: list - reprezentările binare ale numerelor de la 1 la n
    """
    return [bin(i)[2:] for i in range(1, n + 1)]  # O(n) iterații, fiecare cu O(log i) operații
