import os

def exibir_nome_programa():
    print('Sabor Express\n') #shift + seta para baixo -> multiplica | \n -> pula uma linha

def exibir_opcao_programa():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    print('Finalizando o programa\n')

def  opcao_invalida():
    print('Opção inválida!\n')
    input('Digite uma tecla para voltar ao menu principal')
    main()

def escolher_opcao():
    try:                                                    #try - Tente: Você coloca dentro deste bloco o código que pode dar erro.
        opcao_escolhida = int(input('Escolha uma opção: ')) #Se o usuário digitar "ABC", o Python não consegue transformar isso em número e causaria um erro fatal chamado ValueError
        # opcao_escolhida = int(opcao_escolhida)
        print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            print('Cadastrar restaurante')
        elif opcao_escolhida == 2:
            print('Listar restaurante')
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
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