import mysql.connector

mydb = mysql.connector.connect(user = 'root',
                               passwd = 'root123',
                               host = 'localhost',
                               auth_plugin = 'mysql_native_password',
                               database = 'BankDB')
#Created Database BankDB
#mycursor.execute('create databese BankDB')
mycursor = mydb.cursor()

b = 5
#Function to display the menu
def Menu():
    print("Main Menu".rjust(b, " "))
    print("1. Insert Record/Records".rjust(b, " "))
    print("2. Display Records as per Account Number".rjust(b, " "))
    print("     a. Sorted as per Account Number".rjust(b, " "))
    print("     b. Sorted as per Customer Balance".rjust(b, " "))
    print("3. Update Record".rjust(b, " "))
    print("4. Delete Record".rjust(b, " "))
    print("5. Transactions Debt/Withdraw from the account".rjust(b, " "))
    print("     a. Debit/Withdraw from the account".rjust(b, " "))
    print("     b. Credit  into the the account".rjust(b, " "))
    print("6. Exit".rjust(b, " "))

def MenuSort():
    print("     a. Sorted as per Account Number".rjust(b, " "))
    print("     b. Sorted as per Customer Name".rjust(b, " "))
    print("     c. Sorted as per Customer Balance".rjust(b, " "))
    print("     d. Back".rjust(b, " "))

def MenuTransaction():
    print("     a. Debit/Withdraw from the account".rjust(b, " "))
    print("     b. Credit into the account".rjust(b, " "))
    print("     c. Back".rjust(b, " "))

def Create():
    try:
         mycursor.execute("create table bank(ACCNO varchar(10), NAME varchar(20), Mobile varchar(10), Email varchar(20), ADDRESS varchar(20)")
         print("Table Created")
         Insert()
    except:
         print("Table Exit")
         Insert()

def Insert():
    #Loop for accepting records
    while True:
        Acc = input("Enter Account No.")
        Name = input("Enter Name")
        Mob = input("Enter Mobile No.")
        email = input("Enter Email")
        Add = input("Enter Address")
        City = input("Enter City")
        Country = input("Enter Country")
        Bal = float(input("Enter Balance"))
        Rec = [Acc, Name.upper(), Mob, email.upper(), Add.upper(), City.upper(), Country.upper(), Bal]
        Cmd = "insert into BANK values(%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(Cmd, Rec)
        mydb.commit()
        ch = input("Do you want to enter more records")
        if ch == 'N' or ch == 'n':
            break
#Function to Display records as per ascending order of Account Number
def DispSortAcc():
    try:
        cmd = "select * from BANK order by ACCINO"
        mycursor.execute(cmd)
        F = "%15s %15s %15s %15s %15s %15s %15s %15s"
        print(F%("ACCNO", "NAME", "MOBILE", "EMAIL ADDRESS", "COMPLETE ADDRESS", "CITY", "COUNTRY", "BALANCE"))
        print()
        for i in mycursor:
            for j in i:
                print("%14s" %j, end=" ")
            print()
        print()
    except:
        print("Table doesn't exist")

def DispSortBal():
    try:
        cmd = "select * from BANK"
        mycursor.execute(cmd)
        ch = input("Enter the account no to be searched")
        for i in mycursor:
            if i[0] == ch:
                print()
                F = "%15s %15s %15s %15s %15s %15s %15s %15s"
                print(F % ("ACCNO", "NAME", "MOBILE", "EMAIL ADDRESS", "COMPLETE ADDRESS", "CITY", "COUNTRY", "BALANCE"))
                print()
                for j in i:
                    print("%14s" %j,end=" ")
                print()
                break
            else:
                print("Record Not Found")
    except:
        print("Table doesn't exist")

