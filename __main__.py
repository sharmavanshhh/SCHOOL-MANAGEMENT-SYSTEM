#Update database and passwd details before runnnig.....
import mysql.connector.con = mysql.connector.connect(host = 'localhost', user = 'root', database = %s , passwd = %s)

def addst () :
    c = con.cursor()
    s = 'create table if not exists student(Name char(20),Class int,Roll_No int, Address varchar(50),Contact bigint)'
    c.execute(s)
    n = input("Student Name : ")
    cl = input("Class : ")
    r = int(input("Roll No. : "))
    a = input("Address : ")
    ph = int(input("Phone No. : "))
    data = (n, cl, r, a, ph)
    c = con.cursor()
    sql = 'INSERT INTO student(Name,Class,Roll_No, Address,Contact) VALUES(%s, %s, %s, %s, %s)'
    c.execute(sql,data)
    con.commit()
    print("Data Entered Successfully !! ")
    print(" ")
    main()

def removest() :
    cl = int(input("Class : "))
    r = int(input("Roll No. : "))
    data = (cl,r)
    sql = 'delete from student where Class=%s and Roll_no=%s'
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Updated Successfully !! ")
    print(" ")
    main()

def displayst() :
    cl = input("Class : ")
    data = (cl,)
    sql = 'select * from student where class = %s'
    c = con.cursor()
    c.execute(sql,data)
    d = c.fetchall()
    print(" ")
    print("(Name,Class,Roll_No,Address,Contact)")
    for i in d :
        print(i)
    print(" ")
    main()

def addt() :
    c = con.cursor()
    s = 'create table if not exists teacher(t_code int,Name char(20), Salary int, Address varchar(50),Contact bigint)'
    c.execute(s)
    tcode = int(input("TCode : "))
    n = input("Teacher Name : ")
    s = int(input("Salary : "))
    a = input("Address : ")
    ph = input("Phone : ")
    data = (tcode,n,s,a,ph)
    c = con.cursor()
    sql = 'insert into teacher(t_code,Name,Salary, Address,Contact) values (%s, %s, %s, %s, %s)'
    c.execute(sql,data)
    con.commit()
    print("Data Entered Successfully !! ")
    print(" ")
    main()

def removet() :
    n = input("Teacher Name : ")
    tcode = int(input("TCode : "))
    data = (n,tcode)
    sql = 'delete from teacher where Name=%s and t_code=%s'
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Updated Successfully !! ")
    print(" ")
    main()

def updatesal() :
    tcode = int(input("TCode : "))
    sal = int(input("New Salary :  "))
    data = (sal,tcode)
    sql = 'update teacher set salary=%s where t_code=%s'
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Updated Successfully !! ")
    print(" ")
    main()

def displayt() :
    sql = 'select * from teacher'
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    print(" ")
    print("(t_code, Name, Salary, Address, Contact)")
    for i in d :
        print(i)
    print(" ")
    c = con.cursor()
    c.execute(sql)
    print(" ")
    main()

def clattd() :
    c = con.cursor()
    s = 'create table if not exists clattendance(Class int,Teacher char(20),Strength int,Date char(10),Absentees int)'
    c.execute(s)
    a = input("Class : ")
    clt = input("Class Teacher : ")
    t = int(input("Class Strength : "))
    d = input("Date : ")
    ab = int(input("No. of Absentees : "))
    data = (a,clt,t,d,ab)
    sql = 'insert into clattendance(Class,Teacher,Strength,Date,Absentees)  values (%s, %s, %s, %s, %s)'
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Entered Successfully !! ")
    print(" ")
    main()

def displayclattd():
    sql = 'select * from clattendance'
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    print(" ")
    print("(Class,Teacher,Strength,Date,Absentees)")
    for i in d :
        print(i)
    print(" ")
    main()

def tattd() :
    c = con.cursor()
    s = 'create table if not exists tattendance(Name char(20),Date char(10),Status char(10))'
    c.execute(s)
    n = input("Name : ")
    d = input("Date : ")
    a = input("Attendence : ")
    data = (n,d,a)
    sql = 'insert into tattendance(Name,Date,Status) value(%s, %s, %s)'
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Entered Successfully")
    print(" ")
    main()

def displaytattd() :
    sql = 'select * from tattendance'
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    print(" ")
    print("(Name,Date,Status)")
    for i in d :
        print(i)
    print(" ")
    main()

def addfees() :
    c = con.cursor()
    s = 'create table if not exists feestructure(Class int null,Monthly int null,BusFee int null,ScFee int null,TechFee int null,Total int null)'
    c.execute(s)
    cl = int(input("Class : "))
    m = int(input("Monthly : "))
    b = int(input("BusFee : "))
    sc = int(input("ScFee : "))
    tc = int(input("TechFee : "))
    t = m + b + sc + tc
    _dat = (cl,m,b,sc,tc,t)
    _sql = 'insert into feestructure(Class,Monthly,BusFee,ScFee,TechFee,Total) values(%s,%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(_sql,_dat)
    con.commit()
    print("Data Updated !! ")
    print(" ")
    main()

