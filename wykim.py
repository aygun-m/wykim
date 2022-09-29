#/usr/bin/python3
from wykim import Wykim
from wykim.core import *
import sqlite3
import os
__author__ = "Mert"
__version__ = "1.0.0"
__date__ = "28/09/2004"
wykim = Wykim()
ready = True
while(ready):
    try:
        os.system("clear")
        mainMenu()
        mainUserInput = int(userInput())
        if mainUserInput == 1:
            #Get Priority Work Item
            #Get Due Date
            #priorityMenu()
            """
            
            The only thing left
            
            """

        elif mainUserInput == 2:
            #Get All Records in Database
            #Print in List Format
            conn = sqlite3.connect(wykim.dbPath)
            curr = conn.cursor()
            results = curr.execute("SELECT * FROM WorkItems").fetchall()
            
            print("---------- >>")
            for x in results:
                print(x)
            print("---------- >>\nPress Enter to return to menu")
            input()
            conn.close()
        elif mainUserInput == 3:
            #Enter Work Type: "Assignment"
            #Enter Due Date:  "7"
            #Record has been added
            print("Enter Work Name")
            workName = userInput()
            print("Enter Work Type")
            workType = userInput()
            print("Enter Due Distance")
            workDue = int(userInput())
            conn = sqlite3.connect(wykim.dbPath)
            curr = conn.cursor()
            curr.execute(f"INSERT INTO WorkItems(name, type, due) VALUES (\"{workName}\", \"{workType}\", {workDue})")
            conn.commit()
            print("---------- >>")            
            print("Record has been created")
            print("---------- >>\nPress Enter to return to menu")
            input()            
            conn.close()
        elif mainUserInput == 4:
            #Get All Records in Database
            #Print in List Format
            #Enter Work Item: "id=14"
            #Record has been deleted
            conn = sqlite3.connect(wykim.dbPath)
            curr = conn.cursor()
            results = curr.execute("SELECT * FROM WorkItems").fetchall()
            conn.close()
            print("---------- >>")
            for x in results:
                print(x)
            print("---------- >>")
            print("Enter ID (int)")
            delRecord = int(userInput())
            delConn = sqlite3.connect(wykim.dbPath)
            delCurr = delConn.cursor()
            results = delCurr.execute(f"DELETE FROM WorkItems WHERE id={delRecord}")
            delConn.commit()
            print("Record has been deleted\n---------- >>\nPress Enter to return to menu")
            input()
            delConn.close()
        elif mainUserInput == 5:
            print("Quitting Wykim...")
            exit()
        else:pass
    except KeyboardInterrupt:
        print("\nQuitting Wykim...")
        exit()
    

