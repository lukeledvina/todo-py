todo = {"Task": "Complete By",}

# Allow the user to either input tasks, or view tasks with an option at start
# Save the task dict to a file that can be saved to and read from

def input_task(task, date):
    todo[task] = date
    print(f"{task} added to be completed by {date}.")


# Sort by nearest completion date?
def view_tasks():
    for k, v in todo:
        print(k, v)

while True:
    choice = int(input("Please Select an option:\n(1) Input a new task\n(2) View task list\n(3) Exit"))
    if choice == 1:
        input_task(input("Input your task name: ", input("Input the completion date of the task: ")))
    elif choice == 2:
        view_tasks()
    elif choice == 3:
        exit()
    else:
        print("Enter a valid option")
