from math import sqrt

from utils import is_prime, test_is_prime, get_parte_fractionara, is_palindrom, test_get_parte_fractionara, \
    test_is_palindrom


def list_parte_intrega_nr_prim_caractere_invers(lst):
    '''

    :param lst: list of floats
    :return: lista cu nr reale si stringuri
    Float-urile care au partea întreagă a radicalului număr prim
    sunt puse ca string-uri cu caracterele în ordine inversă si restul elemn raman la fel
    '''
    rez = []
    for el in lst:
        if is_prime(int(sqrt(el))):
            rez.append(str(el)[::-1])
        else:
            rez.append(el)
    return rez


def test_list_parte_intrega_nr_prim_caractere_invers():
    assert list_parte_intrega_nr_prim_caractere_invers([10.0, 100.0, 12.45, 50.0, 101.2]) == ['0.01', 100.0, '54.21',
                                                                                              '0.05', 101.2]
    assert list_parte_intrega_nr_prim_caractere_invers([100.0, 101.2]) == [100.0, 101.2]
    assert list_parte_intrega_nr_prim_caractere_invers([]) == []


def list_parte_fract_palindrom(lst):
    '''

    :param lst: list of floats
    :return: lista cu nr reale cu partea fractionara nr palindrom
    '''
    rez = []
    for el in lst:
        part_frac = get_parte_fractionara(el)
        if is_palindrom(part_frac):
            rez.append(el)
    return rez


def test_list_parte_fract_palindrom():
    assert list_parte_fract_palindrom([12.121, 13.01, 1.1]) == [12.121, 1.1]
    assert list_parte_fract_palindrom([12.0, 13.01, 1.1]) == [12.0, 1.1]
    assert list_parte_fract_palindrom([]) == []


def max_div(lst, nr):
    '''
    Det. celui mai mare număr din lst divizibil cu un nr
    :param lst: float list
    :param nr: int
    :return: int (max din lst divizibil cu nr)
    '''
    max = None
    for el in list_int_elems(lst):
        int_el = int(el)
        if int_el % nr == 0:
            if max == None or int_el > max:
                max = int_el
    return max


def test_max_div():
    assert max_div([12.0, 4.0, 17.37, 17.12], 3) == 12
    assert max_div([12.0, 4.0, 17.37, 17.12], 4) == 12
    assert max_div([12.0, 4.0, 17.37, 17.12], 5) == None
    assert max_div([], 4) == None


def list_int_elems(lst):
    '''
    Return list with int elems
    :param lst: list with real numbers
    :return: list with int number as floats
    '''
    rez = []
    for el in lst:
        if el == int(el):
            rez.append(el)
    return rez


def test_list_int_elems():
    assert list_int_elems([12.0, 3, 654.65]) == [12.0, 3]
    assert list_int_elems([12.23, 3.56, 654.65]) == []
    assert list_int_elems([]) == []


def read_list():
    '''
    Read list of floats
    :return: list of floats
    '''
    # list_str = input("Enter list items: ").split(" ")
    # lst = []
    # for el in list_str:
    #     lst.append(float(el))

    lst = [float(e) for e in input("Enter list items: ").split(" ")]
    return lst


def show_menu():
    '''
    Print menu
    :return:
    '''
    print('''
    1. Citeste lista
    2. Afișarea tuturor numerelor întregi din listă 
    3. Afișarea celui mai mare număr divizibil cu un număr citit de la tastatură.
    4. Afișarea tuturor float-urilor ale căror parte fracționară este palindrom.
    5. Afișarea listei obținute din lista inițială în care float-urile cu partea întreagă
     a radicalului număr prim sunt puse ca string-uri cu caracterele în ordine inversă
     6. Afisare lista
    x. Iesire
    ''')


def main():
    lst = []
    while True:
        show_menu()
        cmd = input("Command: ")
        if cmd == '1':
            lst = read_list()
        elif cmd == '2':
            rez = list_int_elems(lst)
            print(rez)
        elif cmd == '3':
            nr = int(input("ENter nr"))
            rez = max_div(lst, nr)
            print(rez)
        elif cmd == '4':
            rez = list_parte_fract_palindrom(lst)
            print(rez)
        elif cmd == '5':
            rez = list_parte_intrega_nr_prim_caractere_invers(lst)
            print(rez)
        elif cmd == '6':
            print(lst)
        elif cmd == 'x':
            break
        else:
            print("Invalid command")

def run_tests():
    test_list_parte_intrega_nr_prim_caractere_invers()
    test_is_prime()
    test_list_parte_fract_palindrom()
    test_get_parte_fractionara()
    test_is_palindrom()
    test_max_div()
    test_list_int_elems()

if __name__ == '__main__':
    run_tests()
    main()

# main()
