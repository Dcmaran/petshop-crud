import psycopg2
import sys

def dataConnection():
    try:
        connection = psycopg2.connect(
            dbname="petshop_crud",
            user="postgres",
            password="dcmrdb",
            host="172.17.0.1",
            port="5432"
        )

        cursor = connection.cursor()

        return connection, cursor

    except Exception as e:
        print(f"Error creating connection: {e}")

def selectOption():
    print("Choose a option: ")
    option = sys.stdin.readline().strip()
    return option

def mainMenu():
    print("1. Enter data")
    print("2. Update data")
    print("3. View data")
    print("4. Delete Data")
    print("0. exit")

# Enter data Functions
def enterDataMenu():
    print("1. Enter Client")
    print("2. Enter Pet")
    print("3. Enter Appointment ")
    
def enterClient():
    connection, cursor = dataConnection()

    nome = input("Enter name: ")
    telefone = input("Enter phone number: ")

    try:
        cursor.execute("INSERT INTO cliente (nome, telefone) VALUES (%s, %s);", (nome, telefone))
        connection.commit()
        print("Data entered successfully!")
    except Exception as e:
        print(f"Error entering data: {e}")
    finally:
        connection.close()

def enterPet():
    connection, cursor = dataConnection()

    nome = input("Enter pet name: ")
    especie = input("Enter pet species: ")
    cliente_id = int(input("Enter the pet owner's ID: "))

    try:
        cursor.execute("INSERT INTO animal (nome, especie, dono_id) VALUES (%s, %s, %s) RETURNING id;", (nome, especie, cliente_id))
        animal_id = cursor.fetchone()[0]

        print(f"Animal inserido com ID: {animal_id}")
    except Exception as e:
        print(f"Erro ao inserir animal: {e}")
    finally:
        connection.commit()
        connection.close()

def enterAppointment():
    connection, cursor = dataConnection()

    date = input("Enter the appointment date (YYYY-MM-DD): ")
    pet_id = int(input("Enter the pet's ID for the appointment: "))
    description = input("Enter the appointment description: ")

    try:
        cursor.execute("INSERT INTO consulta (data, animal_id, descricao) VALUES (%s, %s, %s) RETURNING id;", (date, pet_id, description))
        consulta_id = cursor.fetchone()[0]

        print(f"Consulta inserida com ID: {consulta_id}")
    except Exception as e:
        print(f"Erro ao inserir consulta: {e}")
    finally:
        connection.commit()
        connection.close()

# Update data Functions
def atualizar_cliente():
    conn = conectar()
    cur = conn.cursor()

    id_cliente = int(input("Digite o ID do cliente que deseja atualizar: "))
    novo_telefone = input("Digite o novo telefone: ")
    novo_nome = input("Digite o novo nome: ")

    try:
        cur.execute("UPDATE cliente SET nome = %s, telefone = %s WHERE id = %s;", (novo_nome, novo_telefone, id_cliente))
        conn.commit()
        print("Dados atualizados com sucesso!")
    except Exception as e:
        print(f"Erro ao atualizar dados: {e}")
    finally:
        conn.close()
    
def atualizar_animal():
    conn = conectar()
    cur = conn.cursor()

    id_animal = int(input("Digite o ID do animal que deseja atualizar: "))
    novo_nome = input("Digite o novo nome: ")
    nova_especie = input("Digite a nova especie: ")
    novo_id_dono = input("Digite a novo ID do dono: ")

    try:
        cur.execute("UPDATE animal SET nome = %s, especie = %s, dono_id = %s WHERE id = %s;", (novo_nome, nova_especie, novo_id_dono, id_animal))
        conn.commit()
        print("Dados atualizados com sucesso!")
    except Exception as e:
        print(f"Erro ao atualizar dados: {e}")
    finally:
        conn.close()

def atualizar_consulta():
    conn = conectar()
    cur = conn.cursor()

    id_consulta = int(input("Digite o ID da consulta que deseja atualizar: "))
    nova_data = input("Digite a nova Data: ")
    novo_id_animal = input("Digite o novo ID do animal da consulta: ")
    nova_descricao = input("Digite a nova descricao: ")

    try:
        cur.execute("UPDATE consulta SET data = %s, animal_id = %s, descricao = %s WHERE id = %s;", (nova_data, novo_id_animal, nova_descricao, id_consulta))
        conn.commit()
        print("Dados atualizados com sucesso!")
    except Exception as e:
        print(f"Erro ao atualizar dados: {e}")
    finally:
        conn.close()


def recuperar_cliente():
    conn = conectar()
    cur = conn.cursor()

    try:
        cur.execute("SELECT * FROM cliente;")
        rows = cur.fetchall()

        for row in rows:        
            print(row)

    except Exception as e:
        print(f"Erro ao recuperar dados: {e}")
    finally:
        conn.close()


