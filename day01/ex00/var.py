def my_var ():
    inteiro = 42
    string = "42"
    string_2 = "quarante-deux"
    double = 42.0
    boolean = True
    lista = [42]
    array = {42: 42}
    items = (42,)
    lista_2 = set()

    print(str(inteiro) + " has a type " + str(type(inteiro)))
    print(str(string) + " has a type " + str(type(string)))
    print(str(string_2) + " has a type " + str(type(string_2)))
    print(str(double) + " has a type " + str(type(double)))
    print(str(boolean) + " has a type " + str(type(boolean)))
    print(str(lista) + " has a type " + str(type(lista)))
    print(str(array) + " has a type " + str(type(array)))
    print(str(items) + " has a type " + str(type(items)))
    print(str(lista_2) + " has a type " + str(type(lista_2)))

if __name__ == '__main__':
    my_var()