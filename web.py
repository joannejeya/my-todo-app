import streamlit as st
import functions as f

todos = f.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    f.write_todos(todos)


st.title("My To-do App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

todos = f.get_todos()

for item in todos:
    st.checkbox(item)

st.text_input(label="Label", placeholder="Add new todo...", on_change=add_todo, key="new_todo")

print("Hello")