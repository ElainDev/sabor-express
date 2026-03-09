<h1 align="center"> 🍕 Sabor Express - Primeira Aplicação com Python </h1>

<p align="center">
Este projeto foi desenvolvido durante o curso de <b>Python: crie a sua primeira aplicação</b> da Alura.
</p>

<div align="center"> <img src="assets/Finalizado.png" width="100px" alt="Status" style="vertical-align: middle;"> <strong style="font-size: 18px;">Status: Finalizado ✅🚀</strong> </div>

<br>


## 📝 Sobre o Projeto
   O **Sabor Express** é um sistema de gerenciamento de restaurantes via terminal. Ele permite registrar estabelecimentos, categorizá-los e gerenciar sua disponibilidade no sistema (Ativo/Desativado), utilizando uma interface organizada e intuitiva no console.

## 🛠️ Novas Funcionalidades:
- [x] **Cadastro de Restaurantes:** Registro de nome e categoria salvos em dicionários.
- [x] **Listagem Formatada:** Exibição elegante utilizando alinhamento de texto (`ljust`).
- [x] **Alternar Estado:** Lógica inteligente para ativar/desativar restaurantes com verificação de existência.
- [x] **Interface Dinâmica:** Subtítulos estilizados com bordas dinâmicas e limpeza de tela.
- [x] **Robustez:** Tratamento de erros para entradas inválidas do usuário.

## 🚀 Tecnologias Utilizadas
* **Python 3.12**
* **Biblioteca `os`**: Para limpeza e manipulação do sistema de arquivos do terminal.

## 🛠️ Como rodar o projeto
1. Tenha o Python instalado (versão 3 ou superior).
2. Clone este repositório.
3. No terminal, execute:
   ```bash  
    python app.py
  

## 🧠 Conhecimentos Adquiridos

Neste projeto, apliquei diversos conceitos de lógica de programação:

| Categoria | O que foi usado |
| :--- | :--- |
| **Dicionários `{}`** | Armazenamento de dados no formato chave-valor (`key: value`). |
| **Modularização** | Criação de funções com `def` para organizar o fluxo. |
| **Bibliotecas** | `import os` para interagir com o sistema operacional. |
| **Entrada de Dados** | `input()` com conversão de tipo `int()`. |
| **Saída de Dados** | `print()` e uso de f-strings para mensagens dinâmicas. |
| **Fluxo de Decisão** | Estruturas condicionais `if`, `elif` e `else`. |
| **Tratamento de Erros** | Blocos `try` e `except` para evitar interrupções por inputs inválidos. |
| **Ponto de Entrada** | Uso do `if __name__ == '__main__':` para garantir a execução correta. |
| **Estrutura de Dados** | Uso de Listas `[]` para armazenamento de dados voláteis. |
| **Manipulação de Listas** | Método `.append()` para adicionar novos elementos dinamicamente. |
| **Lógica Booleana** | Inversão de estado usando o operador `not`. |
| **Operadores Ternários** | Condicionais simplificadas para exibição de status e mensagens. |
| **Refatoração** | Funções parametrizadas (ex: exibir_subtitulo) para evitar repetição de código. |
| **UX no Terminal** |Uso de input() para pausar a execução e os.system('cls'). |


## Anotação 📝
| Sintaxe | Função |
| :--- | :--- |
| print() | Exibe informações no console/terminal. |
| input() | Recebe dados digitados pelo usuário. (sempre como string) |
| print() | Exibe informações no console/terminal. |
| os.system('cls') | Limpa o terminal para o usuário não ver o "lixo" de comandos anteriores. |
| f'texto {var}' | F-Strings: Interpola variáveis dentro de textos de forma simples. |
| \n | Caractere de escape que pula uma linha no console. |
| int(input()) | Garante que o que o usuário digitou seja tratado como número (inteiro). |
| match | Estrutura de seleção (semelhante ao switch/case) para múltiplas condições. |
| try / except | Tenta executar um código e captura o erro caso algo dê errado, impedindo o crash do app. |
| lista = [] | Declaração de uma lista vazia para armazenar múltiplos valores. Lista é mutável |
| .append() | Adiciona um novo item ao final de uma lista existente. |
| tuplas = () | Declaração de uma "lista" (tupla) vazia para armazenar múltiplos valores. Tupla é imutável (constante) |
| dicionario = {'chave': 'valor'} | Estrutura que mapeia chaves a valores específicos. |
| restaurante['nome'] | Forma de acessar o valor de uma propriedade específica no dicionário. |
| restaurantes.append(novo_dict) | Adiciona um dicionário inteiro como um novo item na lista. |
| for r in lista: | Itera sobre a lista, onde cada `r` representa um dicionário completo. |
| .ljust(n) | Ajusta o texto à esquerda preenchendo com espaços até completar n caracteres. |
| not valor | Inverte um valor booleano (True vira False e vice-versa). |
| var = x if cond else y | Atribui um valor baseado em uma condição em apenas uma linha. |
| len(texto) | Conta o número de caracteres para criar bordas dinâmicas proporcionais. |

<h2 align="center">🤝 Contribuição</h2>
<p align="center">Este é um projeto de estudos. Sinta-se à vontade para dar sugestões ou feedbacks!</p>