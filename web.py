import streamlit as st
import func

def add_todo():
    todo = st.session_state['new_todos']+ '\n'
    print(todo)
    todos.append(todo)
    func.write_todos(todos)


todos = func.get_todos()
st.title("check_app")
st.subheader('My check list')
st.write("This app is to help you to manage your checklist for an event")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        func.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='',placeholder='please enter todo',
              on_change=add_todo,
              key='new_todos')


