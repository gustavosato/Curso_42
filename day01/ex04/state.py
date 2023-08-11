states = {
    "Oregon": "OR",
    "Alabama": "AL",
    "New Jersey": "NJ",
    "Colorado": "CO",
    "Bufalo": "BU"
}

capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
}

def valida_numero_argumentos():
    if len(sys.argv) > 2 or len(sys.argv) == 1:
        return True
    else:
        return False

def exibir_cidade_capital(capitais_cidade):
    for estado, abreviacao in states.items():
        if capital_cities.get(abreviacao) == capitais_cidade:
            return print(estado)
        
    print("Unknown capital city")

if __name__ == "__main__":
    import sys

    if valida_numero_argumentos():
        exit
    else:
        exibir_cidade_capital(sys.argv[1])