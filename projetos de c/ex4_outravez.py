'''Criar um programa em Python para gerenciar um catálogo de até 100 livros. O programa deve permitir que o usuário realize as seguintes operações: 
Cadastrar livros: 
O programa deve permitir que o usuário adicione novos livros ao catálogo, informando o título, o autor e o ano de publicação. 
Procurar por livros: 
O usuário deve poder procurar por título ou autor. O programa deve exibir as posições onde o livro foi encontrado e mostrar o conteúdo correspondente. 
Excluir livros: 
O usuário deve poder excluir um livro a partir da sua posição no catálogo. A posição será dada pelo índice do livro na lista. 
Ordenar livros: 
O programa deve permitir que o usuário ordene os livros cadastrados por título ou autor. 
Listar todos os livros cadastrados: 
O programa deve listar todos os livros cadastrados, exibindo as informações de cada um (título, autor, ano). 
Sair do programa: 
O programa deve continuar em execução até que o usuário escolha explicitamente a opção de sair. 
 
Menu do Programa: 
O programa deve apresentar um menu com as seguintes opções: 
Adicionar novo livro 
Procurar por título ou autor 
Excluir livro 
Ordenar livros 
Listar livros 
Sair do Programa 
 
Requisitos: 
O programa deve permitir a execução contínua das operações, retornando sempre ao menu principal após cada ação. 
As operações de busca, exclusão e ordenação devem ser realizadas com base nas listas de títulos e autores. 
O programa deve garantir que não sejam cadastrados mais de 100 livros. 
Adicionar a possibilidade de verificar se o livro já está cadastrado antes de permitir o cadastro. 
 
8 pontos do teste estão destinados a: 
 - (2) Criar Algoritmos de procura e de validação. 
 - (2) Funções e reutilização das mesmas. 
 - (1) Utilização de boas praticas e standards. 
 - (1) Uso de Exceções. '''

livros = []

indicelivr = 0

opcao = 0

def adicionar_livro():
    while True:
        try:
            global indicelivr
            nome = input("insere o nome do livro: ")
            autor = input("insere o nome do autor do livro: ")
            data = int(input("insere a data em que o livro foi publicado: "))
        except ValueError:
            print("input inserido de formato inválido")

        livro = {
            "nome" : nome,
            "autor" : autor,
            "data" : data,
            "indicelivr" : indicelivr
        }

        

        livros.append(livro)
        indicelivr +=1

        ola = input("pretende voltar ao menu inicial? (s/n): ")
        if ola == 's':
            return
        elif ola != 'n':
            continue 

def procurar():
    while True:
        if not livros:
            print("não ha livros ainda na lista my people")
        search = input("insere o nome do livro ou autor que queres procurar: ")

        for livro in livros:
            if livro['nome'] == search:
                print(f"\n\nnome: {livro['nome']}")
                print(f"autor: {livro['autor']}")
                print(f"ano: {livro['data']}")
                
            elif livro['autor'] == search:
                print(f"\n\nnome: {livro['nome']}")
                print(f"autor: {livro['autor']}")
                print(f"ano: {livro['data']}")

                ola = input("pretende voltar ao menu inicial? (s/n): ")
                if ola == 's' or 'S':
                    return
                elif ola == 'n' or 'N':
                    continue
            
def listar():
    while True:
        for livro in livros:
                print(f"\n\nindice: {livro['indicelivr']}")
                print(f"nome: {livro['nome']}")
                print(f"autor: {livro['autor']}")
                print(f"ano: {livro['data']}")

        ola = input("pretende voltar ao menu inicial? (s/n): ")
        if ola == 's' or 'S':
            return
        elif ola == 'n' or 'N':
            continue



def menu():
    while True:
        print("1 - Adicionar novo livro")
        print("2 - Procurar livro ou autor")
        print("3 - Excluir livro")
        print("4 - Ordenar livros")
        print("5 - Listar livros")
        print("6 - Sair do programa")

        opcao = input("Insere a função que queres efetuar: ")

        match opcao:
            case '1':
                adicionar_livro()
            case '2':
                procurar()
            case '3':
                pass
            case '4':
                pass
            case '5':
                listar()
            case '6':
                pass



menu()