def updatefees() :
    c = con.cursor()
    s = 'create table if not exists feestructure(Class int null,Monthly int null,BusFee int null,ScFee int null,TechFee int null,Total int null)'
    c.execute(s)
    cl = int(input("Class : "))
    m = int(input("Monthly : "))
    b = int(input("BusFee : "))
    sc = int(input("ScFee : "))
    tc = int(input("TechFee : "))
    t = m + b + sc + tc
    _dat = (cl,)
    data = (m,b,sc,tc,t,cl)
    sql = 'update feestructure set Monthly=%s, BusFee=%s, ScFee=%s, TechFee=%s, Total=%s where class=%s'
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Updated !! ")
    print(" ")
    main()

def displayfees() :
    sql = 'select * from feestructure'
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    print(" ")
    print("(Class,Monthly,BusFee,ScFee,TechFee,Total)")
    for i in d :
        print(i)
    print(" ")
    main()

def addbook() :
    c = con.cursor()
    s = 'create table if not exists library(Book_ID varchar(20),Title varchar(200),Author char(20), Publisher char(20), Genre char(20))'
    c.execute(s)
    bid = (input("Book ID : "))
    t = input("Title : ")
    a = input("Author : ")
    p = input("Publisher : ")
    g = input("Genre : ")
    data = (bid,t,a,p,g)
    sql = 'insert into library(Book_ID,Title,Author,Publisher,Genre) values(%s, %s, %s, %s, %s)'
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Entered Successfully !! ")
    print(" ")
    main()

def removeb():
    t = input("Title : ")
    bid = int(input("Book ID : "))
    data = (t,bid)
    sql = 'delete from library where Title=%s and Book_ID=%s'
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Updated Successfully !! ")
    print(" ")
    main()

def displayb() :
    sql = 'select * from library'
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    print(" ")
    print("(Book_ID,Title,Author,Publisher,Genre)")
    for i in d :
        print(i)
    print(" ")
    main()

def main() :
    print("-----------------------------")
    print("SCHOOL MANAGEMENT SYSTEM")
    print("-----------------------------")
    print("~ P. R. PUBLIC SCHOOL ~ ")
    print("1. Student")
    print("2. Teacher")
    print("3. Class Attendance")
    print("4. Teacher Attendance")
    print("5. Fee Structure")
    print("6. Library")
    print("7. Exit")
    table = int(input("Enter Your Choice : "))
    print(" ")

    if table == 1 :
        op = 'y'
        while op in ['y', 'Y'] :
            print("1. Add Student")
            print("2. Remove Student")
            print("3. Display Student Details")
            task = int(input("Enter Your Choice : "))
            if task == 1 :
                addst()
            if task == 2 :
                removest()
            if task == 3 :
                displayst()
            else :
                print("Enter Valid Choice !! ")
            op = input("Continue? (y/n)")

    elif table == 2 :
        op = 'y'
        while op in ['y', 'Y'] :
            print("1. Add Teacher")
            print("2. Remove Teacher")
            print("3. Update Salary")
            print("4. Display Teachers Detalis")
            task = int(input("Enter Your Choice : "))
            if task == 1 :
                addt()
            elif task == 2 :
                removet()
            elif task == 3 :
                updatesal()
            elif task == 4 :
                displayt()
            else :
                print("Enter Valid Choice !! ")
            op = input("Continue? (y/n)")

    elif table == 3 :
        op = 'y'
        while op in ['y', 'Y'] :
            print("1. Class Attendance")
            print("2. Display Class Attendance Details")
            task = int(input("Enter Your Choice : "))
            if task == 1 :
                clattd()
            elif task == 2 :
                displayclattd()
            else :
                print("Enter Valid Choice !! ")
            op = input("Continue? (y/n)")

    elif table == 4 :
        op = 'y'
        while op in ['y', 'Y'] :
            print("1. Teachers Attendance")
            print("2. Display Teachers Attendance Details")
            task = int(input("Enter Your Choice : "))
            if task == 1 :
                tattd()
            elif task == 2 :
                displaytattd()
            else :
                print("Enter Valid Choice !! ")
            op = input("Continue? (y/n)")

    elif table == 5 :
        op = 'y'
        while op in ['y', 'Y'] :
            print("1. Add Fees Details")
            print("2. Update Fees Details")
            print("3. Display Fees Details")
            task = int(input("Enter Your Choice : "))
            if task == 1 :
                addfees()
            elif task == 2 :
                updatefees()
            elif task == 3 :
                displayfees()
            else :
                print("Enter Valid Choice !! ")
            op = input("Continue? (y/n)")

    elif table == 6 :
        op = 'y'
        while op in ['y', 'Y']:
            print("1. Add Book")
            print("2. Remove Book")
            print("3. Display Book")
            task = int(input("Enter Your Choice : "))
            if task == 1 :
                addbook()
            elif task == 2 :
                removeb()
            elif task == 3 :
                displayb()
            else :
                print("Enter Valid Choice !! ")
            op = input("continue? (y/n)")

    elif table == 7 :
        print("Thank You :) ")

    else :
        print("Enter Valid Choice !!")
        main()

main()




