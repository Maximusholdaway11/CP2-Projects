#Max Holdaway Keyboard To Do List

import keyboard

import csv

to_do_list = []

with open("to_do_list/TO_DO_LIST.txt", "r") as file:
    csv_txt_reader = csv.reader(file)
    if file.read() != "Empty":
        for row in csv_txt_reader:
            to_do_list = {"task": row[0], "completed": row[3]}
    else:
        pass

def add_a_task(to_do_list, task):
    if task not in to_do_list:
        to_do_list.append({"task": task, "completed": "No"})
        print(f"You have succesfully added the task {task}.")
    else:
        print("That task is already in there.")
    return to_do_list

def mark_a_task(to_do_list, task):
    if to_do_list != []:
        for dict_ in to_do_list:
            if dict_["task"] == task:
                if dict_["completed"] != "Yes":
                    dict_["completed"] == "Yes"
                    print(f"You have succesfully marked the task {task} as done.")
                else:
                    print("This task has already been completed.")
    else:
        print("There is nothing to mark.")
    return to_do_list

def find_task_index(to_do_list, task):
    dict_index = 0
    for dict_ in to_do_list:
        if dict_["task"] == task:
            dict_index = to_do_list.index(dict_)
    return dict_index

def remove_a_task(to_do_list, task):
    dict_index = find_task_index(to_do_list, task)
    to_do_list.pop(dict_index)
    return to_do_list

def display_all_tasks(to_do_list):
    print(to_do_list)
    if to_do_list != []:
        print("Here is your list.")
        for dict_ in to_do_list:
            print(f"""This is your task: {dict_["task"]}
and here is if its completed: {dict_["completed"]}""")
    else:
        print("There is nothing to show.")
        
def save_to_file(to_do_list):
    with open("to_do_list/TO_DO_LIST.txt", "w") as file:
        if to_do_list != []:
            for dict_ in to_do_list:
                file.write(f"Task: {dict_["task"]}, Completed: {dict_["completed"]}")
        else:
            file.write("Empty")

def print_user_instructions():
    print("This is a to_do_list. Which option do you want to use? (press number keys)")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Mark a task as done")
    print("4. Display all tasks")
    print("5. Press esc to exit")

print_user_instructions()
def main(to_do_list):
    while keyboard.is_pressed("Esc") != True:
        if keyboard.is_pressed("1") == True:
            user_task = input("What is the task you want to add?: ")
            to_do_list = add_a_task(to_do_list, user_task)
            print_user_instructions()

        if keyboard.is_pressed("2") == True:
            user_task = input("What is the task you want to remove?: ")
            to_do_list = remove_a_task(to_do_list, user_task)
            print_user_instructions()
        
        if keyboard.is_pressed("3") == True:
            user_task = input("What is the task you want to mark as done?: ")
            to_do_list = mark_a_task(to_do_list, user_task)
            print_user_instructions()
        
        if keyboard.is_pressed("4"):
            display_all_tasks(to_do_list)
            print_user_instructions()
        
        if keyboard.is_pressed("Esc"):
            print("Hope this was useful goodbye!")
            save_to_file(to_do_list)

            
main(to_do_list)