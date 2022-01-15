import json


def listar_livros(status):
    print("*************** LISTA DE LIVROS ***************")
    with open('C:/Users/SAFIRA/PycharmProjects/biblioteca/db/livros.json') as b:
        data = json.load(b)

    for book in data['books']:
        if book['status'] == status:
            numero = book['numero']
            titulo = book['titulo']
            print(numero, "-", titulo)


def retirar_livro(numero_emprestar, emprestado_para):

    numero_Emprestar = numero_emprestar
    emprestado_para = emprestado_para
    status_Indisponivel = "Indisponivel"

    with open('C:/Users/SAFIRA/PycharmProjects/biblioteca/db/livros.json') as b:
        data = json.load(b)

    for book in data['books']:
        if book['id'] == numero_Emprestar:
            print(book['id'], numero_Emprestar, 30)
            book['status'] = status_Indisponivel
            book['emprestado_para'] = emprestado_para

    with open('C:/Users/SAFIRA/PycharmProjects/biblioteca/db/livros.json', 'w') as b:
        json.dump(data, b)


def doar_livro(id, numero, titulo, autor, ano, status):

    new_book = {
        "id": id,
        "numero": numero,
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "status": status,
        "emprestado_para": " "
    }

    with open('C:/Users/SAFIRA/PycharmProjects/biblioteca/db/livros.json', "r+") as file:
        file_data = json.load(file)
        file_data["books"].append(new_book)
        file.seek(0)
        json.dump(file_data, file, indent=id)


def devolver_livro(id):
    status_disponivel = "Disponivel"

    with open('C:/Users/SAFIRA/PycharmProjects/biblioteca/db/livros.json') as b:
        data = json.load(b)

    for book in data['books']:
        if book['id'] == id:
            book['status'] = status_disponivel
            book['emprestado_para'] = ""

    with open('C:/Users/SAFIRA/PycharmProjects/biblioteca/db/livros.json', 'w') as b:
        json.dump(data, b)

def ler_dados_livros():
    nome_arquivo = 'C:/Users/SAFIRA/PycharmProjects/biblioteca/db/livros.json'
    with open("livros.json") as da:
        data = json.load(da)

    print(data)


if __name__ == '__main__':

    print('###############################')
    print('#     MENU DE OPÇÕES          #')
    print('#                             #')
    print('# 1 - Listar livros           #')
    print('# 2 - Retirar Livro           #')
    print('# 3 - Devolver Livro          #')
    print('# 4 - Doar um livro           #')
    print('# 5 - Devolver Livro          #')
    print('#                             #')
    print('# 9 - sair                    #')

    resposta = input('escolha sua opcao: ')
    print(f'A sua escolha foi :  {resposta}')

    if resposta.upper() != '9':
        if resposta == '1':
            listar_livros("Disponivel")
        elif resposta == '2':
            numero_do_livro = input('digite o codigo do livro: ')
            pessoa = input('digite o nome do usuario: ')
            print(type(numero_do_livro))
            print(type(pessoa))
            retirar_livro(int(numero_do_livro), pessoa)
        elif resposta == '3':
            id = input('digite o id do livro: ')
            numero = input('digite o numero do livro: ')
            titulo = input('digite o titulo do livro: ')
            autor = input('digite o autor do livro: ')
            ano = input('digite o ano do livro: ')
            doar_livro(int(id), numero, titulo, autor, int(ano), "Disponivel")
        elif resposta == '4':
            id = input('digite o id do livro: ')
            numero = input('digite o numero do livro: ')
            titulo = input('digite o titulo do livro: ')
            autor = input('digite o autor do livro: ')
            ano = input('digite o ano do livro: ')
            doar_livro(int(id), numero, titulo, autor, int(ano), "Disponivel")
        elif resposta == '5':
            id = input('digite o id do livro: ')
            devolver_livro(int(id))

        else:
            print('Você digitou um a opção invalida. Escolha uma opção de 1 a 5 ')
    else:
        print("Você escolheu sair. Volte sempre")
