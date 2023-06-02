FILEPATH = "todos.txt"

def get_todos(filepath = FILEPATH):
    """ Read a text file and return the list of To-Do
    items.
    """
    with open(filepath,"r") as file_l:
        todos_l = file_l.readlines()
    return todos_l

def write_todos(todos_arg, filepath = FILEPATH):
    """Write the To-Do list in the text file. """
    with open(filepath,'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("hello")


