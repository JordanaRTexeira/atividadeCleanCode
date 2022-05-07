lst_avaliacoes = []
lst_avaliadores = []
lista_de_produtos = [
    "COCACOLA",
    "GUARANA",
    "PEPSI",
    "FANTA",
    "SPRITE"
]

class Avaliador:
    def __init__(self,name):
        self.nome = name

    def get_nome(self):
        return self.nome

    def imprime_atributos(self):
        return self.nome

    def __str__(self):
        return self.nome

class Avaliacao:
    def __init__(self,avaliador,produto,nota):
        self.avaliador = avaliador
        self.avaliacao = {produto:nota}

    def nota_do_produto(self,refrigerante):
        if refrigerante in self.avaliacao:
            return self.avaliacao[refrigerante]
        return 0

    def qt_produtos_avaliados(self):
        return str(len(self.avaliacao))

    def refrigerante_avaliado(self,refrigerante):
        if refrigerante in self.avaliacao:
            return True
        return False

    def refrigerante_ja_avaliado(self,refrigerante):
        try:
            if self.avaliacao[refrigerante]:
                return True
        except:
            pass
        return False

    def nome_avaliador(self):
        return self.avaliador.get_nome()

    def nova_avaliacao(self,produto,nota):
        self.avaliacao[produto] = nota

    def __str__(self):
        return str(self.avaliador)+str(self.avaliacao)

def adiciona_avaliacao(avaliacao):
    lst_avaliacoes.append(avaliacao)

def refrigerante_avaliado(avaliador,refrigerante):
    for avalia in lst_avaliacoes:
        if avalia.nome_avaliador() == avaliador.get_nome():
            if avalia.refrigerante_ja_avaliado(refrigerante):
                return True
    return False

def procura_avaliacao_existente(avaliador):
    for aval in lst_avaliacoes:
        if aval.nome_avaliador() == avaliador.get_nome():
            return False
    return True

def busca_avaliacao(avaliador):
    for aval in lst_avaliacoes:
        if aval.nome_avaliador() == avaliador.get_nome():
            return aval

def relatorio_avaliadores():
    print("=-=-=- Relatório de Avaliadores =-=-=-")
    print("     Avaliador       Qtde Avaliada")
    for avaliacao in lst_avaliacoes:
        print(f"    {str(avaliacao.nome_avaliador()).ljust(15,'.')}     {avaliacao.qt_produtos_avaliados()}")#str(len(avaliacao))}")
    input('[Enter] Continua. ')

def relatorio_produtos():
    print("=-=-=- Relatório das notas dos produtos =-=-=-")
    print( "    Produto")
    for produto in lista_de_produtos:
        nota = 0
        for avaliacao in lst_avaliacoes:
            nota += avaliacao.nota_do_produto(produto)
        if nota > 0:
            print(f"    {produto} , {nota}")
    input("[Enter] Continua.")

def adiciona_avaliador(avaliador):
    lst_avaliadores.append(avaliador)

def avaliadores_cadastrados():
    for ind, avaliador in enumerate(lst_avaliadores):
        print(f" {ind+1}- {avaliador.get_nome()}")

def ler_indice_avaliador():
    try:
        indice = int(input("...Escolha pelo indice: ")) - 1
        return lst_avaliadores[indice]
    except: pass
    input("---Indice incorreto. [Enter]")
    return ler_indice_avaliador()

def refrigerantes_cadastrados():
    for ind,refrigerante in enumerate(lista_de_produtos):
        print(f"{ind+1}- {refrigerante}")

def ler_indice_refrigerante():
    try:
        indice = int(input("...Escolha pelo indice: ")) - 1
        return lista_de_produtos[indice]
    except: pass
    input("---Indice inexistente. [Enter]")
    return ler_indice_refrigerante()


def escolhe_avaliador():
    avaliadores_cadastrados()
    avaliador_escolhido = ler_indice_avaliador()
    return avaliador_escolhido


def escolhe_refrigerante():
    refrigerantes_cadastrados()
    refrigerante_escolhido = ler_indice_refrigerante()
    return refrigerante_escolhido

def cadastrar_avaliador():
    adiciona_avaliador(Avaliador(input("Nome do Avaliador: ")))

def ler_nota():
    try:
        nota = int(input("Nota: "))
        if nota in [1, 2, 3, 4, 5]:
            return nota
    except:
        pass
    input("---Nota incorreta. [Enter] ")
    return ler_nota()

def realizar_avaliacao():
    avaliador = escolhe_avaliador()
    refrigerante = escolhe_refrigerante()

    if procura_avaliacao_existente(avaliador):
        print("primeira avaliacao")
        lst_avaliacoes.append(Avaliacao(avaliador, refrigerante, ler_nota()))
    else:
        if refrigerante_avaliado(avaliador, refrigerante):
            input("Refrigerante já avaliado. [Enter]")
        else:
            avaliacao_existente = busca_avaliacao(avaliador)
            avaliacao_existente.nova_avaliacao(refrigerante, ler_nota())
            print("nova avaliação ok.")


cadastrar_avaliador()
realizar_avaliacao()
relatorio_avaliadores()
relatorio_produtos()
