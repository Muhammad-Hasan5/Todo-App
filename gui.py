import functions as f
import time
import FreeSimpleGUI as sg

sg.theme("Black")

clock = sg.Text('', key='clock')
label = sg.Text('Type in a To-Do')
input_box = sg.InputText(tooltip='Enter To-Do', key='todo')
add_button = sg.Button('Add', size=8)
list_box = sg.Listbox(values=f.get_todos(), key='todos',
                      enable_events=True, size=(45, 10))
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')

window = sg.Window('My To-Do App',
                   layout=[[clock], [label], [input_box, add_button],
                   [list_box, edit_button, complete_button], [exit_button]],
                   font=('Helvetica', 20))
while True:
    event, value = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M"))
    print(1, event)
    print(2, value)
    print(3, value['todos'])
    match event:
        case 'Add':
            todo = f.get_todos()
            new_todo = value['todo'] + '\n'
            todo.append(new_todo)
            f.write_todos(todo)
            window['todos'].update(values=todo)
        case 'Edit':
            try:
                todo_to_edit = value['todos'][0]
                new_todo = value['todo']

                todos = f.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                f.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first!", font=('helvetica', 20))
        case 'todos':
            window['todo'].update(value=value['todos'][0])
        case 'Complete':
            try:
                todo_to_complete = value['todos'][0]
                todos = f.get_todos()
                todos.remove(todo_to_complete)
                f.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first!", font=('helvetica', 20))
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break

window.close()


