import sys
from tabulate import tabulate
import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='mukul')
cur=conn.cursor()
#print(cur)     check for sql connection
cur.execute("show databases")
if not("library",)in cur.fetchall():
    cur.execute("create database library")
cur.execute("use library")
def see():
    cur.execute("select * from admin1")
    o=cur.fetchall()
    print(tabulate(o,headers=[ 'BOOK_ID' , 'Title' , 'Issued_To' ,'Issue_date'],tablefmt='grid'))
def issue():
    print('            HERE IS THE LIST OF THE BOOKS FOR YOU !!')
    print("       DO NOT ISSUE THAT BOOK WHOSE QUANTITY IS EQUAL TO '0' !!")
    cur.execute("select * from books")
    r11=cur.fetchall()
    print(tabulate(r11,headers=[ 'BOOK_ID' , 'BOOK_NAME','QTY'],tablefmt='grid'))
    r=int(input('Enter the Book Id :'))
    s=input('Enter the Book name :')
    v=input('Enter the name of student who issued this book :')
    t=input('Enter the issue date :')
    w="insert into admin1 values({},'{}','{}','{}')".format(r,s,v,t)
    cur.execute(w)
    conn.commit()
    print('YOUR TABLE AFTER ISSUING OF BOOKS')
    cur.execute("select * from admin1")
    x=cur.fetchall()
    print(tabulate(x,headers=[ 'BOOK_ID' , 'Title'  ,'Issued_To' ,'Issue_date'],tablefmt='grid'))
    p11="update books set QTY=QTY-1 where BOOK_ID={}".format(r)
    cur.execute(p11)
    conn.commit()
def returns():
    y=int(input('Enter the BOOK_ID of that book which the student want to return :'))
    z="(select * from admin1 where BOOK_ID={})".format(y)
    cur.execute(z)
    a2=cur.fetchall()
    print(tabulate(a2,headers=['BOOK_ID' , 'Title' ,'Issued_To' ,'Issue_date' ],tablefmt='grid'))
    b2=input('Do the student really want to return this book ?Y/N').lower()
    if b2=='y' or b2=='yes':
        c2="delete from admin1 where BOOK_ID={}".format(y)
        cur.execute(c2)
        conn.commit()
        print('YOUR TABLE AFTER RETURNING A BOOK  :')           
        cur.execute("select * from admin1")
        e2=cur.fetchall()
        print(tabulate(e2,headers=[ 'BOOK_ID' , 'Title'  ,'Issued_To' ,'Issue_date' ],tablefmt='grid'))
        o11="update books set QTY=QTY+1 where BOOK_ID={}".format(y)
        cur.execute(o11)
        conn.commit()
    else:
        print('YOUR TABLE WITHOUT RETUNING THE BOOK:')
        cur.execute("select * from admin1")
        f2=cur.fetchall()
        print(tabulate(f2,headers=[ 'BOOK_ID' , 'Title' ,  'Issued_To' ,'Issue_date' ],tablefmt='grid'))
        print('ITS OK!! YOUR BOOK HAS NOT BEEN RETURNED ')
def modify():
    print('BOOK_ID' ,'/', 'Title' ,'/','Issued_To' ,'/','Issue_date' )
    g2=input("Enter the attribute name in which you want to make the changes:")
    if g2=='BOOK_ID':
        h2=int(input('Enter the BOOK ID that you want to update :'))
        i2=int(input('Enter the OLD BOOK ID :'))
        j2="update admin1 set BOOK_ID={} where BOOK_ID={}".format(h2,i2)
        cur.execute(j)
        conn.commit()
        print('YOUR TABLE AFTER MODIFICATION :')
        k2="select * from admin1"
        cur.execute(k2)
        l2=cur.fetchall()
        print(tabulate(l2,headers=['BOOK_ID' , 'Title' , 'Author' ,'Issued_To' ,'Issue_date' ],tablefmt='grid'))
    else:
        m2=input('Enter the value that you want to update :')
        n2=int(input('Enter the BOOK ID to which you want to make your updation:'))
        o2="update admin1 set {}='{}' where BOOK_ID={}".format(g2,m2,n2)
        cur.execute(o2)
        conn.commit()
        print('YOUR TABLE AFTER MODIFICATION :')
        p2="select * from admin1"
        cur.execute(p2)
        q2=cur.fetchall()
        print(tabulate(q2,headers=['BOOK_ID' , 'Title'  ,'Issued_To' ,'Issue_date'],tablefmt='grid'))
def avail():
    cur.execute("select * from books")
    r2=cur.fetchall()
    print(tabulate(r2,headers=[ 'BOOK_ID' , 'BOOK_NAME','QTY'],tablefmt='grid'))
