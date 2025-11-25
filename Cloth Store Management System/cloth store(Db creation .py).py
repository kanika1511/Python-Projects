import mysql.connector as sql
conn=sql.connect(host="localhost",user="root",passwd="manager",database="old")
if conn.is_connected():
    print('')

c1=conn.cursor()
c1.execute('use old')
print("WELCOME TO GRAND CLOTH STORE")
print(' ')
from time import gmtime,strftime
a=strftime("%a,%d%b%y",gmtime())
print(a)
print(' ')
print("1.login")
print("2.To create account")
print("")
print('')
choice=int(input("enter your choice:"))
print(' ')
if choice==1:

    a=input("enter user_id:")
    c1.execute("select passwd from login where user_id = '"+(a)+"' ;")
    data=c1.fetchall()
    data=data[0]
    data=list(data)
    data=data[0]
    data=str(data)
    print(' ')
    print(' ')
    b=int(input("enter passwd:"))
    conn.cursor()
    conn.commit()
if choice==2:
    print('to create your account please enter your user id and password')
    c1=conn.cursor()
    v_name=input("your full  name:")
    print('')
    v_user_id=input("choose your user id :")
    print('')
    v_passwd=int(input("create your password (in integer):"))
    print('')
    c1=conn.cursor()
    update="insert into login values('"+v_name+"','"+ v_user_id +"',"+ str(v_passwd)+")"
    c1.execute(update)
    conn.commit()
    print("account created")
print("if shopping is done press 1.")
print("if you like to file any marketing problem press 2.")
print("if no shopping is done press 3.")
choice=int(input("enter your choice="))
if choice==1:
    v_customer_name=input("enter your name:")
    v_gender=input("enter gender:")
    v_phone_no=int(input("enter your phone no:"))
    v_items=input("enter item name:")
    v_qty=int(input("enter quantity:"))
    v_payment=int(input("make payment:"))
    v_SQL_INSERT="insert into cloth values('"+v_customer_name+"','"+v_gender+"',"+str(v_phone_no)+",'"+v_items+"',"+str(v_qty)+","+str(v_payment)+")"
    c1.execute(v_SQL_INSERT)
    print("THANK YOU...For your visit.")
if choice==2:
    c1.execute('USE old')
    v_rate_issue=int(input("rate your difficultes out of 10="))
    v_write_problem=input("write your problem:")
    v_SQL_INSERT="insert into problem values("+str(v_rate_issue)+",'"+v_write_problem+"')"
    c1.execute(v_SQL_INSERT)
    print("Your problem will be rectified....thank you.")
if choice==3:
    c1.execute('use old')
    v_comment=input("comment about store here please:")
    v_SQL_insert="insert into comment values('"+v_comment+"')"
    c1.execute(v_SQL_insert)
    print("THANK YOU FOR YOUR VISIT ....WISH YOU BEST.")
conn.commit()


