import psycopg2

def conectardb():

    con = psycopg2.connect(

        #host='localhost',
        #database = 'chuva',
        #user = 'postgres',
        #password = '12345'

        host = 'dpg-cu8fvel2ng1s73ek9ur0-a.oregon-postgres.render.com',
        database = 'comunidades',
        user = 'comunidades_user',
        password = '4Lcl80G8j0Q2cdExitfgdCLfivb8Kd30'
    )
    return con
def login(user,senha):
    con = conectardb()
    cur = con.cursor()
    sq = f"SELECT  nome, login from usuario where login='{user}' and senha='{senha}'  "
    cur.execute(sq)
    saida = cur.fetchall()

    cur.close()
    con.close()

    return saida

def inserir_user(nome,login, senha):

    conn = conectardb()
    cur = conn.cursor()
    try:
        sql = f"INSERT INTO usuario (nome, login, senha) VALUES ('{nome}','{login}','{senha}')"
        cur.execute(sql)

    except psycopg2.IntegrityError:
        conn.rollback()
        exito = False
    else:
        conn.commit()
        exito = True

    cur.close()
    conn.close()
    return exito

def listar_usuarios():
    con = conectardb()
    cur = con.cursor()
    sql = f"SELECT  nome, login from usuario"
    cur.execute(sql)
    saida = cur.fetchall()

    cur.close()
    con.close()

    return saida


def inserir_edital(nomeedital,objetivo,local):

    conn = conectardb()
    cur = conn.cursor()
    try:
        sql = f"INSERT INTO edital (nomeedital,objetivo,local) VALUES ('{nomeedital}','{objetivo}','{local}')"
        cur.execute(sql)

    except psycopg2.IntegrityError:
        conn.rollback()
        exito = False
    else:
        conn.commit()
        exito = True

    cur.close()
    conn.close()
    return exito

def listar_editais():
    con = conectardb()
    cur = con.cursor()
    sql = f"SELECT  * from edital"
    cur.execute(sql)
    saida = cur.fetchall()

    cur.close()
    con.close()

    return saida




