def printTitle():
    print("____Wykim____")

def mainMenu():
    l = ["Priority", "View Due Work", "Add Work", "Disregard Work", "Exit"]
    printTitle()
    for i, x in enumerate(l):print(f"{i+1} - {x}")

def priorityMenu(priority_work, priority_due):
    printTitle()
    due = ""
    if priority_due == 0: due = "Today"
    elif priority_due == 1: due = "Tomorrow"
    else: due = priority_due
    print(f"Your Priority is \"{priority_work}\"\nDue {due}")


def userInput():return input(" >> ")
