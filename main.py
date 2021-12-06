class Simbolo_NT:

    def __init__(self, _nome : str):
        self.nome = _nome
        self.regras = []

class Gramatica:

    def __init__(self, _simbolos : dict):
        self.regras = _simbolos
        self.simbolos_geradores = [x for x in _simbolos]
    
    def imprime(self):
        for s in self.simbolos_geradores:
            print(f"{s} : {self.regras[s]}")
        # print(self.regras)

def formata_input(inputf) -> dict:

    # remove espaços em branco
    lista_regras = [x.rstrip() for x in inputf]
    g_dict = {}

    # formata e armazena na estrutura da gramática
    for regra in lista_regras:

        # separa os símbolos geradores das regras e formata
        s_split = regra.rsplit("=>", maxsplit=1)
        regras_split = s_split[1].rsplit("|")
        regras_split = [x.replace(" ","") for x in regras_split]
        sym_split = s_split[0].replace(" ","")

        if sym_split in g_dict:
            [g_dict[sym_split].append(x) for x in regras_split]
        else:
            g_dict[sym_split] = regras_split


    return(g_dict)


def cyk(gramatica : Gramatica, palavra : str):

    linha_1 = []

    # primeira etapa, símbolos terminais

    for simbolo in palavra:
        
        # lista dos terminais que podem gerar o simbolo
        sim_list = list()
        
        for r in gramatica.regras:
            if simbolo in gramatica.regras[r]:
                sim_list.append(r)

        # adiciona a lista de terminais que geram o simbolo na linha 1 da tabela 
        linha_1.append(sim_list)

    print(linha_1)

    # segunda etapa, redução dos terminais

    tabela = [linha_1]

    # percorre a tabela
    for i in range(len(palavra)-1):
        
        # pega a ultima linha modificada da tabela para o próximo passo
        ultima_linha = tabela[-1]
        nova_linha = list()

        # percorre a linha
        for n in range(len(ultima_linha)-1):

            sim_list = list()
            _regras = combina(ultima_linha[n], ultima_linha[n+1])
            for _r in _regras:
                for r in gramatica.regras:
                    if _r in gramatica.regras[r]:
                        sim_list.append(r)

            if sim_list == []:
                sim_list.append(ultima_linha[n])

            nova_linha.append(sim_list)

        tabela.append(nova_linha)
    
    print(tabela)


def combina(l1 :list , l2:list):
    r = list()
    for i in l1:
        for j in l2:
            r.append(i+j)
    return r

if __name__ == "__main__":

    with open("input.txt") as file:
        file_input = file.readlines()
        gram = Gramatica(formata_input(file_input))
        gram.imprime()
        cyk(gram,'bacc')