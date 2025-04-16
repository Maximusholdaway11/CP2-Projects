#Max Holdaway To Do List

import csv

to_do_list = []

#Reading the file to get the saved to do list
with open("personal_portfolio/TO_DO_LIST.txt", "r", newline='\n') as file:
    csv_txt_reader = csv.reader(file)
    for row in csv_txt_reader:
        if len(row) == 2:
            to_do_list.append({"task": row[0], "completed": row[1]})
            print(to_do_list)
        else:
            pass

#Adding a task to the to do list
def add_a_task(to_do_list, task):
    for dict_ in to_do_list:
        if dict_["task"] == task:
            print("That task is already in there.")
            return to_do_list
    to_do_list.append({"task": task, "completed": "No"})
    print(f"You have succesfully added the task {task}.")
    return to_do_list

#Marking a task as done
def mark_a_task(to_do_list, task):
    if to_do_list != []:
        for dict_ in to_do_list:
            if dict_["task"] == task:
                if dict_["completed"] != "Yes":
                    dict_["completed"] = "Yes"
                    print(f"You have succesfully marked the task {task} as done.")
                else:
                    print("This task has already been completed.")
    else:
        print("There is nothing to mark.")
    return to_do_list

#Finding the task index for removing an item
def find_task_index(to_do_list, task):
    dict_index = None
    for dict_ in to_do_list:
        if dict_["task"] == task:
            dict_index = to_do_list.index(dict_)
    return dict_index

#Removing a task from the to do list
def remove_a_task(to_do_list, task):
    dict_index = find_task_index(to_do_list, task)
    if dict_index is not None:
        to_do_list.pop(dict_index)
        print(f"You have successfully removed {task}.")
    else:
        print("That item could not be found.")
    return to_do_list

#Display all the tasks
def display_all_tasks(to_do_list):
    print(to_do_list)
    if to_do_list != []:
        print("Here is your list.")
        for dict_ in to_do_list:
            print(f"""This is your task: {dict_["task"]}
and here is if its completed: {dict_["completed"]}""")
    else:
        print("There is nothing to show.")

#Saving the to do list to the file
def save_to_file(to_do_list):
    with open("personal_portfolio/TO_DO_LIST.txt", "w+", newline = '\n') as file:
        csv_txt_writer = csv.writer(file)
        csv_txt_reader = csv.reader(file)
        if to_do_list != []:
            for dict_ in to_do_list:
                if dict_["task"] not in csv_txt_reader:
                    csv_txt_writer.writerow(dict_.values())
                else:
                    pass
        else:
            file.write("")

#The main user interface
def main(to_do_list):
    while True:
        user_input = input("""This is a to do list. Which option do you want to use? (type in a number to use)
1. Add a task
2. Remove a task
3. Mark a task as done
4. Display all tasks
5. Save the to do list
6. Exit (will auto save)\n""")

        if user_input.isnumeric():
            user_input = int(user_input)

            if user_input == 1:
                user_task = input("What is the task you want to add?: ")
                to_do_list = add_a_task(to_do_list, user_task)

            if user_input == 2:
                user_task = input("What is the task you want to remove?: ")
                to_do_list = remove_a_task(to_do_list, user_task)
                
            
            if user_input == 3:
                user_task = input("What is the task you want to mark as done?: ")
                to_do_list = mark_a_task(to_do_list, user_task)
            
            if user_input == 4:
                display_all_tasks(to_do_list)

            if user_input == 5:
                print("To Do List has been saved successfully.")
                save_to_file(to_do_list)
            
            if user_input == 6:
                print("Hope this was useful goodbye!")
                save_to_file(to_do_list)
                break

        else:
            print("You have not selected a number please try again.")