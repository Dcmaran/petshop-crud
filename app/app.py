import sys
from functions import *

while True:
    mainMenu()
    
    option = selectOption()

    if option == "1":
        enterDataMenu()

        dataOption = selectOption()
        
        if dataOption == "1":
            enterClient()

        elif dataOption == "2":
            enterPet()

        elif dataOption == "3":
            enterAppointment()
        else:
            print("Invalid option.")

    elif option == "2":
        print("1. Atualizar Cliente")
        print("2. Atualizar Animal")
        print("3. Atualizar Consulta")

        updateOption = selectOption()
        
        if updateOption == "1":
            atualizar_cliente()

        elif updateOption == "2":
            atualizar_animal()

        elif updateOption == "3":
            atualizar_consulta()

        else:
            print("Invalid option.")


    elif option == "3":
        print("1. Recuperar Animais")
        print("2. Recuperar Clientes")
        print("3. Recuperar Consultas")
        print("4. Recuperar Animais por ID do Cliente")
        print("5. Recuperar Animal e Cliente por ID da consulta")

        viewOption = selectOption()
        
        if viewOption == "1":
            recuperar_animais()

        elif viewOption == "2":
            recuperar_cliente()

        elif viewOption == "3":
            recuperar_consultas()

        elif viewOption == "4":
            recuperar_por_id()

        elif viewOption == "5":
            recuperar_por_id_consulta()

        else:
            print("Opção inválida.")
    
    elif option == "4":
        print("1. Excluir Cliente")
        print("2. Excluir Animal")
        print("3. Excluir Consulta")
        print("Escolha uma opção: ")

        deleteOption = selectOption()

        if deleteOption == "1":
            excluir_cliente()

        elif deleteOption == "2":
            excluir_animal()

        elif deleteOption == "3":
            excluir_consulta()

        else:
            print("Invalid option.")

    elif option == "0":
        print("Exiting...")
        break
    
    else:
        print("Invalid opton. Try again.")
