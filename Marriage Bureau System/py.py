import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='manager',database='marriage_bureaw_management')
if conn.is_connected():
     c1=conn.cursor()
     print('________________________________________________________________WELCOME   TO  BSF  MARTIMONIAL  SERVICE  _______________________________________________________')
     c='y'
     while c.lower()=='y':
          print('=======================')
          print("1.provide details")
          print('2. in search of bridegroom')
          choice=int(input('enter the choice:'))
          if choice==1:
              print('==========================')
              print('5.Male customer details')
              print('6.Female customer details')
              choice=int(input('enter the choice:-'))
          if choice==2:
               print('========================')
               print('3. Handsome Bride ')
               print('4. Beautiful Groom ')
               choice=int(input('enter the choice-'))
          if choice == 5 :
               a=(input('enter the name:'))
               b=(input('enter the address:'))
               c=(input('enter the caste:'))
               d=(input('enter the appreance:'))
               e=(input('enter the age:'))
               f=(input('enter the profession:'))
               g=(input('enter the phone_no:'))
               c1=conn.cursor()
               sql_insert="insert into legends_details values( '{}','{}','{}','{}','{}','{}','{}')".format(a,b,c,d,e,f,g)
               c1.execute(sql_insert)
               conn.commit()
               print ('Data inserted')
               c=input('do you want to continue (y/[n]:)')
               
                    
          if choice==6:
               h=(input('enter the name:'))
               i=(input('enter the address:'))
               j=(input('enter the caste:'))
               k=(input('enter the appreance:'))
               l=(input('enter the age:'))
               m=(input('enter the profession:'))
               n=(input('enter the phone_no:'))
               c1=conn.cursor()
               sql_insert="insert into girls_details values( '{}','{}','{}','{}','{}','{}','{}')".format(h,i,j,k,l,m,n)
               c1.execute(sql_insert) 
               conn.commit()
               print("Details are successfully inserted")
               c=input('do you want to continue (y/[n]:)')
               if c =='y' :
                       continue
               else:
                         print('THANK  YOU  FOR  VISITING  OUR   WEBSITE' )
                         print('VISIT  AGAIN')
          if choice==3:
               prof=(input('Enter the profession:'))
               c1.execute("select* from legends_details where profession='{}'". format(prof))
               data= c1.fetchall()
               print("name\t\t address\t\t caste\t\t  appreance\t\t  age\t\t  profession\t\t phone_no \t\t ")
               for i in data:
                  print (data [0][0],'\t\t',data[0][1],'\t\t',data[0][2],'\t\t',data [0][3],'\t\t',data[0][4],'\t\t',data[0][5],'\t\t',data[0][6],'\t\t')
                  c=input('do you want to continue (y/[n]:)')
                  if c =='y' :
                       continue
                  else:
                         print('THANK  YOU  FOR  VISITING  OUR   WEBSITE' )
                         print('VISIT  AGAIN')
               print('=========================')
          if choice==4:
               appearence=(input('Enter the appearence:'))
               c1.execute("select* from girls_details where appearence='{}'". format(appearence))
               data= c1.fetchall()
               print("name\t\t address\t\t caste\t\t  appreance\t\t  age\t\t  profession\t\t phone_no \t\t ")
               for i in data:
                  print (data [0][0],'\t\t',data[0][1],'\t\t',data[0][2],'\t\t',data [0][3],'\t\t',data[0][4],'\t\t',data[0][5],'\t\t',data[0][6],'\t\t')
                  c=input('do you want to continue (y/[n]:)')
                  if c =='y' :
                       continue
                  else:
                         print('THANK  YOU  FOR  VISITING  OUR   WEBSITE' )
                         print('VISIT  AGAIN')
