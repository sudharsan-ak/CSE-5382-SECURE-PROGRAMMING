import os
import csv
from datetime import datetime
import re
import time
from datetime import datetime
import platform


# Regex for phone numbers
p1 = '^\\d{1}\\(\\d{3}\\)\\d{3}-\\d{4}$'
p2 = '^\\d{3}\\s\\d{1}\\s\\d{3}\\s\\d{3}\\s\\d{4}$'
p3 = '^\\(\\d{3}\\)\\d{3}-\\d{4}$'
p4 = '^\\+\\d{2}\\s\\(\\d{2}\\)\\s\\d{3}-\\d{4}$'
p5 = '^\\+\\d\\(\\d{3}\\)\\d{3}\\-\\d{4}$'
p6 = '^\\d{5}.\\d{5}$'
p7 = '^\\d{3}-\\d{4}$'
p8 = '^\\d{3}\\s\\d{1}\\s\\d{3}\\s\\d{3}\\s\\d{4}$'
p9 = '^\\d{5}$'
p10 = '^\\d{3}\\s\\d{3}\\s\\d{3}\\s\\d{4}$'

# Regex for names
n1 ='^[a-zA-Z]+(((\'|-|.)?([a-zA-Z])+))?$'
n2 ='^[a-zA-Z]+(((\\,(\\s)|-|.)?([a-zA-Z])+))+((\\s)?([a-zA-Z])+)*$'
n3= '^[a-zA-Z]+((\\s)?([a-zA-Z])+)*$'
n4 ='^([a-zA-Z])+$'
n5 ='^[^\s]+,?(\s[^\s]+)*$'
n6='^[a-zA-Z]+(((\\,(\\s)|-|.)?([a-zA-Z])+))*$'
n7 ='^[a-zA-Z]+((\\s)?((\'|-|.)?([a-zA-Z])+))*$'

# lists and variables for data processing
list1 = []
np = 0
pp = 1
headers = ['Name', 'Phone Number']



def display():
    try:
        display2(headers, "")
        j = 1
        for i in list1:
            display2 (i, j)
            j+=1
        print()
        try:
            log2()
        except:
            print("")
            main()

    except:
        print("Error Displaying Data")

def load():
    try:
        if os.access("records.csv", os.F_OK):
            f = open("records.csv")
            for r in csv.reader(f):
                list1.append(r)
            f.close()
    except:
        print("Error Loading Data")

def is_root():
    return os.geteuid() == 0

def delete(number):

    try:
        j = 0
        f=0
        for i in list1:
            if i[pp] == number:
                print("Deleting Record....")
                f=1
                j+=1
            else:
                j+=1
        if f==0 :
            print("Record does not exist in the database")
            exit(1)
        del list1[j]
        print("Deleting.;......")
        print("Record Deleted Number : ", number)
        save_list()
    except:
        print("")

def create():
    try:
        print("Enter Details For A New Record")
        nn = input("Enter Name: ")
        check_name(nn)
        nnp = input("Enter phone number: ")
        check_phone_no(nnp)
        phone = [nn, nnp]
        list1.append(phone)
        if (platform.system().lower() != 'windows'):
            try:
                log(nn)
            except:

                print('')
                exit()
    except:
        print("Error Input")

def delete2(name):
    try:
        j=0
        f=0
        for i in list1:
            if i[np]==name:
                print("Deleting...")
                f=1
                j+=1
            else:
                j+=1
        if f==0 :
            print ("Record does not exist")
            exit(1)
        del list1[j-1]
        print("Record Deleted- Name : ", name)
        save_list()

        if (platform.system().lower() != 'windows'):
            try:
                log(name)
            except:

                print('')
                exit()

    except:
        print("Error Deleting Data")



def save_list():
    try:
        f = open ("records.csv", 'w', newline='')
        for i in list1:
            csv.writer (f).writerow (i)
        f.close ()
    except:
        print("Error Saving Data")

