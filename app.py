import os

restaurantes = [{'nome':'Pizzaria Maluca', 'categoria': 'Italiano', 'ativo':False},
                {'nome':'Praça', 'categoria': 'Japonesa', 'ativo':True},
                {'nome':'Cantina da Dona Maria', 'categoria': 'Doce', 'ativo':False} ] # Dicionário 

def exibir_nome_programa(): #título
    print('Sabor Express\n') # alt + shift + seta para baixo -> multiplica | \n -> pula uma linha

def exibir_opcao_programa(): # "menu de opcao"
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar o estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o programa\n')

def voltar_ao_menu():
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def  opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria  do restaurante {nome_do_restaurante}: ')
    dados_dos_restaurante = {'nome': nome_do_restaurante, 'categoria':categoria, 'ativo': False}
    restaurantes.append(dados_dos_restaurante)  # append -> cada nome do restaurante que foi digitado, é ADICIONADO(append) na lista restaurante
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso\n')
    voltar_ao_menu() 

def listar_restaurante():
    exibir_subtitulo('Listando os restaurantes\n')
    print(f'{'nome_restaurante'.ljust(22)} | {'categoria'.ljust(22)} | {'Status'.ljust(22)}')

    for restaurante in restaurantes:                       # Para cada item (que chamarei de 'restaurante'/ variável temporária) dentro da lista 'restaurantes', faça o seguinte:
        nome_restaurante = restaurante['nome']             # Criando a nova variável dentro da função, que só acessa aquele especifico no dicionário, o nome 
        categoria = restaurante['categoria']
        ativo = 'ativo' if restaurante['ativo'] else 'desativado'
        print(f'.{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu()

def ativar_restaurante(): # alterna o estado do restaurante 
    exibir_subtitulo('Alternando o estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False #False, porque ainda não encontramos o restaurante

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']: #Se for iguais significa que o restaurante digitado foi encontrado 
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo'] # Se era False, vira True (Ativado). Se era True, vira False (Desativado)
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu()        


def escolher_opcao():
    try:                                                    #try - Tente: Você coloca dentro deste bloco o código que pode dar erro.
        opcao_escolhida = int(input('Escolha uma opção: ')) #Se o usuário digitar "ABC", o Python não consegue transformar isso em número e causaria um erro fatal chamado ValueError
        # opcao_escolhida = int(opcao_escolhida)
        print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            ativar_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:                                               # except - Exceção/Senão: Se qualquer erro acontecer dentro do bloco try, o Python para a execução ali mesmo e pula direto para o except.
            opcao_invalida()
    except:                                               
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcao_programa()
    escolher_opcao()

if __name__ == '__main__':
    main()