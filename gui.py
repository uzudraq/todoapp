import functions
import PySimpleGUI as sg

label = sg.Text("Type in A to-do")
input_box = sg.InputText(tooltip ="Enter To-do")
add_button = sg.Button("Add")
# add_action = sg.

window = sg.Window('My To-Do App', layout=[[label, input_box, add_button]])
window.read()
print("helo")
window.close()



