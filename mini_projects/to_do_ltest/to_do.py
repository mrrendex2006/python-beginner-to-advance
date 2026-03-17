tasks=[]

def add_task():
    task=input("enter a new task : ")
    tasks.append(task)

def view():
    if not tasks:
        print("no tasks in the list :")
    else:
        print("\n your tasks are :-")
        for i ,task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
def Delete():
    view()
    if tasks:
        try:
            task_num=int(input("enter task number to delete "))
            remove=tasks.pop(task_num-1)
            print(f"removed task:{remove}")

        except (ValueError, IndexError):
            print("invalid task number ")

def to_do():
    
    print("CHOICE::\n")
    print("1. add tasks ")
    print("2. View tasks ")
    print("3. Delete task ")
    print("4. exit")

    choice=input("Enter an option ")

    if choice == "1":
        add_task()
        
    elif choice == "2":
        view()

    elif choice =="3":
        Delete()

    elif choice == "4":
        return False
      

    else:
        print("invalid choice ")

    return True

while True:
    if not to_do():
        print("thank you bye <->")
        break

