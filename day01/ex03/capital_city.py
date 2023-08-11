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

def exibir_capital_cidade(estado):
    estado_selecionado = states.get(estado)
    if estado_selecionado:
        capital_cidade = capital_cities.get(estado_selecionado)
        if capital_cidade:
            print(capital_cidade)
        else:
            print("Unknown capital")
    else:
        print("Unknown state")

if __name__ == "__main__":
    import sys

    if valida_numero_argumentos():
        exit
    else:
        exibir_capital_cidade(sys.argv[1])