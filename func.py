FILEPATH = "todo.txt"
def get_todos(filepath=FILEPATH):

    with open(filepath,"r") as file:
        todo_local = file.readlines()

    return todo_local

def write_todos(todos_arg,filepath=FILEPATH):

    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("hello")
