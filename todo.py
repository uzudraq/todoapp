while True:
    user_action = input("Type add, show, edit,complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':
            with open('files/todos.txt','r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                item = item.title()
                row = f"{index + 1}:- {item}"
                print(row)

        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            print("You want to edit this todo:- ", todos[number] )
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input("Number of the todo to Complete: "))

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index]
            todos.pop(index)

            with open('files/todos.txt','w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)

        case 'exit':
            break
        case _:
            print("Hey, you have entered unknown command")

print("Bye!")
