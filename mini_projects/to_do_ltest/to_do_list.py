import os;

file_name="text.txt"

if not os.path.exists(file_name):
    open(file_name,"w").close()

def load_tasks():
    tasks=[]
    with open(file_name,"r")as f:
        for line in f:
            status,task_task=line.strip().split("|",1)
            tasks.append({"status":status,"task":task_task})
    return tasks

def save_tasks(tasks):
    with open(file_name,"w")as f:
        for t in tasks:
            f.write(t["status"]+"|"+t["task"]+"\n")

def show_tasks(tasks):
    if not tasks:
        print("\n no task found!\n")
        return 

    print("\n ypur tasks :")
    for i ,t in enumerate(tasks,start=1):
        mark="✔" if t["status"] == "1" else "✘"
        print(f"{i}. [{mark}] {t['task']}")
    print()


# Add task
def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task:
        tasks.append({"status": "0", "task": task})
        save_tasks(tasks)
        print("Task added successfully!\n")


# Mark as completed
def complete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to mark complete: "))
        tasks[num - 1]["status"] = "1"
        save_tasks(tasks)
        print("Task marked as completed!\n")
    except:
        print("Invalid number!\n")


# Delete task
def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print("Task deleted!\n")
    except:
        print("Invalid number!\n")


# Main Program
def main():
    while True:
        print("====== TO-DO LIST ======")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose option: ")

        tasks = load_tasks()

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            add_task(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice!\n")


if __name__ == "__main__":
    main()