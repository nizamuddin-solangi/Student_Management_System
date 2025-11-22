import streamlit as st
from services.student_manager import StudentManager
from ui.components import render_add_student_form, render_update_student_form, render_student_table, render_search_filters

# Page configuration
st.set_page_config(
    page_title="Student Management System",
    page_icon="🎓",
    layout="wide"
)

# Initialize student manager
if 'manager' not in st.session_state:
    st.session_state.manager = StudentManager()

# Main title
st.title("🎓 Student Management System")
st.markdown("---")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select Operation",
    ["View All Students", "Add Student", "Update Student", "Delete Student", "Search & Filter"]
)

# View All Students
if page == "View All Students":
    st.header("📋 All Students")
    students = st.session_state.manager.get_all_students()
    
    if students:
        render_student_table(students)
        st.info(f"Total Students: {len(students)}")
    else:
        st.warning("No students found in the system.")

# Add Student
elif page == "Add Student":
    st.header("➕ Add New Student")
    render_add_student_form(st.session_state.manager)

# Update Student
elif page == "Update Student":
    st.header("✏️ Update Student")
    render_update_student_form(st.session_state.manager)

# Delete Student
elif page == "Delete Student":
    st.header("🗑️ Delete Student")
    students = st.session_state.manager.get_all_students()
    
    if students:
        student_options = {f"{s.student_id} - {s.name}": s.student_id for s in students}
        selected = st.selectbox("Select Student to Delete", options=list(student_options.keys()))
        
        if selected:
            student_id = student_options[selected]
            student = st.session_state.manager.get_student_by_id(student_id)
            
            if student:
                st.write("**Student Details:**")
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"**Name:** {student.name}")
                    st.write(f"**Age:** {student.age}")
                    st.write(f"**Grade:** {student.grade}")
                with col2:
                    st.write(f"**Email:** {student.email}")
                    st.write(f"**Phone:** {student.phone}")
                    st.write(f"**Performance:** {student.performance}")
                
                st.warning("⚠️ This action cannot be undone!")
                
                if st.button("🗑️ Confirm Delete", type="primary"):
                    if st.session_state.manager.delete_student(student_id):
                        st.success(f"✅ Student {student.name} deleted successfully!")
                        st.rerun()
                    else:
                        st.error("❌ Failed to delete student.")
    else:
        st.warning("No students available to delete.")

# Search & Filter
elif page == "Search & Filter":
    st.header("🔍 Search & Filter Students")
    render_search_filters(st.session_state.manager)

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Python OOP and Streamlit")