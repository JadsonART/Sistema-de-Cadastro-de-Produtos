from flask import Flask, request, render_template, redirect, url_for
from datetime import date
import sqlite3
from sqlite3 import Error
import os

app = Flask(__name__)

# Função para criar a tabela 'produtos' se não existir
def init_db():
    if not os.path.exists('database/db-produtos.db'):
        conn = sqlite3.connect('database/db-produtos.db')
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE produtos (
                idproduto INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                precocompra REAL NOT NULL,
                precovenda REAL NOT NULL,
                datacriacao DATE NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

init_db()


@app.route('/produtos/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        descricao = request.form['descricao']
        precocompra = request.form['precocompra']
        precovenda = request.form['precovenda']
        datacriacao = date.today()

        conn = None
        if descricao and precocompra and precovenda:
            try:
                conn = sqlite3.connect('database/db-produtos.db')
                sql = ''' INSERT INTO produtos(descricao, precocompra, precovenda, datacriacao)
                          VALUES(?,?,?,?) '''
                cur = conn.cursor()
                cur.execute(sql, (descricao, precocompra, precovenda, datacriacao))
                conn.commit()
                return redirect(url_for('listar'))
            except Error as e:
                print(e)
            finally:
                if conn:
                    conn.close()
    return render_template('cadastrar.html')

@app.route('/produtos/listar', methods=['GET'])
def listar():
    try:
        conn = sqlite3.connect('database/db-produtos.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM produtos")
        registros = cur.fetchall()
        return render_template('listar.html', regs=registros)
    except Error as e:
        print(e)
    finally:
        conn.close()

@app.route('/produtos/editar/<int:idproduto>', methods=['GET', 'POST'])
def editar(idproduto):
    if request.method == 'POST':
        descricao = request.form['descricao']
        precocompra = request.form['precocompra']
        precovenda = request.form['precovenda']
        try:
            conn = sqlite3.connect('database/db-produtos.db')
            sql = ''' UPDATE produtos SET descricao=?, precocompra=?, precovenda=? WHERE idproduto=? '''
            cur = conn.cursor()
            cur.execute(sql, (descricao, precocompra, precovenda, idproduto))
            conn.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()
        return redirect(url_for('listar'))
    else:
        try:
            conn = sqlite3.connect('database/db-produtos.db')
            cur = conn.cursor()
            cur.execute("SELECT * FROM produtos WHERE idproduto=?", (idproduto,))
            produto = cur.fetchone()
        except Error as e:
            print(e)
        finally:
            conn.close()
        return render_template('editar.html', produto=produto)

@app.route('/produtos/deletar/<int:idproduto>', methods=['POST'])
def deletar(idproduto):
    try:
        conn = sqlite3.connect('database/db-produtos.db')
        cur = conn.cursor()
        cur.execute("DELETE FROM produtos WHERE idproduto=?", (idproduto,))
        conn.commit()
    except Error as e:
        print(e)
    finally:
        conn.close()
    return redirect(url_for('listar'))

@app.errorhandler(404)
def pagina_nao_encontrada(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
