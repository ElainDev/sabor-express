'''
#Imprima a frase: Python na Escola de Programação da Alura.
print('Python na Escola de Programação da Alura')

#Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.
nome = input('Escreva seu nome: ')
idade = input('Digite sua idade: ')

print(f'Meu nome é {nome} e tenho {idade} anos')

print('Meu nome é {} e tenho {} anos.'.format(nome,idade)) # Abordagem do .format()


# Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha
print (' A\n L\n U\n R\n A\n')
print('A','L','U','R','A',sep='\n')

#Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa ser armazenado em uma variável e arredondado para apenas duas casas decimais.
pi = 3.14159

# Abordagem de f-string
print(f'O valor arredondado de pi é: {pi:.2f}')

# Abordagem de .format()
print('O valor arredondado de pi é: {:.2f}'.format(pi))

# Utilizando a função round()
print('O valor arredondado de pi é:', round(pi, 2))

# Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

number = int(input('Digite um número:'))

if number % 2 == 0:
    print('O número é par')
else:
    print('O número é ímpar')

# Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

age_child = int(input('Digite a idade do seu filho(a): '))

if 0 < age_child <= 12:
    print('Criança')
elif age_child > 13 and age_child <= 18:
    print('Adolescente')
else:
    print('Adulto')


#Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

name_user = input('Digite seu nome:')
password = input('Digite a sennha:')

name_login = 'Daniel'
password_login = 'bia25'

if name_user == name_login  and password == password_login :
    print("Login bem sucedido!")
else:
    print("Credenciais inválidas. Tente novamente.")
'''
#Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:
#Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
#Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
#Terceiro Quadrante: os valores de x e y devem ser menores que zero;
#Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
#Caso contrário: o ponto está localizado no eixo ou origem.

x = float(input('Digite a coordenada x: '))
y = float(input('Digite a coordenada y: '))

if x > 0 and y > 0:
    print('O ponto está no primeiro quadrante.')
elif x < 0 and y > 0:
    print('O ponto está no segundo quadrante.')
elif x < 0 and y < 0:
    print('O ponto está no terceiro quadrante.')
elif x > 0 and y < 0:
    print('O ponto está no quarto quadrante.')
else:
    print('O ponto está localizado no eixo ou origem')





