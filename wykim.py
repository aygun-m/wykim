#/usr/bin/python3
from wykim import Wykim
from wykim.core import *
import sqlite3, os
from datetime import datetime, timedelta
__author__ = "Mert"
__version__ = "1.0.3"
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
            currentDate = datetime.now() 
            listOfDates = [x for x in results]
            listOfDays = []
            for x in listOfDates:
                y = x[3]
                listOfDays.append(datetime.strptime(y, "%Y-%m-%d"))
            empList = [] 
            for x in listOfDays:
                i = 0
                while(x > currentDate):
                    x = x - timedelta(days=1)
                    i = i + 1
                empList.append(i)
            minimum = min(empList) 
            priorityWork = []
            priorityType = []
            priorityDue = []
            for x in results:
                dt = str(currentDate + timedelta(days=minimum))[:10]
                if(x[3] == dt):
                    priorityWork.append(x[1])
                    priorityType.append(x[2])
                    priorityDue.append(x[3])
            priorityMenu(priorityWork, priorityType, minimum)
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
