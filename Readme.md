<h1 align="center"> 🍕 Sabor Express - Primeira Aplicação com Python </h1>

<p align="center">
Este projeto foi desenvolvido durante o curso de <b>Python: crie a sua primeira aplicação</b> da Alura.
</p>

<div align="center"> <img src="assets/Estudando.png" width="100px" alt="Status" style="vertical-align: middle;"> <strong style="font-size: 18px;">Status: Estudando e codando 🚀</strong> </div>

<br>


## 📝 Sobre o Projeto
   O **Sabor Express** é uma aplicação de linha de comando que permite gerenciar uma lista de restaurantes. O sistema permite o cadastro, a categorização e o controle de status (ativo/inativo) de cada estabelecimento, simulando um sistema real de delivery.

## 🛠️ Novas Funcionalidades:
- [x] **Dicionários de Dados:** Cada restaurante agora possui `nome`, `categoria` e `status`.
- [x] **Listagem Dinâmica:** Percorre a lista de dicionários e exibe as informações formatadas.
- [x] **Refatoração:** Criação de funções auxiliares como `exibir_subtitulo` e `voltar_ao_menu` para melhor reutilização de código.
- [x] **Interatividade:** O usuário pode cadastrar novos restaurantes que são salvos em tempo de execução.

## 🚀 Tecnologias Utilizadas
* **Python 3.12**
* **Biblioteca `os`**: Para limpeza do console e melhor experiência visual.

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

<h2 align="center">🤝 Contribuição</h2>
<p align="center">Este é um projeto de estudos. Sinta-se à vontade para dar sugestões ou feedbacks!</p>