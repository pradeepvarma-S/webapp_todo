import streamlit as st
from todo_function import get_todo, write_todos


def add_todo():
    todo = st.session_state["new_todo"]
    print(todo)
    todos.append(todo + "\n")
    write_todos(todos)

st.set_page_config(layout="wide")

st.title("My TODO APP")
st.header("This App will help you to manage your day task")

# st.checkbox("Hi have a great day")
todos = get_todo()

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="ADD New TODO",
              on_change=add_todo, key='new_todo')

#st.session_state
