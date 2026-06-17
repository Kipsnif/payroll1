import streamlit as st

st.title("🚀 Payroll App - 8-Level Hierarchy")

# --- 1. HIERARCHY DEFINITION ---
HIERARCHY_LEVELS = [
    "Administrator",
    "Group",
    "Corporation",
    "Company",
    "Employee",
    "Contract",
    "Period",
    "Version"
]

LEVEL_INDEX = {level: i for i, level in enumerate(HIERARCHY_LEVELS)}
LEVEL_ICONS = {
    "Administrator": "👨‍💼",
    "Group": "👥",
    "Corporation": "🏢",
    "Company": "🏭",
    "Employee": "👤",
    "Contract": "📄",
    "Period": "📅",
    "Version": "📌"
}

# --- 2. MOCK DATA (8-Level Hierarchical Structure) ---
# Each level stores entities with parent references and children lists
ENTITIES = {
    "Administrator": {
        "A01": {"name": "Admin One", "email": "admin@company.com", "groups": ["G01", "G02"]},
        "A02": {"name": "Admin Two", "email": "admin2@company.com", "groups": ["G03"]},
    },
    "Group": {
        "G01": {"name": "Group Alpha", "description": "Tech Division", "parent_id": "A01", "corporations": ["C01", "C02"]},
        "G02": {"name": "Group Beta", "description": "Healthcare Division", "parent_id": "A01", "corporations": ["C03"]},
        "G03": {"name": "Group Gamma", "description": "Finance Division", "parent_id": "A02", "corporations": ["C04"]},
    },
    "Corporation": {
        "C01": {"name": "TechCorp International", "headquarters": "San Francisco", "parent_id": "G01", "companies": ["CO01", "CO02"]},
        "C02": {"name": "TechCorp Europe", "headquarters": "London", "parent_id": "G01", "companies": ["CO03"]},
        "C03": {"name": "BioHealth Solutions", "headquarters": "Boston", "parent_id": "G02", "companies": ["CO04"]},
        "C04": {"name": "FinanceCore Ltd", "headquarters": "New York", "parent_id": "G03", "companies": ["CO05"]},
    },
    "Company": {
        "CO01": {"name": "TechCorp USA", "location": "California", "parent_id": "C01", "employees": ["E01", "E02"]},
        "CO02": {"name": "TechCorp Canada", "location": "Toronto", "parent_id": "C01", "employees": ["E04"]},
        "CO03": {"name": "TechCorp UK", "location": "London", "parent_id": "C02", "employees": ["E05"]},
        "CO04": {"name": "BioHealth Labs", "location": "Boston", "parent_id": "C03", "employees": ["E03"]},
        "CO05": {"name": "FinanceCore HQ", "location": "New York", "parent_id": "C04", "employees": ["E06"]},
    },
    "Employee": {
        "E01": {"name": "Alice Smith", "role": "Software Engineer", "email": "alice@techcorp.com", "parent_id": "CO01", "contracts": ["CT01"]},
        "E02": {"name": "Bob Jones", "role": "UI Designer", "email": "bob@techcorp.com", "parent_id": "CO01", "contracts": ["CT02"]},
        "E03": {"name": "Charlie Brown", "role": "Biologist", "email": "charlie@biohealth.com", "parent_id": "CO04", "contracts": ["CT03"]},
        "E04": {"name": "Diana Prince", "role": "Manager", "email": "diana@techcorp.com", "parent_id": "CO02", "contracts": ["CT04"]},
        "E05": {"name": "Eve Wilson", "role": "Developer", "email": "eve@techcorp.com", "parent_id": "CO03", "contracts": ["CT05"]},
        "E06": {"name": "Frank Miller", "role": "Analyst", "email": "frank@financecore.com", "parent_id": "CO05", "contracts": ["CT06"]},
    },
    "Contract": {
        "CT01": {"name": "Full-Time 2024", "type": "Full-time", "salary": 120000, "parent_id": "E01", "periods": ["P01"]},
        "CT02": {"name": "Part-Time 2024", "type": "Part-time", "salary": 60000, "parent_id": "E02", "periods": ["P02"]},
        "CT03": {"name": "Full-Time 2024", "type": "Full-time", "salary": 110000, "parent_id": "E03", "periods": ["P03"]},
        "CT04": {"name": "Full-Time 2024", "type": "Full-time", "salary": 130000, "parent_id": "E04", "periods": ["P04"]},
        "CT05": {"name": "Full-Time 2024", "type": "Full-time", "salary": 115000, "parent_id": "E05", "periods": ["P05"]},
        "CT06": {"name": "Full-Time 2024", "type": "Full-time", "salary": 125000, "parent_id": "E06", "periods": ["P06"]},
    },
    "Period": {
        "P01": {"name": "Q1 2024", "start_date": "2024-01-01", "end_date": "2024-03-31", "parent_id": "CT01", "versions": ["V01", "V02"]},
        "P02": {"name": "Q1 2024", "start_date": "2024-01-01", "end_date": "2024-03-31", "parent_id": "CT02", "versions": ["V03"]},
        "P03": {"name": "Q1 2024", "start_date": "2024-01-01", "end_date": "2024-03-31", "parent_id": "CT03", "versions": ["V04"]},
        "P04": {"name": "Q1 2024", "start_date": "2024-01-01", "end_date": "2024-03-31", "parent_id": "CT04", "versions": ["V05"]},
        "P05": {"name": "Q1 2024", "start_date": "2024-01-01", "end_date": "2024-03-31", "parent_id": "CT05", "versions": ["V06"]},
        "P06": {"name": "Q1 2024", "start_date": "2024-01-01", "end_date": "2024-03-31", "parent_id": "CT06", "versions": ["V07"]},
    },
    "Version": {
        "V01": {"name": "Version 1.0", "timestamp": "2024-01-15", "status": "Draft", "parent_id": "P01"},
        "V02": {"name": "Version 2.0 (Final)", "timestamp": "2024-02-01", "status": "Approved", "parent_id": "P01"},
        "V03": {"name": "Version 1.0", "timestamp": "2024-01-15", "status": "Approved", "parent_id": "P02"},
        "V04": {"name": "Version 1.0", "timestamp": "2024-01-15", "status": "Approved", "parent_id": "P03"},
        "V05": {"name": "Version 1.0", "timestamp": "2024-01-15", "status": "Approved", "parent_id": "P04"},
        "V06": {"name": "Version 1.0", "timestamp": "2024-01-15", "status": "Approved", "parent_id": "P05"},
        "V07": {"name": "Version 1.0", "timestamp": "2024-01-15", "status": "Approved", "parent_id": "P06"},
    }
}

