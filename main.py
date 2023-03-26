import functions
import time

print("It is", time.strftime("%b, %d, %Y   %H:%M:%S"))

while True:
    user_action = input("Please enter add , show, edit,complete or exit:")
    if user_action.startswith('add'):
        # save the items that already in the file
        todos = functions.get_todos()
        todos.append(user_action[4:] + '\n')
        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}-{item}")
    elif user_action.startswith('exit'):
        break
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            todos = functions.get_todos()
            todos[number - 1] = input("Please enter the new todos :") + '\n'
            functions.write_todos(todos)

        except ValueError:
            print("Wrong action, please try again")
            continue
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            functions.write_todos(todos)
            print(f"{todo_to_remove} is removed")
        except IndexError:
            print("Wrong number, please try again")
            continue
    else:
        print("Wrong input,please enter again")
print('Bye!')
