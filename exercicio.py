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
'''
'''
# FOR

numero = -1 (apenas um valor inicial inválido).
for _ in range(3):  # Supondo um número máximo de tentativas (3) arbitrário
    numero = int(input("Digite um número positivo: "))
    if numero > 0:
        break        #Se for positivo, o comando break "quebra" o loop imediatamente e pula para o final.

print("Você digitou:", numero)


'''

'''
# WHILE

numero = -1
while numero <= 0:
    numero = int(input("Digite um número positivo: "))

print("Você digitou:", numero)
'''
'''
 Crie uma lista para cada informação a seguir:

Lista de números de 1 a 10;
Lista com quatro nomes;
Lista com o ano que você nasceu e o ano atual.
'''
'''
numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
four_names = ['Ana', 'Beatriz', 'Daniel', 'Santos']
year = [2001 , 2026]

# Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
food = ['Pizza', 'Sushi', 'Macarrão', 'Pão']

for foods in food:
    print(f'.{foods}')

# Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
soma_impares = 0

for i in range (3,5,9):
    soma_impares += i

print(soma_impares)

# Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
numero = int(input('Digite um número: '))
for i  in range(1, 11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')

# Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
list_number = [2, 5 , 9 , 2 , 1]
soma_total = 0

try:
    for numero in list_number:
        soma_total += numero  # O mesmo que: soma_total = soma_total + numero
    
    print(f"A soma de todos os elementos é: {soma_total}")

except TypeError: #captura casos onde alguém pode ter colocado uma palavra (string) no meio da lista de números por engano.
    print("Erro: A lista contém itens que não são números!")
except Exception as e: #serve como uma rede de segurança para qualquer outro erro que não previmos.
    print(f"Ocorreu um erro inesperado: {e}")

# Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
soma_total2 = 0
try:
    for numero1  in list_number:
       soma_total2 += numero1 # somamMediana = somamMediana + numero1
        
    media = soma_total2 / len(list_number) # len(list_number) nos dá a quantidade de itens na lista
    
    print(f'A média é {media}')

except TypeError:
    print("Erro: A lista está vazia, não é possível calcular a média de zero elementos.")
except TypeError:
    print("Erro: A lista contém valores que não são números.")
'''
#1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
pessoa = [{'nome': 'Ana', 'idade': 24 , 'cidade':'Recife'}]

#2 - Utilizando o dicionário criado no item 1:
#Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
pessoa['idade'] = 31
#Adicione um campo de profissão para essa pessoa;
pessoa['Profissao'] = 'Engenharia'
#Remova um item do dicionário.
del pessoa['cidade']

#3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.
numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)
#4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
pessoa1 = {'nome': 'Amanda', 'idade': 19, 'cidade': 'São Luís'}
if 'nome' in pessoa1:
    print("A chave 'nome' existe no dicionário.")
else:
    print("A chave 'nome' não existe no dicionário.")
#5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)
