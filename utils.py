from math import sqrt


def is_prime(nr):
    '''
    Verify if a number nr is prime
    :param nr: int
    :return: True if is prime, False otherwise
    '''
    if nr < 2:
        return False
    if nr != 2 and nr % 2 == 0:
        return False
    for d in range(3, int(sqrt(nr)) + 1, 2):
        if nr % d == 0:
            return False
    return True


def test_is_prime():
    assert is_prime(244) == False
    assert is_prime(-5) == False
    assert is_prime(4) == False
    assert is_prime(2) == True
    assert is_prime(37) == True

def get_parte_fractionara(nr):
    '''
    Returneaza parte fractionara a numarului nr ca string
    :param nr: float
    :return: part_frac as string
    '''
    float_nr = float(nr)
    str_float_nr = str(float_nr)
    poz = str_float_nr.find('.')
    return str_float_nr[poz + 1:len(str_float_nr)]


def test_get_parte_fractionara():
    assert get_parte_fractionara(12.435) == '435'
    assert get_parte_fractionara(12.0) == '0'
    assert get_parte_fractionara(12.035) == '035'
    assert get_parte_fractionara(12) == '0'


def is_palindrom(str_nr):
    '''
    Verifica daca nr_str e palindrom
    :param nr: string
    :return: True if is palindrom, False otherwise
    '''
    str_invers_nr = str_nr[::-1]
    return str_invers_nr == str_nr


def test_is_palindrom():
    assert is_palindrom('121') == True
    assert is_palindrom('1') == True
    assert is_palindrom('12') == False