import os
import csv
from datetime import datetime
import re
import time
from datetime import datetime
import platform


# Regex for phone numbers
phoneNumberF1 = '^\\d{1}\\(\\d{3}\\)\\d{3}-\\d{4}$'
phoneNumberF2 = '^\\d{3}\\s\\d{1}\\s\\d{3}\\s\\d{3}\\s\\d{4}$'
phoneNumberF3 = '^\\(\\d{3}\\)\\d{3}-\\d{4}$'
phoneNumberF4 = '^\\+\\d{2}\\s\\(\\d{2}\\)\\s\\d{3}-\\d{4}$'
phoneNumberF5 = '^\\+\\d\\(\\d{3}\\)\\d{3}\\-\\d{4}$'
phoneNumberF6 = '^\\d{5}.\\d{5}$'
phoneNumberF7 = '^\\d{3}-\\d{4}$'
phoneNumberF8 = '^\\d{3}\\s\\d{1}\\s\\d{3}\\s\\d{3}\\s\\d{4}$'
phoneNumberF9 = '^\\d{5}$'
phoneNumberF10 ='^\\d{3}\\s\\d{3}\\s\\d{3}\\s\\d{4}$'

# Regex for names
nameF1 = '^[a-zA-Z]+(((\'|-|.)?([a-zA-Z])+))?$'
nameF2 = '^[a-zA-Z]+(((\\,(\\s)|-|.)?([a-zA-Z])+))+((\\s)?([a-zA-Z])+)*$'
nameF3 = '^[a-zA-Z]+((\\s)?([a-zA-Z])+)*$'
nameF4 = '^([a-zA-Z])+$'
nameF5 = '^[^\s]+,?(\s[^\s]+)*$'
nameF6 = '^[a-zA-Z]+(((\\,(\\s)|-|.)?([a-zA-Z])+))*$'
nameF7 = '^[a-zA-Z]+((\\s)?((\'|-|.)?([a-zA-Z])+))*$'

# lists and variables
list1 = []
nameParameter = 0
phoneParameter = 1
headers = ['Name', 'Phone Number']


# Function for displaying LIST of records. 
def list():
    try:
        display2(headers, "")
        j = 1
        for i in list1:
            display2 (i, j)
            j += 1
        print()
        try:
            log2()
        except:
            print("")
            main()

    except:
        print("Error Displaying Data")

# Function for loading the csv file.
def load():
    try:
        if os.access("records.csv", os.F_OK):
            f = open("records.csv")
            for r in csv.reader(f):
                list1.append(r)
            f.close()
    except:
        print("Error Loading Data")

# Function to check to see if the user is root
def is_root():
    return os.geteuid() == 0

# FUnction to DELETE records using PHONE NUMBER
def delete_phone(number):

    try:
        j = 0
        f=0
        for i in list1:
            if i[phoneParameter] == number:
                print("Deleting Record....")
                f=1
                j+=1
            else:
                j+=1
        if f==0 :
            print("Record does not exist in the database")
            exit(1)
        del list1[j]
        print("Deleting.......")
        print("Record Deleted Number : ", number)
        save_csv()
    except:
        print("")

# Function to ADD records
def add():
    try:
        print("Enter Details For A New Record")
        nn = input("Enter Name: ")
        name_check(nn)
        nnp = input("Enter phone number: ")
        phone_check(nnp)
        phone = [nn, nnp]
        list1.append(phone)

        # Log the details if not Windows OS.
        if (platform.system().lower() != 'windows'):
            try:
                log(nn)
            except:

                print('')
                exit()
    except:
        print("Input Error")

# Function for DELETE records using NAME
def delete_name(name):
    try:
        j=0
        f=0
        for i in list1:
            if i[nameParameter]==name:
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
        save_csv()

        # Log the details if not Windows OS.
        if (platform.system().lower() != 'windows'):
            try:
                log(name)
            except:

                print('')
                exit()

    except:
        print("Error Deleting Data")


# Function for saving the data into the csv file.
def save_csv():
    try:
        f = open ("records.csv", 'w', newline='')
        for i in list1:
            csv.writer (f).writerow (i)
        f.close ()
    except:
        print("Error Saving Data")

# Function for check if input is valid
def choice(n):
    try:
        if not n.isdigit():
            print("Please enter a valid option")
            return False
        no = int(n)
        return True
    except:
        print("Error in entering choice")