def delete():
    s2=int(input('Enter the BOOK_ID of that book which you want to delete from the list :'))
    t2="(select * from books where BOOK_ID={})".format(s2)
    cur.execute(t2)
    u2=cur.fetchall()
    print(tabulate(u2,headers=['BOOK_ID' , 'BOOK_NAME','QTY' ],tablefmt='grid'))
    v2=input('Do the student really want to return this book ?Y/N').lower()
    if v2=='y' or v2=='yes':
        w2="delete from books where BOOK_ID={}".format(s2)
        cur.execute(w2)
        conn.commit()
        print('YOUR TABLE AFTER DELETION ')           
        cur.execute("select * from books")
        x2=cur.fetchall()
        print(tabulate(x2,headers=[  'BOOK_ID' , 'BOOK_NAME','QTY'],tablefmt='grid'))      
    else:
        print('YOUR TABLE WITHOUT DELETION')
        cur.execute("select * from books")
        y2=cur.fetchall()
        print(tabulate(y2,headers=[ 'BOOK_ID' , 'BOOK_NAME','QTY' ],tablefmt='grid'))
        print('ITS OK!! YOUR DELETION OF BOOK IS NOT DONE. ')
def logout():
    print('YOUR PORTAL IS LOGGED OUT')
    print('HAVE A NICE DAY !!')
    sys.exit()
def see1(z2):
    cur.execute("select * from {}".format(z2))
    a1=cur.fetchall()
    print(tabulate(a1,headers=[' BOOK_ID', 'BOOK_NAME' ,'ISSUE_DATE' ],tablefmt='grid'))
def issue1(k1):
    print('            HERE IS THE LIST OF THE BOOKS FOR YOU !!')
    print("       DO NOT ISSUE THAT BOOK WHOSE QUANTITY IS EQUAL TO '0' !!")
    cur.execute("select * from books")
    t11=cur.fetchall()
    print(tabulate(t11,headers=[ 'BOOK_ID' , 'BOOK_NAME','QTY'],tablefmt='grid'))
    f1=int(input('Enter the Book Id :'))
    g1=input('Enter the Book name :')
    h1=input('Enter the issue date :')
    i1="insert into {} values({},'{}','{}')".format(k1,f1,g1,h1)
    cur.execute(i1)
    conn.commit()
    a18="insert into admin1 values({},'{}','{}','{}')".format(f1,g1,k1,h1)
    cur.execute(a18)
    conn.commit()
    print('YOUR TABLE AFTER ISSUING OF BOOKS ')
    cur.execute("select * from {}".format(k1))
    j1=cur.fetchall()
    print(tabulate(j1,headers=[' BOOK_ID', 'BOOK_NAME' ,'ISSUE_DATE' ],tablefmt='grid'))   
    s11="update books set QTY=QTY-1 where BOOK_ID={}".format(f1)
    cur.execute(s11)
    conn.commit()
def return1(l1):
    m1=int(input('Enter the BOOK_ID of that book which you want to return :'))
    n1="(select * from {} where BOOK_ID={})".format(l1,m1)
    cur.execute(n1)
    o1=cur.fetchall()
    print(tabulate(o1,headers=[' BOOK_ID', 'BOOK_NAME' ,'ISSUE_DATE' ],tablefmt='grid'))
    p1=input('Do you really want to return this book ?Y/N').lower()
    if p1=='y' or p1=='yes':
        q1="delete from {} where BOOK_ID={}".format(l1,m1)
        cur.execute(q1)
        conn.commit()
        c12="delete from admin1 where BOOK_ID={}".format(m1)
        cur.execute(c12)
        conn.commit()
        print('YOUR TABLE AFTER RETURNING A BOOK  :')           
        cur.execute("select * from {}".format(l1))
        r1=cur.fetchall()
        print(tabulate(r1,headers=[' BOOK_ID', 'BOOK_NAME' ,'ISSUE_DATE' ],tablefmt='grid'))
        u11="update books set QTY=QTY+1 where BOOK_ID={}".format(m1)
        cur.execute(u11) 
        conn.commit()
    else:
        print('YOUR TABLE WITHOUT RETUNING THE BOOK:')
        cur.execute("select * from {}".format(l1))
        s1=cur.fetchall()
        print(tabulate(s1,headers=[' BOOK_ID', 'BOOK_NAME' ,'ISSUE_DATE' ],tablefmt='grid'))
        print('ITS OK!! YOUR BOOK HAS NOT BEEN RETURNED ')
def logout1(m20):
    print('YOUR PORTAL IS LOGGED OUT')
    print('HAVE A NICE DAY !!')
    sys.exit()
