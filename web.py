import streamlit as st
import functions as f

st.title("My To-Do App")

todos = f.get_todos()

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Enter a new Todo")