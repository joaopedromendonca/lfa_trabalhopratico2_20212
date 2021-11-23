
from os import spawnl


class Simbolo_NT:

    def __init__(self, _nome : str):
        self.nome = _nome
        self.regras = []

class Gramatica:

    def __init__(self, _simbolos : dict):
        self.simbolos = _simbolos

    def imprime(self):

        for s in self.simbolos:
            print(f"{s} : {self.simbolos[s]}")

def formata_input(inputf) -> dict:

    lista = [x.rstrip() for x in inputf]
    g_dict = {}
    simbolos = set()
    for s in lista:
        s_split = s.rsplit("=>", maxsplit=1)
        regras_split = s_split[1].rsplit("|")
        new_rsplit = [x.replace(" ","") for x in regras_split]
        sym_split = s_split[0].replace(" ","")
        simbolos.add(sym_split)
        if sym_split in g_dict:
            [g_dict[sym_split].append(x) for x in new_rsplit]
        else:
            g_dict[sym_split] = new_rsplit
        # print(f"{sym_split} : {new_rsplit}")
    return(g_dict)


if __name__ == "__main__":

    with open("input.txt") as file:
        file_input = file.readlines()
        gram = Gramatica(formata_input(file_input))
        gram.imprime()