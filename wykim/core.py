def printTitle():print("____Wykim____")
def mainMenu():
    l = ["Priority", "View Due Work", "Add Work", "Disregard Work", "Exit"]
    printTitle()
    for i, x in enumerate(l):print(f"{i+1} - {x}")
def userInput():return input(" >> ")
def priorityMenu(priority_work, priority_type, priority_due):
    printTitle()
    due = ""
    if priority_due == 0: due = "today"
    elif priority_due == 1: due = "tomorrow"
    else: due = f"in {priority_due} days"
    print(f"Your Priorities are due {due}")
    for x in range(len(priority_work)):
        print("\n----------\n")
        print(f"Priority: {x + 1}")
        print(f"Name: {priority_work[x]}")
        print(f"Type: {priority_type[x]}")
