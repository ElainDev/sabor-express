import os

restaurantes = ['Pizza','Sushi'] 

def exibir_nome_programa():
    print('Sabor Express\n') #shift + seta para baixo -> multiplica | \n -> pula uma linha

def exibir_opcao_programa():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
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
    print(texto)

def listar_restaurante():
    exibir_subtitulo('Listando os restaurantes\n')

    for restaurante in restaurantes:                       #Para cada item (que chamarei de 'restaurante'/ variável temporária) dentro da lista 'restaurantes', faça o seguinte:
        print(f'.{restaurante}')

    voltar_ao_menu()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes\n')
    
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante) # append -> cada nome do restaurante que foi digitado, é ADICIONADO(append) na lista restaurante
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso\n')
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