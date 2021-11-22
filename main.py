
class Simbolo_NT:

    def __init__(self, _nome : str):
        self.nome = _nome
        self.regras = []

class Gramatica:

    def __init__(self, _simbolos : dict):
        self.simbolos = _simbolos

def formata_input(inputf) -> dict:

    lista = [x.rstrip() for x in inputf]
    g_dict = {}
    for s in lista:
        print(s)


if __name__ == "__main__":

    with open("input.txt") as file:
        file_input = file.readlines()
        formata_input(file_input)
