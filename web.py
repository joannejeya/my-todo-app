import streamlit as st
import functions as f

todos = f.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    f.write_todos(todos)
    st.session_state.new_todo = ""


st.title("To-Do List")
st.subheader("Make today count!")
st.write("Add tasks below, and check them off as you complete them.")

todos = f.get_todos()

for index, item in enumerate(todos):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        todos.pop(index)
        f.write_todos(todos)
        del st.session_state[item]
        st.rerun()

st.text_input(label=" ", placeholder="Add new todo...", on_change=add_todo, key="new_todo")
