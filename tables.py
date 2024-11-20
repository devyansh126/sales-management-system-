import mysql.connector as sql
conn = sql.connect(host='localhost', user='root', password='dev123')
if conn.is_connected():
    print("Connection Established.")
c1 = conn.cursor()
c1.execute("CREATE DATABASE IF NOT EXISTS sms1")
c1.execute('USE sms1')
c1.execute("CREATE TABLE IF NOT EXISTS stock (product_no INT(10) PRIMARY KEY, product_name VARCHAR(30), cost_per_product INT(10), stock INT(10), purchased INT(10));")
c1.execute("CREATE TABLE IF NOT EXISTS user (username VARCHAR(255), passwd VARCHAR(255));")
conn.commit()
c1.close()
conn.close()

