# Project Overview:
"""Objective: Develop a simple to-do list application using Python with an emphasis on
functions and data structures."""
# initialising the empty list for storing the tasks 
task = []
# defining user defined functions for various operations on to-do list
# function to add the tasks in to the to-do list
def add_tasks(num_tasks):
    for i in range(num_tasks):
        task.append(input(f"Task {i+1}:"))
# function to delete the tasks from to-do list
def delete_tasks(remove_task_num):
    for i, t in enumerate(task, 1):
            print(f"{i}. {t}")
    if 0<=remove_task_num<len(task):
        removed_task=task.pop(remove_task_num)
        print(f"{removed_task} has been successfully removed from your to-do list.")
    else:
        print("Invalid task number.")
# function to display the tasks in To-do list
def display_tasks():
    if task:
        for i, t in enumerate(task, 1):
            print(f"Task {i}: {t}")
    else:
        print("No tasks available.\n")
# function to mark the task as complete and to remove the completed task from To-do list
def mark_task_complete(complete_task_num):
    for i, t in enumerate(task, 1):
            print(f"{i}. {t}")
    if 0<=complete_task_num<len(task):
        complete_task=task.pop(complete_task_num)
        print(f"{complete_task} is marked as complete\n")
    else:
        print("Invalid task number.")
# function to update the tasks 
def update_tasks(task_num,update_task):
    for i, t in enumerate(task, 1):
        print(f"{i}. {t}")
    if (0<=task_num<len(task)):
        task[task_num]=update_task
        print("Task updated successfully.")
    else:
        print("Invalid task number.")
# function to append the tasks in to the To-do list
def append_tasks(new_task):
    task.append(new_task)
    print("Task added successfully.")
print("welcome to To-do List application developed by B Chaitanya Reddy\n")
print("Follow the below instructions for successful usage of the to-do list\n")
print("select any of the choice based on your requirement\n")
# instructions to be followed for successful usage of To-do list
print("For adding the tasks, enter your choice as 1\n")
print("For viewing the entered tasks, enter your choice as 2\n")
print("For updating the tasks, enter your choice as 3\n")
print("For appending the new tasks, enter your choice as 4\n")
print("For removing tasks, enter your choice as 5\n")
print("To mark task as complete, enter your choice as 6\n")
print("For exit, enter your choice as 7\n")
# initialising the while loop until the user desires to exit the program
while True:
    user_choice=int(input("Enter your choice:")) #accepting the user's choice
    # initialising the if condition based on user's choice for adding the tasks into the to-do list
    if user_choice==1:
        num_tasks=int(input("Enter the number of tasks to be added:"))
        add_tasks(num_tasks) # calling the add_tasks function that adds the tasks into the to-do list
    # initialising the elif condition based on user's choice to display the tasks in the to-do list
    elif user_choice==2:
        display_tasks() # calling the display_tasks function that displays the tasks in the to-do list
    # initialising the elif condition based on user's choice for updating the tasks in the to-do list
    elif user_choice==3:
        task_num=int(input("Enter the number of the task to be updated: "))-1
        update_task=input("Enter the updated task:")
        update_tasks(task_num,update_task)# calling the update_tasks function that update the tasks with the user input task
    # initialising the elif condition based on user's choice for appending the tasks into the to-do list
    elif user_choice==4:
        new_task=input("Enter the name of the task to append: ")
        append_tasks(new_task)# calling the append_tasks function to append the tasks into the to-do list
# initialising the elif condition based on user's choice for removing the tasks from the to-do list
    elif user_choice==5:
        remove_task_num=int(input("Enter the number of the task to be removed: "))-1
        delete_tasks(remove_task_num)# calling the delete_tasks function to delete the user specified task from to-do list
# initialising the elif condition based on user's choice for marking the task as complete in the to-do list
    elif user_choice==6:
        completed_task_num=int(input("Enter the number of the task to be mark as complete: "))-1
        mark_task_complete(completed_task_num)# calling the mark_task_complete function that marks the specified task as complete
# initialising the if condition based on user's choice for closing the to-do list
    elif user_choice==7:
        print("closing your To-do List.")
        break
    else:
        print("Invalid Choice,please enter a number between 1 and 7\n")
        break
