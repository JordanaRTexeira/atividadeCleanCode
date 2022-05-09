pesquisa = {}
# Lista de Produtos. Fixa - Não precisa ser modificada
listaProdutos    = ['COCACOLA', 'GUARANÁ', 'PEPSI', 'FANTA', 'SPRITE']
listaAvaliadores = ['ANA','MARIA','PEDRO','EDSON']


def existeAlgumAvaliador():
    if listaAvaliadores:
        return True
    input('Nenhum Avaliador Cadastrado. Pressione [Enter] para Retorna.')
    return False

def mostraAvaliadores():
    for ind, avaliador in enumerate(listaAvaliadores):
        print(f" {ind+1} - {avaliador}")

def lerTeclado(mensagem):
    return input(mensagem).upper()

def continuar(mensagem):
    resposta = lerTeclado(mensagem)
    if resposta.upper() == 'N':
        return False
    return True

def cadastrarAvaliador():
    listaAvaliadores.append(lerTeclado("Nome do Avaliador: "))

def listarAvaliadores():
    if existeAlgumAvaliador():
        mostraAvaliadores()

def indiceEscolhidoOk(indice,lista):
    try:
        lista[indice]
        return True
    except:
        input('Indice inexistente. Pressione [Enter] e Escolha novamente.')
        return False

def escolherAvaliador():
    while True:
        print('=-=-=- Escolha um Avaliador pelo indice =-=-=-')
        listarAvaliadores()
        try:
            indiceEscolhido = int(lerTeclado('   Sua escolha:')) - 1
            if indiceEscolhidoOk(indiceEscolhido,listaAvaliadores):
                return listaAvaliadores[indiceEscolhido]
        except:
            input('--- Indice deve ser numérico. Pressione [Enter] para Continuar')

def listarProdutos():
    for ind, produto in enumerate(listaProdutos):
        print(f" {ind+1} - {produto}")

def escolherProduto():
    while True:
        print('=-=-=- Escolha um Produto pelo indice =-=-=-')
        listarProdutos()
        try:
            indiceEscolhido = int(lerTeclado('   Sua escolha:')) - 1
            if indiceEscolhidoOk(indiceEscolhido,listaProdutos):
                return listaProdutos[indiceEscolhido]
            input('--- Deve ser um dos números apresentados. Pressione [Enter] para Continuar')
        except:
            input('--- Indice deve ser numérico. Pressione [Enter] para Continuar')

def digitarNota(produto):
    while True:
        print(f"---- Avaliando o Produto: {produto}")
        print("")
        nota = input('''
        ---- Entre com uma das seguintes notas:
            1-	Péssimo
            2-	Ruim
            3-	Regular
            4-	Bom
            5-	Ótimo 
        --> Sua Nota: ''')
        try:
            if int(nota) in range(1,6):
                return nota
            input("--- Nota deve ser de 1 a 5. Pressione [Enter] para Continuar")
        except:
            input("--- Nota deve ser um númeral. Pressione [Enter] para Continuar")

def inserirAvaliacao(nome,produto,nota):
    try:
        pesquisa[nome]
    except:
        pesquisa[nome] = []
    pesquisa[nome].append(produto)
    pesquisa[nome].append(nota)

def produtoJaAvaliado(nome,produtoEscolhido):
    try:
        if pesquisa[nome] and pesquisa[nome].count(produtoEscolhido) > 0:
            input('---Produto já avaliado. Pressione [Enter] para Continuar.')
            return True
    except: return False

def realizarAvaliacao():
    nomeDoAvaliador = escolherAvaliador()
    produtoEscolhido = escolherProduto()
    if not produtoJaAvaliado(nomeDoAvaliador,produtoEscolhido):
        nota = digitarNota(produtoEscolhido)

        inserirAvaliacao(nomeDoAvaliador,produtoEscolhido,nota)
        print(pesquisa)

def relatorioAvaliadores():
    print("=-=-=- Relatório de Avaliadores =-=-=-")
    print("     Avaliador       Qtde Avaliada")
    for avaliador,avaliacoes in pesquisa.items():
        print(f"    {avaliador.ljust(10)}     {len(avaliacoes)/2}")
    input('Pressione [Enter] para Continuar.')

def notaTotal(produto):
    soma = 0
    for avaliacao in pesquisa.values():
        try:
            ind = avaliacao.index(produto)
            soma += int(avaliacao[ind+1])
        except: pass
    return soma

def relatorioProdutos():
    print("=-=-=- Relatório das notas dos produtos =-=-=-")
    print( "    Produto")
    for produto in listaProdutos:
        nota = notaTotal(produto)
        print(f"    {produto} , {nota}")
    input("Pressione [Enter] para Continuar.")

def menu():
    while True:
        escolha = input ('''
        
         Menu
        |-----------------------------------|
        |0-	Finalizar o Programa            |
        |1-	Cadastrar avaliador             |
        |2-	Realizar avaliação              |
        |3-	Relatório de avaliadores        |
        |4-	Relatório de produtos           |
        |-----------------------------------|
         Escolha: ''')

        if   escolha == '0':  break
        elif escolha == '1':  cadastrarAvaliador()
        elif escolha == '2':  realizarAvaliacao()
        elif escolha == '3':  relatorioAvaliadores()
        elif escolha == '4':  relatorioProdutos()
        else: input("ERRO! escolha um número conforme o menu. Pressione [Enter] para Continuar.")

menu()
