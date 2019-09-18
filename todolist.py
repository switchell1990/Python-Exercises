"""
Let’s start with the good-old trusty todo list, the “Hello, World” of full programs.
You’re going to write a command-line todo list program that meets the following specifications:

Prompt the user to enter a chore or task. Store the task in a permanent location so that the task persists when the
program is restarted.

Allow the user to enter as many tasks as desired but stop entering tasks by entering a blank task.
Do not store the blank task.

Display all the tasks.

Allow the user to remove a task, to signify it’s been completed.

Persist todos to Redis
"""

import redis

r_server = redis.Redis("localhost")


def menu():
    choice = input("Please state which of the following (Add, Remove, Print, Exit): ")

    while True:
        if choice.lower() == "add":
            add_task()
        elif choice.lower() == "remove":
            # Decided to just delete the key, redis doesn't appear to have good functionality to delete by value.
            r_server.delete("Task")
            exit()
        elif choice.lower() == "print":
            task_list = r_server.get("Task").decode('utf-8')
            print("Here are your list of tasks that need completing {}".format(task_list))
            break
        elif choice.lower() == "exit":
            print("Thanks for using the To Do List Program. Shutting Down..")
            exit()
        else:
            print("Sorry was unable to recongise the command you have entered, please check and try again.")
            menu()


def add_task():
    task_add = input("Please enter a task: ")
    if task_add != "":
        r_server.append("Task", " " + task_add)
        if input("Would you like to add another task? Y/N ").lower().strip() == "y":
            add_task()
        else:
            exit()


print("Welcome to your To Do List")
menu()
