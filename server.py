import dao

from flask import *

app = Flask(__name__)

app.secret_key = '!@S4KUR4@!@!'

@app.route('/login', methods=['POST'])
def fazer_login():
    login = request.form.get('username')
    senha = request.form.get('password')
    saida = dao.login(login, senha)
    print(saida)
    if len(saida) > 0:
        session['login'] = login
        nome_user = saida[0][0]
        return render_template('lobby.html' ,nome=nome_user)
    else:
        return render_template('register.html')

@app.route('/logout', methods=['POST', 'GET'])
def sair():
    session.pop('login')
    return render_template('register.html')

@app.route('/')
def home():
    return  render_template('register.html')


def lobby():
    return render_template("lobby.html")

@app.route("/redirecionar")
def redirecionar():
    return render_template("cadastrareditais")

@app.route("/cadastrareditais")
def comunidades():
    return render_template("cadastrareditais.html")

@app.route('/mostrar_cadastro')
def mostrar_pag_cadastro():
    return render_template('paginacadastro.html')

@app.route('/cadastrarusuario', methods=['POST'])
def cadastrar_usuario():
    nome = request.form.get('nome')
    login = request.form.get('login')
    senha = request.form.get('senha')

    if dao.inserir_user(nome, login, senha):
        msg= 'usuário inserido com sucesso'
        return render_template('register.html', texto=msg)
    else:
        msg = 'Erro ao inserir usuário'
        return render_template('register.html', texto=msg)

@app.route('/listadeusuarios')
def listar_usuarios():

    usuarios = dao.listar_usuarios()
    print(usuarios)
    return render_template('listadeusuarios.html', lista=usuarios)

@app.route('/cadastrareditais', methods=['POST'])
def cadastrar_editais():
    nomeedital = request.form.get('nomeedital')
    objetivo = request.form.get('objetivo')
    local = request.form.get('local')

    print(nomeedital,objetivo,local)

    if dao.inserir_edital(nomeedital, objetivo,local):
        msg= 'edital inserido com sucesso'
        return render_template('lobby.html', texto=msg)
    else:
        msg = 'Erro ao inserir o edital'
        return render_template('cadastrareditais.html', texto=msg)



@app.route('/listareditais')
def listar_editais():

    editais= dao.listar_editais()
    print(editais)
    return render_template('listadeeditais.html', lista=editais)


if __name__ == '__main__':
    app.run(debug=True)
