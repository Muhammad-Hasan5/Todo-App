import functions as f
import FreeSimpleGUI as sg

label = sg.Text('Type in a To-Do')
input_box = sg.InputText(tooltip='Enter To-Do', key='todo')
add_button = sg.Button('Add')

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))
while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case 'Add':
            todo = f.get_todos()
            new_todo = value['todo'] + '\n'
            todo.append(new_todo)
            f.write_todos(todo)
        case WIN_CLOSED:
            break

window.close()


