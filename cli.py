import functions
import time


date = time.strftime("%b %d, %Y")
time = time.strftime("%H:%M")
print(f"Date: {date}")
print(f"Time: {time}\n")


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        user_action = user_action[4:]

        todos = functions.get_todos()

        todos.append(user_action)

        functions.write_todos(todos)

    elif user_action.startswith('show'):

        todos = functions.get_todos()

        for index, items in enumerate(todos):
            print(f"{index + 1}-{items.strip('\n')}")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Edit todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("invalid command")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            index = number - 1

            todos = functions.get_todos()

            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo '{todo_to_remove}' is removed!"
            print(message)

        except IndexError:
            print("invalid index")
            continue

    elif user_action.startswith('exit'):
        print("Bye!")
        break

    else:
        print("Invalid command!")


