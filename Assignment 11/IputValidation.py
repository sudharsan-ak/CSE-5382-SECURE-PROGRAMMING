import os
import csv
from datetime import datetime
import re
import time
from datetime import datetime
import platform


# Regex for phone numbers
phoneNumberFormat1 = '^\\d{1}\\(\\d{3}\\)\\d{3}-\\d{4}$'
phoneNumberFormat2 = '^\\d{3}\\s\\d{1}\\s\\d{3}\\s\\d{3}\\s\\d{4}$'
phoneNumberFormat3 = '^\\(\\d{3}\\)\\d{3}-\\d{4}$'
phoneNumberFormat4 = '^\\+\\d{2}\\s\\(\\d{2}\\)\\s\\d{3}-\\d{4}$'
phoneNumberFormat5 = '^\\+\\d\\(\\d{3}\\)\\d{3}\\-\\d{4}$'
phoneNumberFormat6 = '^\\d{5}.\\d{5}$'
phoneNumberFormat7 = '^\\d{3}-\\d{4}$'
phoneNumberFormat8 = '^\\d{3}\\s\\d{1}\\s\\d{3}\\s\\d{3}\\s\\d{4}$'
phoneNumberFormat9 = '^\\d{5}$'
phoneNumberFormat10 ='^\\d{3}\\s\\d{3}\\s\\d{3}\\s\\d{4}$'

# Regex for names
nameFormat1 = '^[a-zA-Z]+(((\'|-|.)?([a-zA-Z])+))?$'
nameFormat2 = '^[a-zA-Z]+(((\\,(\\s)|-|.)?([a-zA-Z])+))+((\\s)?([a-zA-Z])+)*$'
nameFormat3 = '^[a-zA-Z]+((\\s)?([a-zA-Z])+)*$'
nameFormat4 = '^([a-zA-Z])+$'
nameFormat5 = '^[^\s]+,?(\s[^\s]+)*$'
nameFormat6 = '^[a-zA-Z]+(((\\,(\\s)|-|.)?([a-zA-Z])+))*$'
nameFormat7 = '^[a-zA-Z]+((\\s)?((\'|-|.)?([a-zA-Z])+))*$'

# lists and variables for data processing
list1 = []
nameParameter = 0
phoneParameter = 1
headers = ['Name', 'Phone Number']


# Function for listing the available data. 
def display():
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

# FUnction for deleting the record using phone number.
def delete(number):

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
        print("Deleting.;......")
        print("Record Deleted Number : ", number)
        save_list()
    except:
        print("")

# This function is used for the ADD function:
def create():
    try:
        print("Enter Details For A New Record")
        nn = input("Enter Name: ")

        # Checking the name using regex
        check_name(nn)
        nnp = input("Enter phone number: ")

        # Checking the phone number using regex
        check_phone_no(nnp)

        # Putting them together into a list
        phone = [nn, nnp]

        # Appending the new list to the initial list.
        list1.append(phone)

        # As long as the platform isn't windows, log the details.
        if (platform.system().lower() != 'windows'):
            try:
                log(nn)
            except:

                print('')
                exit()
    except:
        print("Error Input")

# Function for deleting the record using the name.
def delete2(name):
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
        save_list()

        # As long as the platform isn't windows, log the details.
        if (platform.system().lower() != 'windows'):
            try:
                log(name)
            except:

                print('')
                exit()

    except:
        print("Error Deleting Data")


# Function for saving the data into the csv file.
def save_list():
    try:
        f = open ("records.csv", 'w', newline='')
        for i in list1:
            csv.writer (f).writerow (i)
        f.close ()
    except:
        print("Error Saving Data")

# Function for input validations (checking if it is a digit and so on)
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
        print (outputstr.format (index, phone[nameParameter], phone[phoneParameter]))
    except:
        print("Error Displaying Data")

# The following function is used inside of the ADD function.
def log(name):

    # Set a variable for the current time and the RUID that is received from the system.
    t1 = datetime.now()
    ruid = os.getuid()

    # Set up a pair of try-except statements for writing the log file.
    try:

        # As long as the user is root, do the following:
        if(is_root()):

            # Open a file named log.txt to write data.
            f = open("log.txt", "a")

            # Write data to it and close file.
            f.write("\nRUID: " + str(ruid) + ' ' + 'Name: ' + name + ' ' + "Time-Stamp: " + str(t1))
            f.close()

        # Throw an error message to the user if the user isn't root.
        else:
            print("Cannot write to log, Not a root user")
            main()
    except:
        print("")

# The following function is used inside of the DELETE function.
def log2():

    # Set a variable for the current time and the RUID that is received from the system.
    ruid = os.getuid()
    t2 = datetime.now()

    # As long as the user is root, do the following:
    try:
        if(is_root()):

            # Open a file named log.txt to write data.
            f = open("log.txt", "a")

            # Write data to it and close file.
            f.write("\nRUID: " + str(ruid) + ' ' + "Time-Stamp: " + str(t2))
            f.close()

        # Throw an error message to the user if the user isn't root.
        else:
            print("Cannot write to log, Not a root user")
            main()
    except:
        print("")

def check_name(name):
    try:

        if (re.search ( nameFormat1,name)):
            print("\nName Accepted")
        elif (re.search( nameFormat2,name)):
            print ("\nName Accepted")
        elif (re.search( nameFormat3,name)):
            print ("\nName Accepted")
        elif (re.search(nameFormat4,name)):
            print ("\nName Accepted")
        elif (re.search(nameFormat5,name )):
            print ("\nName Accepted")
        elif (re.search(nameFormat6,name)):
            print ("\nName Accepted")
        elif (re.search(nameFormat7,name)):
            print ("\nName Accepted")
        else:
            print("\nName Rejected, Enter it in correct format")
            exit(1)
    except:
        print("Error in regular expression search")

def check_phone_no(phone):
    try:

        if (re.search ( phoneNumberFormat1,phone)):
            print("\nPhone Accepted")
        elif (re.search( phoneNumberFormat2,phone)):
            print ("\nPhone Accepted")
        elif (re.search( phoneNumberFormat3,phone)):
            print ("\nPhone Accepted")
        elif (re.search( phoneNumberFormat4, phone)):
            print ("\nPhone Accepted")
        elif (re.search( phoneNumberFormat5,phone)):
            print ("\nPhone Accepted")
        elif (re.search( phoneNumberFormat6,phone)):
            print ("\nPhone Accepted")
        elif (re.search( phoneNumberFormat7,phone)):
            print ("\nPhone Accepted")
        elif (re.search (phoneNumberFormat8, phone)):
            print ("\nPhone Accepted")
        elif (re.search (phoneNumberFormat9, phone)):
            print ("\nPhone Accepted")
        elif (re.search (phoneNumberFormat10, phone)):
            print ("\nPhone Accepted")
        else:
            print("\nPhone Rejected, Enter it in correct format")
            exit(1)
    except:
        print("Error in regular expression search")

def menu():
    try:
        print ("#####Options#####")
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