# --- 3. INITIALIZE SESSION STATE ---
if "current_view" not in st.session_state:
    st.session_state.current_view = "Dashboard"

if "breadcrumb" not in st.session_state:
    st.session_state.breadcrumb = []  # List of (level, id) tuples


# --- 4. HELPER FUNCTIONS ---
def get_children_key(level):
    """Get the key used to store children in an entity"""
    idx = LEVEL_INDEX[level]
    if idx < len(HIERARCHY_LEVELS) - 1:
        next_level = HIERARCHY_LEVELS[idx + 1]
        return next_level.lower() + "s"
    return None

def get_entity(level, entity_id):
    """Retrieve an entity from the data"""
    return ENTITIES[level].get(entity_id)

def get_parent_info(level, entity_id):
    """Get parent entity info"""
    entity = get_entity(level, entity_id)
    if not entity or "parent_id" not in entity:
        return None
    parent_level = HIERARCHY_LEVELS[LEVEL_INDEX[level] - 1]
    parent = get_entity(parent_level, entity["parent_id"])
    return (parent_level, entity["parent_id"], parent)

def get_children(level, entity_id):
    """Get all children of an entity"""
    entity = get_entity(level, entity_id)
    if not entity or LEVEL_INDEX[level] >= len(HIERARCHY_LEVELS) - 1:
        return []
    
    children_key = get_children_key(level)
    child_ids = entity.get(children_key, [])
    next_level = HIERARCHY_LEVELS[LEVEL_INDEX[level] + 1]
    
    return [(next_level, cid, get_entity(next_level, cid)) for cid in child_ids]


# --- 5. NAVIGATION FUNCTIONS ---
def go_to_dashboard():
    st.session_state.current_view = "Dashboard"
    st.session_state.breadcrumb = []
    st.rerun()

