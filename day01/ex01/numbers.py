def ler_arquivo():
    with open ("numbers.txt", "r") as arquivo:
        numeros = arquivo.readline()
        result = numeros.split(",")
        for i in result:
            print(i)
    arquivo.close()

if __name__ == '__main__':
    ler_arquivo()
