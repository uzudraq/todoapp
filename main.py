

def get_open(todo_arg,filepath="files/todo.txt"):
    with open('files/todos.txt', 'r') as file:
        todos = file.readlines()
        
    return todos
# def get_write(todo_arg,filepath="files/todo.txt"):
#     with open('files/todos.txt','w') as file:
#         todos = file.writelines(todos)
    
while True:
    user_action = input("Type add, show, edit,complete or exit: ")
    user_action = user_action.strip()

    if 'add' in user_action:
        todo = user_action[4:]

        todos = get_open()'

        todos.append(todo)

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action:
        todos = get_open()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            row = f"{index + 1}:- {item}"
            print(row)

    elif 'edit' in user_action:
        number = int(user_action[5:])
        print(number)
        number = number - 1

        todos = get_open()

        # print("You want to edit this todo:- ", todos[number])
        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + '\n'
        # print("The new Todo is: " + new_todo)

        with open("files/todos.txt", 'w') as file:
            file.writelines(todos)

    elif 'complete' in user_action:
        number = int(user_action[9:])
        
        todos = get_open()

        index = number - 1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)

        with open("files/todos.txt", 'w') as file:
            file.writelines(todos)

        message = f"Todo :- {todo_to_remove} ,was removed from the list"
        print(message)

    elif 'exit' in user_action:
        break
    else:
        print("command is not valid")
    # match user_action:
    #     case _:
    #         print("Hey, you have entered unknown command")

print("Bye!")
