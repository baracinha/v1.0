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

import json

livros = []

livro = 0

numlivr = 0

def adicionar_livro():
    while True:
        
        global numlivr
        autor = input("insere o autor do livro: ")
        title = input("insere o nome do livro: ")
        data = int(input("insere a data de punlicacao: "))

        if data(ValueError):
            print("bisa")

        livro = {
            "numlivr" : numlivr,
            "title" : title,
            "autor" : autor,
            "data" : data
        }

                 


        livros.append(livro)
        numlivr +=1

        menuinicial = input("deseja voltar ao menu inicial? (s/n): ")

        if menuinicial == 's':
            return
        elif menuinicial == 'n':
            continue
        

def excluir_livro():
    pass

def procurar_livro():
    while True:
        search = input("insere o nome do livro que queres procurar: ")
        for livro in livros:
            if livros(livro['nome']) == search:
                print(f"nome :{livro['nome']}")

def listar_livros():
        for livro in livros:
            print(f"numero : {livro['numlivr']})")
            print(f"nome: {livro['title']})")
            print(f"autor: {livro['autor']})")
            print(f"data: {livro['data']}")

        epa = input("deseja voltar ao menu inicial?: ")
        if epa == 's':
            return
        elif epa == 'n':
            listar_livros()

            

def ordenar_livbros():
    pass

def sair():
    pass



def menu():
    while True:
        option = 0
        print("1 - Adicionar novo livro")
        print("2 - Procurar livro por titulo ou autor")
        print("3 - Excluir livro")
        print("4 - Ordenar livros")
        print("5 - Listar livros")
        print("6 - Sair do programa")
        
        option = input("insere a operação que queres efetuar: ")

        match option:
            case '1':
                adicionar_livro()
            case '2':
                procurar_livro()
            case '3':
                pass
            case '4':
                pass
            case '5':
                listar_livros()
            case '6':
                break


menu()