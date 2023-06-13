import functions
import PySimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter to do", key='todo')
add_button = sg.Button("Add")

window = sg.Window("My TO-DO App",
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 10))
while True:
    enent, vaule = window.read()
    match enent:
        case "Add":
            todos = functions.get_todos()
            todos.append(vaule['todo']+"\n")
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break


window.close()
