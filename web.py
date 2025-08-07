import streamlit as st
import functions as f

todos = f.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    f.write_todos(todos)
    st.session_state['new_todo'] = ""

st.title("My To-Do App")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        f.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Enter a new Todo",
              on_change=add_todo, key='new_todo')