def signup(a15):
    k=input('PLEASE ENTER THE PASSWORD THAT YOU WANT TO SET :')
    for m in range(3):
        l=input('PLEASE CONFIRM YOUR PASSWORD:')
        if l==k:
            print('ACCOUNT CREATED SUCCESFULLY')
            d1[a15]=l
            break
        else:
            print('PASSWORD  mentioned is incorrect')
            if m<2:print('Try Again')
            else:
                print('THE PASSWORD YOU ARE GIVING DOES NOT MATCH WITH THE PASSWORD YOU HAVE SET .')
                print('AGAIN CREATE YOUR NEW PASSWORD')
                a11=input('DO YOU WANT TO CREATE YOUR NEW PASSWORD ?').lower()
                if a11=='y' or a11=='yes':
                    signup(j)
                else:
                    print('HAVE A NICE DAY!!')
                    sys.exit()
d1={'dev':'dev@','amit':'amit@','arpit':'arpit@'}
print('***************************** WELCOME TO LIBRARY MANAGEMENT *****************************')
a=input('ARE YOU ADMIN OR STUDENT ? ').lower()
a5='y'
while a5=='y':
    if a=='admin':
        print('                            WELCOME TO YOUR PORTAL')
        print('             TYPE 1 TO SEE NO OF BOOKS THAT HAVE BEEN ISSUED BY THE STUDENTS ')
        print('                      TYPE 2 ISSUING OF A BOOK BY THE STUDENT ')
        print('                      TYPE 3 RETURNING OF BOOK BY THE STUDENT ')
        print('                      TYPE 4 TO DO SOME MODIFICATION IN THE TABLE')
        print('                      TYPE 5 TO CHECK THE AVAILIBLITY OF BOOKS ')
        print('                TYPE 6 TO DELETE THAT BOOK RECORD WHICH IS NOT IN THE STOCK')
        print('                      TYPE 7 TO TAKE LOGOUT FROM YOUR SYSTEM')
        d={1:see,2:issue,3:returns,4:modify,5:avail,6:delete,7:logout}
        b=int(input('PLEASE ENTER YOUR CHOICE:'))
        d[b]()
    elif a=='student':
        c=input('DO YOU WANT TO LOGIN OR SIGNUP YOUR ACCOUNT ? ').lower()
        if c=='login':
            e=input('PLEASE ENTER YOUR NAME :')
            if e in d1.keys():
                for f in range(3):
                    g=input('PLEASE ENTER YOUR PASSWORD:')
                    if g==d1[e]:
                        print('You have logged in your account')
                        break
                    else:
                        print('PASSWORD  mentioned is incorrect')
                        if f<2:print('Try Again')
                        else:
                            print('You must have forgotten your password .')
                            print('GO TO SIGN UP AND MAKE YOUR NEW ACCOUNT.')
                            print('HAVE A NICE DAY!!')
                            sys.exit()
                while True:
                    print('                     WELCOME TO YOUR PORTAL')           
                    print('          TYPE 1 TO SEE HOW MANY BOOKS YOU HAVE ISSUED TILL NOW ')
                    print('                   TYPE 2 ISSUING A BOOK')
                    print('                   TYPE 3 RETURNING OF BOOK ')
                    print('                   TYPE  4 TO LOGOUT ')
                    d2={1:see1,2:issue1,3:return1,4:logout1}
                    i=int(input('PLEASE ENTER YOUR CHOICE:'))
                    d2[i](e)
                    choice=input('DO YOU WANT TO RETURN TO YOUR MENU ?')
                    if choice in'Nn':
                        break
            else:
                print('YOU ARE NOT THE EXISITING USER')
                print('GO TO SIGN UP AND CREATE YOUR NEW ACCOUNT')
        else:
            j=input('PLEASE ENTER YOUR NAME :')
            signup(j)       
            cur.execute("show tables")
            if not(j,)in cur.fetchall():      
                cur.execute("create table {}(BOOK_ID INT PRIMARY KEY,BOOK_NAME VARCHAR(255),ISSUE_DATE DATE)".format(j))
            while True:
                print('                      WELCOME TO YOUR PORTAL')           
                print('              TYPE 1 TO SEE HOW MANY BOOKS YOU HAVE ISSUED TILL NOW ')
                print('                      TYPE 2 ISSUING A BOOK')
                print('                      TYPE 3 RETURNING OF BOOK ')
                print('                         TYPE 4 TO LOGOUT ')
                d2={1:see1,2:issue1,3:return1,4:logout1}
                a12=int(input('PLEASE ENTER YOUR CHOICE :'))
                d2[a12](j)
                choice1=input('DO YOU WANT TO RETURN TO YOUR MENU ?')
                if choice1 in'Nn':
                    break    
    else:
        print('OUT OF CHOICE !!')
    a5=input('DO YOU WANT TO CONTINUE ?')