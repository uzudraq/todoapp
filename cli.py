from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S ")
print("the time is below: ")
print("It is", now)

while True:
    user_action = input("Type add, show, edit,complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()  # parameter,argument

        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            row = f"{index + 1}:- {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            todos = get_todos()

            print("You want to edit this todo:- ", todos[number])
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'
            print("The new Todo is: " + new_todo)
            # change from line 20, here filepath and todos_arg is specifically mentioned,
            # that is required cuz todos_arg is not default parameter and
            # non default parameter follows deafult parameters.
            # un
            write_todos(todos)
        except ValueError:
            print("Please enter a valid command")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Todo :- {todo_to_remove} ,was removed from the list"
            print(message)

        except IndexError:
            print("there is no todo with this number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("command is not valid")

print("Bye!")
