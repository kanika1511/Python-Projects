import mysql.connector as sql
conn=sql.connect(host="localhost",user="root",passwd="manager",database="old")
if conn.is_connected():
    print('successfully connected')
c1=conn.cursor()    
c1.execute('create table login(name varchar(50),user_id varchar(30)primary key,passwd varchar(20))')

