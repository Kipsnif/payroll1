import streamlit as st

st.title("🚀 Browser Streamlit App with Session State")

# 1. Initialize Session State variables if they don't exist
if "counter" not in st.session_state:
    st.session_state.counter = 0

if "todos" not in st.session_state:
    st.session_state.todos = ["Learn Streamlit", "Master Session State"]

# --- SECTION 1: THE COUNTER ---
st.header("🔢 Simple Counter")
st.write(f"The current count is: **{st.session_state.counter}**")

col1, col2 = st.columns(2)
with col1:
    if st.button("➕ Increment"):
        st.session_state.counter += 1
        st.rerun()  # Forces the app to update immediately
with col2:
    if st.button("➖ Decrement"):
        st.session_state.counter -= 1
        st.rerun()

# --- SECTION 2: THE TODO LIST ---
st.header("📝 Dynamic Todo List")

# Input for new todo
new_todo = st.text_input("Add a new task:", placeholder="Type something here...")

if st.button("Add Task") and new_todo:
    st.session_state.todos.append(new_todo)
    st.success(f"Added: {new_todo}")
    st.rerun()

# Display current todos
st.subheader("Current Tasks:")
for i, todo in enumerate(st.session_state.todos):
    st.write(f"{i+1}. {todo}")

# Reset Button
if st.button("🧹 Clear Everything"):
    st.session_state.counter = 0
    st.session_state.todos = []
    st.rerun()