#Function to change the details of a customer
def Update():
    try:
        cmd = "select * from BANK"
        mycursor.execute(cmd)
        A = input("Enter the account no whose details to be changed")
        for i in mycursor:
            i = list(i)
            if i[0] == A:
                ch = input("Change Name(Y/N)")
                if ch == 'Y' or ch == 'y':
                    i[1] = input("Enter Name")
                    i[1] = i[1].upper()

                ch = input("Change Mobile(Y/N)")
                if ch == 'Y' or ch == 'y':
                    i[2] = input("Enter Mobile")

                ch = input("Change Email(Y/N)")
                if ch == 'Y' or ch == 'y':
                    i[3] = input("Enter email")
                    i[3] = i[3].upper()

                ch = input("Change Address(Y/N)")
                if ch == 'Y' or ch == 'y':
                    i[4] = input("Enter Address")
                    i[4] = i[4].upper()

                ch = input("Change City(Y/N)")
                if ch == 'Y' or ch == 'y':
                    i[5] = input("Enter City")
                    i[5] = i[5].upper()

                ch = input("Change Country(Y/N)")
                if ch == 'Y' or ch == 'y':
                    i[6] = input("Enter Country")
                    i[6] = i[6].upper()

                ch = input("Change Balance(Y/N)")
                if ch == 'Y' or ch == 'y':
                    i[7] = float(input("Enter Balance"))
                cmd = "UPDATE BANK SET NAME = %s, MOBILE = %s, EMAIL = %s, ADDRESS = %s, CITY = %s, COUNTRY = %s, BALANCE = %s WHERE ACCNO = %s"
                val = (i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[0])
                mycursor.execute(cmd, val)
                mydb.commit()
                print("Account Updated")
                break
        else:
            print("Record not found")
    except:
        print("No such table")

#function to delete the details of the customer
def Delete():
    try:
        cmd = "select * from BANK"
        mycursor.execute(cmd)
        A = input("Enter the account no whose details to be changed")
        for i in mycursor:
            i = list(i)
            if i[0]==A:
                cmd = "delete from bank where accno = %s"
                val = (i[0])
                mycursor.execute(cmd, val)
                mydb.commit()
                print("Account Deleted")
                break
        else:
            print("Record not found")
    except:
        print("No such Table")

#function to Withdraw the amount by assuring the min balance of Rs 5000
def Debit():
    try:
        cmd = "select * from BANK"
        mycursor.execute(cmd)
        print("Please Note that the money can only be debited if min balance of Rs 5000 exists")
        acc = input("Enter the account np from which the money is to be debited")
        for i in mycursor:
            i = list(i)
            if i[0] == acc:
                Amt = float(input("Enter the amount to be withdraw"))
                if i[7]-Amt>=5000:
                    i[7] -= Amt
                    cmd = "UPDATE BANK SET BALANCE = %s WHERE ACCNO = %s"
                    val = (i[7], i[0])
                    mycursor.execute(cmd, val)
                    mydb.commit()
                    print("Amount Debited")
                    break
                else:
                    print("There must be min balance of Rs 5000")
                    break
            else:
                print("Record not Found")
    except:
        print("Table doesn't exist")

#function to Withdraw the amount by assuring the min balance of Rs 5000
def Credit():
    try:
        cmd = "select * from BANK"
        mycursor.execute(cmd)
        S = mycursor.fetchall()
        acc = input("Enter the account np from which the money is to be credited")
        for i in S:
            i = list(i)
            if i[0] == acc:
                Amt = float(input("Enter the amount to be credited"))
                i[7]+=Amt
                cmd = "UPDATE BANK SET BALANCE = %s WHERE ACCNO = %s"
                val = (i[7], i[0])
                mycursor.execute(cmd, val)
                mydb.commit()
                print("Amount Credited")
                break
            else:
                print("Record not found")
    except:
        print("Table doesn't exist")
while True:
    Menu()
    ch = input("Enter your choice")
    if ch == "1":
        Create()
    elif ch == "2":
        while True:
            MenuSort()
            ch1 = input("Enter choie a/b/c/d")
            if ch1 in ['a', 'A']:
                DispSortAcc()
            elif ch1 in ['b', 'B']:
                DispSortBal()
            elif ch1 in ['c', 'C']:
                print("Back to main menu")
                break
            else:
                print("Invalid choice")
    elif ch == "3":
        Update()
    elif ch == "4":
        Delete()
    elif ch == "5":
        while True:
            MenuTransaction()
            ch1 = input("Enter choice a/b/c")
            if ch1 in ['a', 'A']:
                Debit()
            elif ch1 in ['b', 'B']:
                Credit()
            elif ch1 in ['c', 'C']:
                print("Back to the main Menu")
                break
            else:
                print("Invalid Choice")
    elif ch == "6":
        print("Exiting...")
    else:
        print("Wrong Choice Entered")


