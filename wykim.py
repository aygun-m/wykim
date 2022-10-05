#/usr/bin/python3
from wykim import Wykim
from wykim.core import *
import sqlite3
import os, time
from datetime import datetime, timedelta
__author__ = "Mert"
__version__ = "1.0.2"
__date__ = "28/09/2004"
wykim = Wykim()
ready = True
while(ready):
    try:
        os.system("clear")
        mainMenu()
        mainUserInput = int(userInput())
        if mainUserInput == 1:
            conn = sqlite3.connect(wykim.dbPath)
            curr = conn.cursor()
            results = curr.execute("SELECT * FROM WorkItems").fetchall()
            conn.close()
            #Find the date closest to now.
            #timedelta can be used to add and subtract from datetime objects

            #priorityMenu(priorityWork, priorityType, priorityDue)
            print("\n----------\n\nPress Enter to return to menu")
            input()
        elif mainUserInput == 2:
            conn = sqlite3.connect(wykim.dbPath)
            curr = conn.cursor()
            results = curr.execute("SELECT * FROM WorkItems").fetchall()
            print("---------- >>")
            for x in results:print(x)
            print("---------- >>\nPress Enter to return to menu")
            input()
            conn.close()
        elif mainUserInput == 3:
            print("Enter Work Name")
            workName = userInput()
            print("Enter Work Type")
            workType = userInput()
            print("Enter Due Date (Year)")
            workDueYear = int(userInput())
            print("Enter Due Date (Month)")
            workDueMonth = int(userInput())
            print("Enter Due Date (Day)")
            workDueDay = int(userInput())
            workDue = str(datetime(workDueYear, workDueMonth, workDueDay))[:10]
            conn = sqlite3.connect(wykim.dbPath)
            curr = conn.cursor()
            curr.execute(f"INSERT INTO WorkItems(name, type, due) VALUES (\"{workName}\", \"{workType}\", \"{workDue}\")")
            conn.commit()
            print("---------- >>")            
            print("Record has been created")
            print("---------- >>\nPress Enter to return to menu")
            input()            
            conn.close()
        elif mainUserInput == 4:
            conn = sqlite3.connect(wykim.dbPath)
            curr = conn.cursor()
            results = curr.execute("SELECT * FROM WorkItems").fetchall()
            conn.close()
            print("---------- >>")
            for x in results:print(x)
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
