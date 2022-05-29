from flask import Flask, request as flask_request
import sqlite3 as sql
import os
import cadastro


app = Flask(__name__)


def createdb():
    if not os.path.exists('database.db'):
        conn = sql.connect('database.db')
        conn.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, status BOOLEAN, icon TEXT, email TEXT, password BLOB, CPF INTEGER)')
        conn.commit()
        conn.close()
        app.logger.info('Database created')
        return 'Database created'
    else:
        return 'Database already exists'


@app.route('/cadastro/usuarios', methods=['POST'])
def cadastro_usuarios():
    json_data = flask_request.get_json()
    if json_data:
        return cadastro.users(json_data)


if __name__ == '__main__':
    createdb()
    app.run(debug=True, port=80)