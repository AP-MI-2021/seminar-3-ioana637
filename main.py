def read_list():
    '''
    Read list of floats
    :return: list of floats
    '''
    list_str = input("Enter list items: ").split(" ")
    lst = []
    for el in list_str:
        lst.append(float(el))

    # lst = [float(e) for e in input("Enter list items: ").split(" ")]
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
            pass
        elif cmd == '3':
            pass
        elif cmd == '4':
            pass
        elif cmd == '5':
            pass
        elif cmd == '6':
            print(lst)
        elif cmd == 'x':
            break
        else:
            print("Invalid command")

if __name__ == '__main__':
    main()

# main()

