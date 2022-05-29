import sqlite3 as sql
import crypt


def users(json_data):
    password = crypt.encrypt(json_data["pass"])
    passw = password.decode('utf-8')
    print(passw)

    try:
        conn = sql.connect('database.db')
        cur = conn.cursor()
        cur.execute(f'INSERT INTO users (name, email, CPF, password) VALUES ("{json_data["name"]}", "{json_data["email"]}", "{json_data["cpf"]}", "{password}")')
        conn.commit()

        return f'Usuário: {json_data["name"]} inserido com o emails: {json_data["email"]}, cpf: {json_data["cpf"]} e senha: password: {password}'

    except Exception as e:
        return(str(e))