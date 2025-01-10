# Este programa foi desenvolvido como parte de um projeto para uma disciplina de Programação de Computadores.
# O objetivo é criar um sistema de gerenciamento de livros para uma pequena empresa.
# O sistema permite cadastrar, consultar, remover livros e encerrar o programa.

# Função para cadastrar um livro na lista de livros
def cadastrar_livro(id):
    # Solicita informações sobre o livro ao usuário
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor do livro: ")
    editora = input("Digite o nome da editora do livro: ")
    # Cria um dicionário contendo os detalhes do livro e adiciona à lista de livros
    livro = {'id': id, 'nome': nome, 'autor': autor, 'editora': editora}
    lista_livro.append(livro)
    print("Livro cadastrado com sucesso!")

# Função para consultar um livro por ID
def consultar_por_id():
    # Solicita ao usuário o ID do livro que deseja consultar
    id_consulta = int(input("Digite o ID do livro que deseja consultar: "))
    # Percorre a lista de livros e verifica se algum tem o ID fornecido
    for livro in lista_livro:
        if livro['id'] == id_consulta:
            # Se encontrado, imprime os detalhes do livro na tela
            print("Livro encontrado:")
            print("ID:", livro['id'])
            print("Nome:", livro['nome'])
            print("Autor:", livro['autor'])
            print("Editora:", livro['editora'])
            return
    # Se nenhum livro for encontrado com o ID fornecido, exibe uma mensagem informando
    print("Livro não encontrado.")

# Função para consultar livros
def consultar_livro():
    # Solicita ao usuário que escolha uma opção de consulta
    opcao = input("Escolha uma opção (1. Consultar Todos / 2. Consultar por Id / 3. Consultar por Autor / 4. Retornar ao menu): ")
    if opcao == '1':
        # Se escolhida a opção de consultar todos, imprime todos os livros na lista
        for livro in lista_livro:
            print(livro)
    elif opcao == '2':
        # Se escolhida a opção de consultar por ID, chama a função para consultar por ID
        consultar_por_id()
    elif opcao == '3':
        # Se escolhida a opção de consultar por autor, solicita o nome do autor e imprime os livros correspondentes
        autor_consulta = input("Digite o nome do autor: ")
        for livro in lista_livro:
            if livro['autor'] == autor_consulta:
                print(livro)
    elif opcao == '4':
        return
    else:
        print("Opção inválida!")

# Função para remover livro
def remover_livro():
    # Solicita ao usuário o ID do livro que deseja remover
    id_remover = int(input("Digite o id do livro a ser removido: "))
    # Percorre a lista de livros e verifica se algum tem o ID fornecido
    for livro in lista_livro:
        if livro['id'] == id_remover:
            # Se encontrado, remove o livro da lista
            lista_livro.remove(livro)
            print("Livro removido com sucesso!")
            return
    # Se nenhum livro for encontrado com o ID fornecido, exibe uma mensagem informando
    print("Livro não encontrado!")

# Função principal
def main():
    # Mensagem de boas-vindas ao iniciar o programa
    print("Bem-vindo ao sistema de gerenciamento de livros do Diogo Pedroso ")
    # Inicializa o ID global com 1
    global id_global
    id_global = 1
    while True:
        # Exibe o menu de opções para o usuário
        print("\nMenu:")
        print("1. Cadastrar Livro")
        print("2. Consultar Livro")
        print("3. Remover Livro")
        print("4. Encerrar Programa")
        # Solicita ao usuário que escolha uma opção
        opcao_menu = input("Escolha uma opção: ")

        if opcao_menu == '1':
            # Se escolhida a opção de cadastrar livro, chama a função correspondente
            cadastrar_livro(id_global)
            id_global += 1
        elif opcao_menu == '2':
            # Se escolhida a opção de consultar livro, chama a função correspondente
            consultar_livro()
        elif opcao_menu == '3':
            # Se escolhida a opção de remover livro, chama a função correspondente
            remover_livro()
        elif opcao_menu == '4':
            # Se escolhida a opção de encerrar o programa, exibe uma mensagem de encerramento e sai do loop
            print("Encerrando o programa...")
            break
        else:
            # Se escolhida uma opção inválida, exibe uma mensagem de erro
            print("Opção inválida!")

# Lista de livros (inicialmente vazia)
lista_livro = []

# Execução do programa
if __name__ == "__main__":
    main()