def display2(phone, index):
    try:
        outputstr = "{0:>3}  {1:<20}  {2:>16}"
        print (outputstr.format (index, phone[nameParameter], phone[phoneParameter]))
    except:
        print("Error Displaying Data")

# Function to write into LOG file
def log(name):

    # Store the current system time and the RUID.
    t1 = datetime.now()
    ruid = os.getuid()

    try:

        if(is_root()):
            f = open("log.txt", "a")
            f.write("\nRUID: " + str(ruid) + ' ' + 'Name: ' + name + ' ' + "Time-Stamp: " + str(t1))
            f.close()

        # Error if the user isn't root.
        else:
            print("Unable to write into log file. Not a root user")
            main()
    except:
        print("")

# Function to update LOG file.
def log2():

    # Store the current system time and the RUID.
    ruid = os.getuid()
    t2 = datetime.now()

    # As long as the user is root, do the following:
    try:
        if(is_root()):
            f = open("log.txt", "a")
            f.write("\nRUID: " + str(ruid) + ' ' + "Time-Stamp: " + str(t2))
            f.close()

        # Error if the user isn't root.
        else:
            print("Unable to write into log file. Not a root user")
            main()
    except:
        print("")

def name_check(name):
    try:

        if (re.search(nameF1,name)):
            print("\nName Accepted")
        elif (re.search(nameF2,name)):
            print ("\nName Accepted")
        elif (re.search(nameF3,name)):
            print ("\nName Accepted")
        elif (re.search(nameF4,name)):
            print ("\nName Accepted")
        elif (re.search(nameF5,name )):
            print ("\nName Accepted")
        elif (re.search(nameF6,name)):
            print ("\nName Accepted")
        elif (re.search(nameF7,name)):
            print ("\nName Accepted")
        else:
            print("\nNot a Valid Name. Please Enter in correct format")
            exit(1)
    except:
        print("Regular Expression Search Error")

def phone_check(phone):
    try:

        if (re.search (phoneNumberF1,phone)):
            print("\nPhone Accepted")
        elif (re.search(phoneNumberF2,phone)):
            print ("\nPhone Accepted")
        elif (re.search(phoneNumberF3,phone)):
            print ("\nPhone Accepted")
        elif (re.search(phoneNumberF4, phone)):
            print ("\nPhone Accepted")
        elif (re.search(phoneNumberF5,phone)):
            print ("\nPhone Accepted")
        elif (re.search(phoneNumberF6,phone)):
            print ("\nPhone Accepted")
        elif (re.search(phoneNumberF7,phone)):
            print ("\nPhone Accepted")
        elif (re.search(phoneNumberF8, phone)):
            print ("\nPhone Accepted")
        elif (re.search(phoneNumberF9, phone)):
            print ("\nPhone Accepted")
        elif (re.search(phoneNumberF10, phone)):
            print ("\nPhone Accepted")
        else:
            print("\nNot a Valid Phone Number. Please Enter in correct format")
            exit(1)
    except:
        print("Regular Expression Search Error")

def menu():
    try:
        print ("#####Options#####")
        print ("\nList-L")
        print ("\nAdd-A")
        print("\nDelete using Name-DN")
        print ("\nDelete using Phone Number-DP")
        print ("\nExit-E")
        print("\nNote: Choices are case sensitive")
        choice = input("Choice: ")
        if choice.upper() in ['A', 'DN', 'L', 'DP', 'E']:
            return choice.upper()
        else:

            print("Not a valid choice. Please choose a correct choice..")
            return None
    except:
        print("Main Menu Error")
        exit(1)


def main():
    try:
        load()

        while True:
            choice = menu()
            if choice == None:
                continue
            if choice == 'A':
                add()
            elif choice == 'DP':
                num = input ("Please Enter The Phone Number Of The Record To Delete ")
                print("Phone number : ", num)
                delete_phone(num)
            elif choice == 'DN':
                num = input ("Please Enter The Name Of The Record To Delete ")
                print("Name : ", num)
                delete_name(num)
            elif choice == 'L':
                list()
            elif choice == 'E':
                print("Exiting...")
                exit()
            else:
                print("Not a Valid Choice")



        save_csv ()
    except:
        print("")
        exit()


if __name__ == '__main__':
    main()