#Max Holdaway To Do List

import csv

to_do_list = []

with open("to_do_list/TO_DO_LIST.txt", "r") as file:
    csv_txt_reader = csv.reader(file)
    if csv_txt_reader != "Empty":
        for row in csv_txt_reader:
            to_do_list.append({"task": row[0], "completed": row[1]})
            print(to_do_list)
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
                    dict_["completed"] = "Yes"
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
    with open("to_do_list/TO_DO_LIST.txt", "a") as file:
        csv_txt_writer = csv.writer(file)
        if to_do_list != []:
            for dict_ in to_do_list:
                csv_txt_writer.writerow([f"{dict_["task"]}, {dict_["completed"]}"])
        else:
            file.write("Empty")

def main(to_do_list):
    while True:
        user_input = input("""This is a to_do_list. Which option do you want to use? (press number keys)"
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
           
main(to_do_list)