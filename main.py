import streamlit as st
from services.student_manager import StudentManager
from ui.components import (
    render_add_student_form, 
    render_update_student_form, 
    render_student_table, 
    render_search_filters,
    render_dashboard_header,
    render_statistics_overview
)

# Page configuration with custom theme
st.set_page_config(
    page_title="Student Management System",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Premium CSS Styling
st.markdown("""
<style>
    /* Import Premium Font */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Poppins', sans-serif !important;
    }
    
    /* Main Background - Sophisticated Gradient */
    .main {
        background: linear-gradient(to bottom right, #0f172a, #1e293b, #334155);
        min-height: 100vh;
    }
    
    /* Content Container - Glass Effect */
    .block-container {
        background: rgba(255, 255, 255, 0.98);
        backdrop-filter: blur(20px);
        border-radius: 24px;
        padding: 2.5rem !important;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* Sidebar - Premium Dark */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }
    
    [data-testid="stSidebar"] * {
        color: rgba(255, 255, 255, 0.95) !important;
    }
    
    /* Sidebar Logo Area */
    [data-testid="stSidebar"] > div:first-child {
        padding-top: 2rem;
    }
    
    /* Sidebar Title */
    [data-testid="stSidebar"] h3 {
        color: white !important;
        font-weight: 700;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        padding: 1.5rem 1rem 1rem 1rem;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 1rem;
    }
    
    /* Radio Navigation Buttons */
    [data-testid="stSidebar"] .stRadio > div {
        gap: 0.5rem;
    }
    
    [data-testid="stSidebar"] .stRadio label {
        background: rgba(255, 255, 255, 0.03);
        padding: 1rem 1.25rem;
        border-radius: 12px;
        color: rgba(255, 255, 255, 0.7) !important;
        font-weight: 500;
        font-size: 0.9rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        cursor: pointer;
        border: 1px solid transparent;
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }
    
    [data-testid="stSidebar"] .stRadio label:hover {
        background: rgba(255, 255, 255, 0.08);
        transform: translateX(4px);
        border-color: rgba(255, 255, 255, 0.1);
        color: white !important;
    }
    
    [data-testid="stSidebar"] .stRadio input:checked + label {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        border-color: rgba(59, 130, 246, 0.5);
        box-shadow: 0 8px 16px rgba(59, 130, 246, 0.3);
        color: white !important;
        font-weight: 600;
    }
    
    /* Headers - Premium Typography */
    h1 {
        color: #0f172a;
        font-weight: 800;
        font-size: 2.75rem;
        margin-bottom: 0.5rem;
        letter-spacing: -0.03em;
        line-height: 1.2;
    }
    
    h2 {
        color: #1e293b;
        font-weight: 700;
        font-size: 1.875rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
        letter-spacing: -0.02em;
    }
    
    h3 {
        color: #334155;
        font-weight: 600;
        font-size: 1.25rem;
        margin-bottom: 1rem;
    }
    
    /* Premium Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.875rem 2rem;
        font-weight: 600;
        font-size: 0.95rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 4px 14px rgba(59, 130, 246, 0.4);
        text-transform: none;
        letter-spacing: 0.3px;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(59, 130, 246, 0.5);
        background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    /* Input Fields - Modern Design */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input,
    .stSelectbox > div > div > select {
        border-radius: 10px;
        border: 1.5px solid #e2e8f0;
        padding: 0.75rem 1rem;
        font-size: 0.95rem;
        transition: all 0.3s ease;
        background: #f8fafc;
        color: #1e293b;
    }
    
    .stTextInput > div > div > input:focus,
    .stNumberInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus {
        border-color: #3b82f6;
        background: white;
        box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.1);
        outline: none;
    }
    
    /* Labels - Clean Typography */
    .stTextInput > label,
    .stNumberInput > label,
    .stSelectbox > label {
        color: #334155;
        font-weight: 600;
        font-size: 0.875rem;
        margin-bottom: 0.5rem;
        letter-spacing: 0.3px;
    }
    
    /* DataFrames - Modern Table */
    [data-testid="stDataFrame"] {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        border: 1px solid #e2e8f0;
    }
    
    /* Metrics - Elegant Cards */
    [data-testid="stMetricValue"] {
        font-size: 2.25rem;
        font-weight: 800;
        color: #0f172a;
        letter-spacing: -0.02em;
    }
    
    [data-testid="stMetricLabel"] {
        color: #64748b;
        font-weight: 600;
        font-size: 0.875rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    [data-testid="stMetricDelta"] {
        font-size: 0.875rem;
        font-weight: 600;
    }
    
    /* Forms - Premium Container */
    [data-testid="stForm"] {
        background: linear-gradient(to bottom, #f8fafc, #f1f5f9);
        border-radius: 16px;
        padding: 2rem;
        border: 1px solid #e2e8f0;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
    }
    
    /* Alerts - Modern Design */
    .stAlert {
        border-radius: 12px;
        border: none;
        padding: 1.25rem 1.5rem;
        font-weight: 500;
        font-size: 0.95rem;
    }
    
    /* Success Alert */
    .stSuccess {
        background: linear-gradient(135deg, #ecfdf5, #d1fae5);
        border-left: 4px solid #10b981;
        color: #065f46;
    }
    
    /* Info Alert */
    .stInfo {
        background: linear-gradient(135deg, #eff6ff, #dbeafe);
        border-left: 4px solid #3b82f6;
        color: #1e40af;
    }
    
    /* Warning Alert */
    .stWarning {
        background: linear-gradient(135deg, #fffbeb, #fef3c7);
        border-left: 4px solid #f59e0b;
        color: #92400e;
    }
    
    /* Error Alert */
    .stError {
        background: linear-gradient(135deg, #fef2f2, #fee2e2);
        border-left: 4px solid #ef4444;
        color: #991b1b;
    }
    
    /* Dividers */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(to right, transparent, #e2e8f0, transparent);
        margin: 2rem 0;
    }
    
    /* Slider */
    .stSlider > div > div > div > div {
        background: #3b82f6 !important;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
        background: transparent;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 10px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        background: #f1f5f9;
        color: #64748b;
        border: none;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #3b82f6, #2563eb);
        color: white;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
    }
    
    /* Scrollbar - Minimalist */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f5f9;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #3b82f6, #2563eb);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #2563eb, #1e40af);
    }
    
    /* Animations */
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .main > div > div {
        animation: slideIn 0.5s ease-out;
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Hide sidebar collapse button and text */
    [data-testid="collapsedControl"] {
        display: none;
    }
    
    button[kind="header"] {
        display: none;
    }
    
    /* Hide the collapse arrow in sidebar */
    [data-testid="stSidebar"] button[aria-label] {
        display: none !important;
    }
    
    /* Force all text to black */
    .main * {
        color: #000000 !important;
    }
    
    /* Force input backgrounds to white */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input,
    .stSelectbox > div > div > select,
    .stTextArea > div > div > textarea,
    [data-baseweb="select"] > div,
    [data-baseweb="input"] > div {
        background-color: #ffffff !important;
        color: #000000 !important;
    }
    
    /* Force dropdown options to white background */
    [data-baseweb="popover"] {
        background-color: #ffffff !important;
    }
    
    [data-baseweb="menu"] {
        background-color: #ffffff !important;
    }
    
    [data-baseweb="menu"] li {
        background-color: #ffffff !important;
        color: #000000 !important;
    }
    
    [data-baseweb="menu"] li:hover {
        background-color: #f3f4f6 !important;
    }
    
    /* Selectbox dropdown - force white background and black text */
    [data-baseweb="select"] {
        background-color: #ffffff !important;
    }
    
    [data-baseweb="select"] > div {
        background-color: #ffffff !important;
        color: #000000 !important;
    }
    
    [data-baseweb="select"] input {
        background-color: #ffffff !important;
        color: #000000 !important;
    }
    
    [data-baseweb="select"] svg {
        color: #000000 !important;
    }
    
    /* Dropdown list items */
    [role="listbox"] {
        background-color: #ffffff !important;
    }
    
    [role="option"] {
        background-color: #ffffff !important;
        color: #000000 !important;
    }
    
    [role="option"]:hover {
        background-color: #f3f4f6 !important;
        color: #000000 !important;
    }
    
    /* Selected option in dropdown */
    [aria-selected="true"] {
        background-color: #e5e7eb !important;
        color: #000000 !important;
    }
    
    /* Dropdown container */
    [data-baseweb="popover"] > div {
        background-color: #ffffff !important;
    }
    
    /* Multi-select and all select variants */
    .stSelectbox [data-baseweb="select"] {
        background-color: #ffffff !important;
    }
    
    .stSelectbox [data-baseweb="select"] * {
        color: #000000 !important;
    }
    
    /* Dropdown arrow icon */
    .stSelectbox svg {
        color: #000000 !important;
    }
    
    /* Force all headings to black */
    h1, h2, h3, h4, h5, h6 {
        color: #000000 !important;
    }
    
    /* Force paragraph text to black */
    p, span, div, label {
        color: #000000 !important;
    }
    
    /* Force dataframe text to black */
    [data-testid="stDataFrame"] * {
        color: #000000 !important;
    }
    
    /* Force metric values to black */
    [data-testid="stMetricValue"] {
        color: #000000 !important;
    }
    
    [data-testid="stMetricLabel"] {
        color: #000000 !important;
    }
    
    /* Force form text to black */
    [data-testid="stForm"] * {
        color: #000000 !important;
    }
    
    /* Exception: Keep sidebar text white */
    [data-testid="stSidebar"] * {
        color: rgba(255, 255, 255, 0.95) !important;
    }
    
    /* Exception: Keep button text white */
    .stButton > button {
        color: #ffffff !important;
    }
    
    /* Exception: Keep alert text appropriate colors */
    .stSuccess * {
        color: #065f46 !important;
    }
    
    .stInfo * {
        color: #1e40af !important;
    }
    
    .stWarning * {
        color: #92400e !important;
    }
    
    .stError * {
        color: #991b1b !important;
    }
    
    /* Exception: Keep custom HTML card text as designed */
    [style*="background: linear-gradient"] * {
        color: inherit !important;
    }
    
    /* Selectbox dropdown text */
    [data-baseweb="select"] input {
        color: #000000 !important;
    }
    
    /* Placeholder text */
    ::placeholder {
        color: #6b7280 !important;
        opacity: 1;
    }
    
    :-ms-input-placeholder {
        color: #6b7280 !important;
    }
    
    ::-ms-input-placeholder {
        color: #6b7280 !important;
    }
    
    /* Selectbox Dropdown */
    [data-baseweb="select"] {
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize student manager
if 'manager' not in st.session_state:
    st.session_state.manager = StudentManager()

# Dashboard Header
render_dashboard_header()

# Sidebar navigation
with st.sidebar:
    st.markdown("### 🎯 NAVIGATION")
    page = st.radio(
        "Links",
        ["📊 Dashboard", "👥 All Students", "➕ Add Student", "✏️ Update Student", "🗑️ Delete Student", "🔍 Search & Filter"],
        label_visibility="collapsed"
    )

# Dashboard
if page == "📊 Dashboard":
    render_statistics_overview(st.session_state.manager)

# View All Students
elif page == "👥 All Students":
    st.markdown("## 👥 Student Directory")
    students = st.session_state.manager.get_all_students()
    
    if students:
        col1, col2, col3 = st.columns([2, 2, 1])
        with col1:
            st.metric("📚 Total Students", len(students))
        with col2:
            avg_age = sum(s.age for s in students) / len(students)
            st.metric("👶 Average Age", f"{avg_age:.1f} years")
        with col3:
            excellent = len([s for s in students if s.performance == "Excellent"])
            st.metric("⭐ Excellence", excellent)
        
        st.markdown("---")
        render_student_table(students)
    else:
        st.info("🎓 No students enrolled yet. Start by adding your first student!")

# Add Student
elif page == "➕ Add Student":
    st.markdown("## ➕ Enroll New Student")
    st.markdown("*Complete the form below to register a new student*")
    render_add_student_form(st.session_state.manager)

# Update Student
elif page == "✏️ Update Student":
    st.markdown("## ✏️ Update Student Records")
    st.markdown("*Select a student to modify their information*")
    render_update_student_form(st.session_state.manager)

# Delete Student
elif page == "🗑️ Delete Student":
    st.markdown("## 🗑️ Remove Student")
    st.markdown("*Permanently remove a student from the system*")
    students = st.session_state.manager.get_all_students()
    
    if students:
        student_options = {f"{s.student_id} - {s.name}": s.student_id for s in students}
        selected = st.selectbox("📋 Select Student to Remove", options=list(student_options.keys()))
        
        if selected:
            student_id = student_options[selected]
            student = st.session_state.manager.get_student_by_id(student_id)
            
            if student:
                st.markdown("---")
                st.markdown("### 📝 Student Information")
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown(f"**👤 Name:** {student.name}")
                    st.markdown(f"**🎂 Age:** {student.age} years")
                with col2:
                    st.markdown(f"**📚 Grade:** {student.grade}")
                    st.markdown(f"**📧 Email:** {student.email}")
                with col3:
                    st.markdown(f"**📱 Phone:** {student.phone}")
                    st.markdown(f"**⭐ Performance:** {student.performance}")
                
                st.markdown("---")
                st.warning("⚠️ **Warning:** This action is permanent and cannot be undone.")
                
                # Initialize confirmation state
                if 'delete_confirmation' not in st.session_state:
                    st.session_state.delete_confirmation = False
                if 'selected_student_for_deletion' not in st.session_state:
                    st.session_state.selected_student_for_deletion = None
                
                # Reset confirmation if different student selected
                if st.session_state.selected_student_for_deletion != student_id:
                    st.session_state.delete_confirmation = False
                    st.session_state.selected_student_for_deletion = student_id
                
                col1, col2, col3 = st.columns([1, 1, 2])
                
                if not st.session_state.delete_confirmation:
                    # First click - Ask for confirmation
                    with col1:
                        if st.button("🗑️ Delete Student", type="primary", use_container_width=True):
                            st.session_state.delete_confirmation = True
                            st.rerun()
                else:
                    # Second click - Confirm deletion
                    st.error("### ⚠️ Are you absolutely sure?")
                    st.markdown("**This will permanently delete the student. This action cannot be undone.**")
                    
                    col_a, col_b, col_c = st.columns([1, 1, 1])
                    with col_a:
                        if st.button("✅ Yes, Delete", type="primary", use_container_width=True):
                            student_name = student.name
                            if st.session_state.manager.delete_student(student_id):
                                from ui.components import show_popup
                                # Reset confirmation state
                                st.session_state.delete_confirmation = False
                                st.session_state.selected_student_for_deletion = None
                                show_popup(
                                    "Student Removed",
                                    f"✅ {student_name} has been successfully removed from the system.",
                                    icon="🗑️",
                                    type="success"
                                )
                                import time
                                time.sleep(1)
                                st.rerun()
                            else:
                                st.error("❌ Unable to delete student. Please try again.")
                    
                    with col_b:
                        if st.button("❌ Cancel", use_container_width=True):
                            st.session_state.delete_confirmation = False
                            st.rerun()
    else:
        st.info("🎓 No students available to remove.")

# Search & Filter
elif page == "🔍 Search & Filter":
    st.markdown("## 🔍 Advanced Search")
    st.markdown("*Find students using filters and search criteria*")
    render_search_filters(st.session_state.manager)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #94a3b8; padding: 1.5rem 0; font-weight: 500;'>
    <p style='font-size: 0.875rem; margin-bottom: 0.5rem;'>Student Management System • Premium Edition</p>
    <p style='font-size: 0.75rem; color: #cbd5e1;'>Built with Python & Streamlit • © 2024</p>
</div>
""", unsafe_allow_html=True)