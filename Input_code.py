# create table books
'''a="create table books( BOOK_ID INT PRIMARY KEY , BOOK_NAME VARCHAR(255), QTY INT)"
cur.execute(a)'''
# add book records in table book
l=int(input('Enter the Book Id :'))
m=input('Enter the BOOK NAME :')
n=int(input('Enter the Quantity available :'))
q="insert into books values({},'{}',{})".format(l,m,n)
cur.execute(q)
conn.commit()
#create table admin1
y="CREATE TABLE ADMIN1( BOOK_ID INT PRIMARY KEY, Title VARCHAR(255), Issued_To VARCHAR(255),Issue_date date)"
cur.execute(y)
# insert records into admin1
b=int(input('Enter the Book Id :'))
c=input('Enter the title of the Book :')
e=input('Enter the name of the person to whom issued:')
f=input('Enter the issue date :')
g="insert into ADMIN1 values({},'{}','{}','{}')".format(b,c,e,f)
cur.execute(g)
conn.commit()
# create table arpit
y="CREATE TABLE arpit( BOOK_ID INT PRIMARY KEY, BOOK_NAME VARCHAR(255), ISSUE_DATE date)"
cur.execute(y)
# add data in table - arpit 
y2=int(input('Enter the Book Id :'))
z2=input('Enter the Book name :')
a3=input('Enter the issue date :')
b3="insert into arpit values({},'{}','{}')".format(y2,z2,a3)
cur.execute(b3)
conn.commit()
# create table dev
y="CREATE TABLE dev( BOOK_ID INT PRIMARY KEY, BOOK_NAME VARCHAR(255), ISSUE_DATE date)"
cur.execute(y)
# add data in table - dev
y2=int(input('Enter the Book Id :'))
z2=input('Enter the Book name :')
a3=input('Enter the issue date :')
b3="insert into dev values({},'{}','{}')".format(y2,z2,a3)
cur.execute(b3)
conn.commit()
# create table amit
y="CREATE TABLE amit( BOOK_ID INT PRIMARY KEY, BOOK_NAME VARCHAR(255), ISSUE_DATE date)"
cur.execute(y)
# add data in table - amit
y2=int(input('Enter the Book Id :'))
z2=input('Enter the Book name :')
a3=input('Enter the issue date :')
b3="insert into amit values({},'{}','{}')".format(y2,z2,a3)
cur.execute(b3)
conn.commit()