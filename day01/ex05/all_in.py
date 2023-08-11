states = {
    "Oregon": "OR",
    "Alabama": "AL",
    "New Jersey": "NJ",
    "Colorado": "CO"
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

def encontra_paramentro_na_lista(arg):
    inverte_estados = {v: k for k, v in states.items()}
    inverte_capital = {v: k for k, v in capital_cities.items()}

    for i in arg:
        i = i.strip()
        arg_formatado = i.title()

        if arg_formatado in states:
            capital = capital_cities[states[arg_formatado]]
            print(f"{capital} is the capital of {arg_formatado}")
        elif arg_formatado in inverte_capital:
            estado = inverte_estados[inverte_capital[arg_formatado]]
            print(f"{arg_formatado} is the capital of {estado}")
        elif arg_formatado == "":
            pass
        else:
           print(f"{i} is neither a capital city nor a state") 
        
if __name__ == "__main__":
    import sys

    if valida_numero_argumentos():
        exit()
    else:
        argumentos = sys.argv[1].split(",")
        encontra_paramentro_na_lista(argumentos)