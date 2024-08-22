import pymysql

def connection():

    conn = pymysql.connect(host='127.0.0.1', user='root', password='ya23101108!!', db='Triary', charset='utf8')

    cur = conn.cursor()

    sql = cur.execute("SELECT * FROM users")

    cur.execute(sql)

    conn.commit()

    conn.close()