import functions
import PySimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter to do")
add_button = sg.Button("Add")

window = sg.Window("My TO-DO App",layout=[[label],[input_box,add_button]])
window.read()
window.close()