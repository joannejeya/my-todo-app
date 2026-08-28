import functions as f

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todo.capitalize()
        todos = f.get_todos()

        todos.append(todo + '\n')
        f.write_todos(todos)

    elif user_action.startswith("show"):
        todos = f.get_todos()
        for index, item in enumerate(todos):
            instruction = item.strip("\n")
            print(f"{index+1}. {instruction.capitalize()}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:]) - 1
            todos = f.get_todos()

            new_todo = input("What is the new todo?")
            todos[number] = new_todo + '\n'
            f.write_todos(todos)

        except ValueError:
            print("Command is invalid! You must enter 'edit #'.")
            continue
        except IndexError:
            print("This is not a number on the list!")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:]) - 1
            todos = f.get_todos()

            todo_to_remove = todos[number].strip("\n")
            todos.pop(number)

            f.write_todos(todos)

            message = f"Todo '{todo_to_remove}' was removed from the list!"
            print(message)
        except IndexError:
            print("There is not an item with this number.")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command not valid!")
        continue

print("Bye!")