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

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))
    # opcao_escolhida = int(opcao_escolhida)
    print(f'Você escolheu a opção {opcao_escolhida}') #f-string (ou Formatted String Literal)


    if opcao_escolhida == 1:
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('Listar restaurante')
    elif opcao_escolhida == 3:
        print('Ativar restaurante')
    else:
        finalizar_app()

def main():
    exibir_nome_programa()
    exibir_opcao_programa()
    escolher_opcao()

if __name__ == '__main__':
    main()