def go_to_entity(level, entity_id):
    """Navigate to a specific entity in the hierarchy"""
    st.session_state.current_view = "Entity Page"
    st.session_state.breadcrumb.append((level, entity_id))
    st.rerun()

def go_back():
    """Go back one level in the hierarchy"""
    if st.session_state.breadcrumb:
        st.session_state.breadcrumb.pop()
    if not st.session_state.breadcrumb:
        st.session_state.current_view = "Dashboard"
    st.rerun()


# --- 6. PAGE RENDERERS ---

def render_dashboard():
    st.title(f"{LEVEL_ICONS['Administrator']} Main Hierarchy Dashboard")
    st.write("Navigate through the organizational structure starting from administrators.")
    
    st.markdown("---")
    st.subheader(f"{LEVEL_ICONS['Administrator']} Level 1: Administrators")
    
    for admin_id, admin_data in ENTITIES["Administrator"].items():
        if st.button(
            f"{admin_data['name']} [{admin_id}]",
            key=f"btn_{admin_id}"
        ):
            go_to_entity("Administrator", admin_id)


def render_entity_page():
    """Render a page for any entity in the hierarchy"""
    if not st.session_state.breadcrumb:
        go_to_dashboard()
        return
    
    current_level, current_id = st.session_state.breadcrumb[-1]
    entity = get_entity(current_level, current_id)
    
    if not entity:
        st.error(f"Entity not found: {current_level} {current_id}")
        if st.button("⬅️ Back"):
            go_back()
        return
    
    level_index = LEVEL_INDEX[current_level]
    icon = LEVEL_ICONS.get(current_level, "📋")
    
    # --- Header ---
    st.title(f"Level {level_index + 1}: {icon} {current_level} Profile")
    st.caption(f"ID: {current_id}")
    
    # --- Navigation buttons ---
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("⬅️ Back"):
            go_back()
    with col2:
        if st.button("🏠 Dashboard"):
            go_to_dashboard()
    
    st.markdown("---")
    
    # --- Breadcrumb trail ---
    if st.session_state.breadcrumb:
        breadcrumb_items = []
        for lvl, eid in st.session_state.breadcrumb:
            entity_data = get_entity(lvl, eid)
            breadcrumb_items.append(f"{LEVEL_ICONS.get(lvl, '📋')} {entity_data['name']}")
        breadcrumb_text = " → ".join(breadcrumb_items)
        st.caption(f"📍 Path: {breadcrumb_text}")
    
    st.markdown("---")
    
    # --- Parent info if exists ---
    if level_index > 0:
        parent_info = get_parent_info(current_level, current_id)
        if parent_info:
            parent_level, parent_id, parent_data = parent_info
            parent_icon = LEVEL_ICONS.get(parent_level, "📋")
            st.info(f"🔗 **Parent:** {parent_icon} {parent_level} '{parent_data['name']}' [{parent_id}]")
    
    # --- Entity details ---
    st.subheader("📋 Details")
    details_displayed = False
    for key, value in entity.items():
        if key not in ["parent_id"] and not isinstance(value, list):
            st.write(f"**{key.replace('_', ' ').title()}:** {value}")
            details_displayed = True
    
    if not details_displayed:
        st.write("*(No additional details)*")
    
    st.markdown("---")
    
    # --- Children if they exist ---
    children = get_children(current_level, current_id)
    if children:
        next_level = HIERARCHY_LEVELS[level_index + 1]
        next_icon = LEVEL_ICONS.get(next_level, "📋")
        
        st.subheader(f"👇 Attached {next_level}s")
        st.write(f"This {current_level} contains {len(children)} {next_level.lower()}(s):")
        st.markdown("")
        
        for child_level, child_id, child_data in children:
            child_icon = LEVEL_ICONS.get(child_level, "📋")
            if child_data:
                if st.button(
                    f"{child_icon} {child_data['name']} [{child_id}]",
                    key=f"child_{child_id}"
                ):
                    go_to_entity(child_level, child_id)
    else:
        st.markdown("---")
        st.write("✓ *This is the lowest level in the hierarchy (no child entities)*")


# --- 7. ROUTER ---
if st.session_state.current_view == "Dashboard":
    render_dashboard()
elif st.session_state.current_view == "Entity Page":
    render_entity_page()


