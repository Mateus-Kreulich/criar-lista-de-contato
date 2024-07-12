import json
import os

ARQUIVO_CONTATOS = 'contatos.json'

def carregar_contatos():
    if os.path.exists(ARQUIVO_CONTATOS):
        with open(ARQUIVO_CONTATOS, 'r') as file:
            return json.load(file)
    return {}

def salvar_contatos(contatos):
    with open(ARQUIVO_CONTATOS, 'w') as file:
        json.dump(contatos, file, indent=4)

def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")

    contatos = carregar_contatos()
    contatos[nome] = {"telefone": telefone, "email": email}
    salvar_contatos(contatos)

    print(f"Contato {nome} adicionado com sucesso!")

def listar_contatos():
    contatos = carregar_contatos()
    if not contatos:
        print("Nenhum contato encontrado.")
    else:
        for nome, detalhes in contatos.items():
            print(f"Nome: {nome}, Telefone: {detalhes['telefone']}, Email: {detalhes['email']}")

def buscar_contato():
    nome = input("Digite o nome do contato que deseja buscar: ")
    contatos = carregar_contatos()

    if nome in contatos:
        detalhes = contatos[nome]
        print(f"Nome: {nome}, Telefone: {detalhes['telefone']}, Email: {detalhes['email']}")
    else:
        print(f"Contato {nome} não encontrado.")

def menu():
    while True:
        print("\n--- Menu de Contatos ---")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Buscar contato")
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_contato()
        elif escolha == '2':
            listar_contatos()
        elif escolha == '3':
            buscar_contato()
        elif escolha == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
 