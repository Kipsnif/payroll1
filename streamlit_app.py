import streamlit as st

st.title("🚀 Payroll app V1")

# --- 1. MOCK DATA (The One-to-Many Relationship) ---
# One company can have multiple employees.
COMPANIES = {
    "C01": {"name": "TechCorp", "employees": ["E01", "E02"]},
    "C02": {"name": "BioHealth", "employees": ["E03"]},
}

EMPLOYEES = {
    "E01": {"name": "Alice Smith", "role": "Software Engineer", "company_id": "C01"},
    "E02": {"name": "Bob Jones", "role": "UI Designer", "company_id": "C01"},
    "E03": {"name": "Charlie Brown", "role": "Biologist", "company_id": "C02"},
}

# --- 2. INITIALIZE SESSION STATE ---
# Track which view/page we are on, and which item is selected
if "current_view" not in st.session_state:
    st.session_state.current_view = "Dashboard"

if "selected_company_id" not in st.session_state:
    st.session_state.selected_company_id = None

if "selected_employee_id" not in st.session_state:
    st.session_state.selected_employee_id = None


# --- 3. HELPER NAVIGATION FUNCTIONS ---
def go_to_dashboard():
    st.session_state.current_view = "Dashboard"
    st.session_state.selected_company_id = None
    st.session_state.selected_employee_id = None
    st.rerun()

def go_to_company(company_id):
    st.session_state.current_view = "Company Page"
    st.session_state.selected_company_id = company_id
    st.session_state.selected_employee_id = None
    st.rerun()

def go_to_employee(employee_id):
    st.session_state.current_view = "Employee Page"
    st.session_state.selected_employee_id = employee_id
    # Automatically ensure the company state is aligned with this employee
    st.session_state.selected_company_id = EMPLOYEES[employee_id]["company_id"]
    st.rerun()


# --- 4. THE PAGES ---

def render_dashboard():
    st.title("🏢 Main Directory Dashboard")
    st.write("Select a company or look at all employees below.")
    
    st.subheader("Companies")
    for c_id, c_data in COMPANIES.items():
        # Clicking this button updates state and "routes" to the company page
        if st.button(f"Go to {c_data['name']}", key=f"btn_c_{c_id}"):
            go_to_company(c_id)
            
    st.markdown("---")
    st.subheader("All System Employees")
    for e_id, e_data in EMPLOYEES.items():
        comp_name = COMPANIES[e_data["company_id"]]["name"]
        if st.button(f"👤 {e_data['name']} ({comp_name})", key=f"btn_e_{e_id}"):
            go_to_employee(e_id)


def render_company_page():
    c_id = st.session_state.selected_company_id
    company_data = COMPANIES[c_id]
    
    st.title(f"🏢 Company Profile: {company_data['name']}")
    st.caption(f"Company ID: {c_id}")
    
    if st.button("⬅️ Back to Main Dashboard"):
        go_to_dashboard()
        
    st.markdown("---")
    st.subheader("Attached Employees (One-to-Many)")
    st.write("The following employees belong strictly to this company:")
    
    # Loop through only the employees attached to this specific company
    for e_id in company_data["employees"]:
        e_data = EMPLOYEES[e_id]
        if st.button(f"View {e_data['name']}'s Page", key=f"comp_page_{e_id}"):
            go_to_employee(e_id)


def render_employee_page():
    e_id = st.session_state.selected_employee_id
    employee_data = EMPLOYEES[e_id]
    parent_company = COMPANIES[employee_data["company_id"]]
    
    st.title(f"👤 Employee Profile: {employee_data['name']}")
    st.write(f"**Role:** {employee_data['role']}")
    
    # Highlight the strict parent relationship
    st.info(f"🔗 **Attached to Higher Level:** {parent_company['name']}")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back to Company"):
            go_to_company(employee_data["company_id"])
    with col2:
        if st.button("🏠 Home Dashboard"):
            go_to_dashboard()

# --- 5. ROUTER ---
# Read the session state and decide which page function to run
if st.session_state.current_view == "Dashboard":
    render_dashboard()
elif st.session_state.current_view == "Company Page":
    render_company_page()
elif st.session_state.current_view == "Employee Page":
    render_employee_page()


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