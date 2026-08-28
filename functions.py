def get_todos(filepath="todos.txt"):
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(updated_todos, filepath="todos.txt"):
    with open(filepath, "w") as file:
        file.writelines(updated_todos)