def recuperar_animais():
    conn = conectar()
    cur = conn.cursor()

    try:
        cur.execute("SELECT * FROM animal;")
        rows = cur.fetchall()

        for row in rows:        
            print(row)

    except Exception as e:
        print(f"Erro ao recuperar dados: {e}")
    finally:
        conn.close()


def recuperar_consultas():
    conn = conectar()
    cur = conn.cursor()

    try:
        cur.execute("SELECT * FROM consulta;")
        rows = cur.fetchall()

        for row in rows:        
            print(row)

    except Exception as e:
        print(f"Erro ao recuperar dados: {e}")
    finally:
        conn.close()

def excluir_cliente():
    conn = conectar()
    cur = conn.cursor()

    cliente_id = int(input("Digite o ID do cliente que deseja excluir: "))

    try:
        cur.execute("DELETE FROM cliente WHERE id = %s;", (cliente_id,))

        conn.commit()
        print("Cliente excluído com sucesso!")
    except Exception as e:
        print(f"Erro ao excluir cliente: {e}")
    finally:
        conn.close()

def excluir_animal():
    conn = conectar()
    cur = conn.cursor()

    animal_id = int(input("Digite o ID do animal que deseja excluir: "))

    try:
        cur.execute("DELETE FROM animal WHERE id = %s;", (animal_id,))
        conn.commit()
        print("Animal excluído com sucesso!")
    except Exception as e:
        print(f"Erro ao excluir animal: {e}")
    finally:
        conn.close()

def excluir_consulta():
    conn = conectar()
    cur = conn.cursor()

    consulta_id = int(input("Digite o ID da consulta que deseja excluir: "))

    try:
        cur.execute("DELETE FROM consulta WHERE id = %s;", (consulta_id,))
        conn.commit()
        print("Consulta excluída com sucesso!")
    except Exception as e:
        print(f"Erro ao excluir consulta: {e}")
    finally:
        conn.close()

def recuperar_por_id():

    cliente_id = int(input("Digite o ID do Cliente para ver seus animais: "))
    conn = conectar()
    cur = conn.cursor()

    try:
        # Exemplo de JOIN entre as tabelas cliente e animal
        cur.execute("""
            SELECT cliente.id as cliente_id, cliente.nome as cliente_nome, 
                   animal.id as animal_id, animal.nome as animal_nome, animal.especie
            FROM cliente
            LEFT JOIN animal ON cliente.id = animal.dono_id
            WHERE cliente.id = %s;
        """, (cliente_id,))

        rows = cur.fetchall()

        if not rows:
            print(f"Nenhum cliente encontrado com o ID {cliente_id}")
            return

        cliente_info = None
        pets_info = []

        for row in rows:
            if cliente_info is None:
                cliente_info = {'id': row[0], 'nome': row[1]}
            
            pets_info.append({'id': row[2], 'nome': row[3], 'especie': row[4]})

        print(f"Informações do Cliente (ID {cliente_info['id']}):")
        print(f"Nome do Cliente: {cliente_info['nome']}")
        print("Animais de Estimação:")
        for pet in pets_info:
            print(f"  - ID: {pet['id']}, Nome: {pet['nome']}, Espécie: {pet['especie']}")

    except Exception as e:
        print(f"Erro ao recuperar dados: {e}")
    finally:
        conn.close()

def recuperar_por_id_consulta():

    consulta_id = int(input("Digite o ID da Consulta para recuperar informações: "))
    conn = conectar()
    cur = conn.cursor()

    try:
        # Exemplo de consulta utilizando JOIN entre as tabelas cliente, animal e consulta
        cur.execute("""
            SELECT cliente.id as cliente_id, cliente.nome as cliente_nome, 
                   animal.id as animal_id, animal.nome as animal_nome, animal.especie,
                   consulta.id as consulta_id, consulta.data, consulta.descricao
            FROM consulta
            LEFT JOIN animal ON consulta.animal_id = animal.id
            LEFT JOIN cliente ON animal.dono_id = cliente.id
            WHERE consulta.id = %s;
        """, (consulta_id,))

        row = cur.fetchone()

        if not row:
            print(f"Nenhuma consulta encontrada com o ID {consulta_id}")
            return

        cliente_info = {'id': row[0], 'nome': row[1]}
        animal_info = {'id': row[2], 'nome': row[3], 'especie': row[4]}
        consulta_info = {'id': row[5], 'data': row[6], 'descricao': row[7]}

        print(f"Informações da Consulta (ID {consulta_info['id']}):")
        print(f"Data da Consulta: {consulta_info['data']}")
        print(f"Descrição: {consulta_info['descricao']}")
        print("\nInformações do Cliente:")
        print(f"  - ID: {cliente_info['id']}, Nome: {cliente_info['nome']}")
        print("\nInformações do Animal:")
        print(f"  - ID: {animal_info['id']}, Nome: {animal_info['nome']}, Espécie: {animal_info['especie']}")

    except Exception as e:
        print(f"Erro ao recuperar dados: {e}")
    finally:
        conn.close()