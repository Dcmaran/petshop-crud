import sys
from functions import *

while True:
    menu()
    print("Escolha uma opção: ")
    escolha = sys.stdin.readline().strip()

    if escolha == "1":
        print("1. Inserir Cliente")
        print("2. Inserir Animal")
        print("3. Inserir Consulta")
        print("Escolha uma opção: ")
        escolha_sub = sys.stdin.readline().strip()
        
        if escolha_sub == "1":
            inserir_cliente()
        elif escolha_sub == "2":
            inserir_animal()
        elif escolha_sub == "3":
            inserir_consulta()
        else:
            print("Opção inválida.")

    elif escolha == "2":
        print("1. Atualizar Cliente")
        print("2. Atualizar Animal")
        print("3. Atualizar Consulta")
        print("Escolha uma opção: ")
        escolha_sub = sys.stdin.readline().strip()
        
        if escolha_sub == "1":
            atualizar_cliente()
        elif escolha_sub == "2":
            atualizar_animal()
        elif escolha_sub == "3":
            atualizar_consulta()
        else:
            print("Opção inválida.")


    elif escolha == "3":
        print("1. Recuperar Animais")
        print("2. Recuperar Clientes")
        print("3. Recuperar Consultas")
        print("4. Recuperar Animais por ID do Cliente")
        print("5. Recuperar Animal e Cliente por ID da consulta")
        print("Escolha uma opção: ")
        escolha_sub = sys.stdin.readline().strip()
        
        if escolha_sub == "1":
            recuperar_animais()
        elif escolha_sub == "2":
            recuperar_cliente()
        elif escolha_sub == "3":
            recuperar_consultas()
        elif escolha_sub == "4":
            recuperar_por_id()
        elif escolha_sub == "5":
            recuperar_por_id_consulta()
        else:
            print("Opção inválida.")
    
    elif escolha == "4":
        print("1. Excluir Cliente")
        print("2. Excluir Animal")
        print("3. Excluir Consulta")
        print("Escolha uma opção: ")
        escolha_sub = sys.stdin.readline().strip()

        if escolha_sub == "1":
            excluir_cliente()
        elif escolha_sub == "2":
            excluir_animal()
        elif escolha_sub == "3":
            excluir_consulta()
        else:
            print("Opção inválida.")

    elif escolha == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