def choice(n):
    try:
        if not n.isdigit():
            print("please enter a valid option")
            return False
        no = int(n)
        return True
    except:
        print("Error in entering choice")


def display2(phone, index):
    try:
        outputstr = "{0:>3}  {1:<20}  {2:>16}"
        print (outputstr.format (index, phone[np], phone[pp]))
    except:
        print("Error Displaying Data")


def log(name):
    t1 = datetime.now()
    ruid = os.getuid()
    try:
        if(is_root()):
            f = open("log.txt", "a")
            f.write("\nRUID: " + str(ruid) + ' ' + 'Name: ' + name + ' ' + "Time-Stamp: " + str(t1))
            f.close()
        else:
            print("Cannot write to log, Not a root user")
            main()
    except:
        print("")

def log2():
    ruid=os.getuid()
    t2=datetime.now()
    try:
        if(is_root()):
            f = open("log.txt", "a")
            f.write("\nRUID: " + str(ruid) + ' ' + "Time-Stamp: " + str(t2))
            f.close()
        else:
            print("Cannot write to log, Not a root user")
            main()
    except:
        print("")

def check_name(name):
    try:

        if (re.search ( n1,name)):
            print("\nName Accepted")
        elif (re.search( n2,name)):
            print ("\nName Accepted")
        elif (re.search( n3,name)):
            print ("\nName Accepted")
        elif (re.search(n4,name)):
            print ("\nName Accepted")
        elif (re.search(n5,name )):
            print ("\nName Accepted")
        elif (re.search(n6,name)):
            print ("\nName Accepted")
        elif (re.search(n7,name)):
            print ("\nName Accepted")
        else:
            print("\nName Rejected, Enter it in correct format")
            exit(1)
    except:
        print("Error in regular expression search")

def check_phone_no(phone):
    try:

        if (re.search ( p1,phone)):
            print("\nPhone Accepted")
        elif (re.search( p2,phone)):
            print ("\nPhone Accepted")
        elif (re.search( p3,phone)):
            print ("\nPhone Accepted")
        elif (re.search( p4, phone)):
            print ("\nPhone Accepted")
        elif (re.search( p5,phone)):
            print ("\nPhone Accepted")
        elif (re.search( p6,phone)):
            print ("\nPhone Accepted")
        elif (re.search( p7,phone)):
            print ("\nPhone Accepted")
        elif (re.search (p8, phone)):
            print ("\nPhone Accepted")
        elif (re.search (p9, phone)):
            print ("\nPhone Accepted")
        elif (re.search (p10, phone)):
            print ("\nPhone Accepted")
        else:
            print("\nPhone Rejected, Enter it in correct format")
            exit(1)
    except:
        print("Error in regular expression search")

def menu():
    try:
        print ("........Options.........")
        print ("\nList-L")
        print ("\nAdd-A")
        print("\nDelete using Name-DN")
        print ("\nDelete using Phone Number-DP")
        print ("\nExit-E")
        print("\nchoices are case sensitive")
        choice = input("Choice: ")
        if choice.upper() in ['A', 'DN', 'L', 'DP', 'E']:
            return choice.upper()
        else:

            print("Invalid Choice,Enter correct choice")
            return None
    except:
        print("Error in main menu")
        exit(1)


def main():
    try:
        load()

        while True:
            choice = menu()
            if choice == None:
                continue
            if choice == 'E':
                print("Exiting...")
                exit()

            elif choice == 'A':
                create()
            elif choice == 'DP':
                num = input ("Enter The Phone Number Of The Record You Want To Delete ")
                print("Phone number : ", num)
                delete(num)
            elif choice == 'L':
                display()
            elif choice == 'DN':
                num = input ("Enter The Name Of The Record You Want To Delete ")
                print("Name : ", num)
                delete2(num)
            else:
                print("Invalid choice.")



        save_list ()
    except:
        print("")
        exit()



if __name__ == '__main__':
    main()