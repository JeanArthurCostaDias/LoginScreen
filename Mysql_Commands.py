import mysql.connector


def insere_usuario(con, nome, email, senha):
    cursor = con.cursor()
    sql = "INSERT INTO login (Nome,Email,Senha) values (%s,%s,%s)"
    valores = (nome, email, senha)
    cursor.execute(sql, valores)
    try:
        cursor.close()
        con.commit()
        return True
    except mysql.connector.Error as err:
        return False


def consultar_dados(con, nome, senha):
    global data
    cursor = con.cursor()
    sql = f"SELECT Nome,Senha from login WHERE Nome=%s AND Senha=%s"
    values = (nome, senha)
    cursor.execute(sql, values)
    try:
        for i,j in cursor:
            data = (i,j)
        cursor.close()
        return data
    except mysql.connector.Error as err:
        print(err)
        return False
