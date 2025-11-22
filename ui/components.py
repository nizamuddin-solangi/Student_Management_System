"""
UI Components
Streamlit components for the user interface
"""

import streamlit as st
import pandas as pd

GRADES = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
          'KG', 'Nursery', 'Pre-K', 'Freshman', 'Sophomore', 'Junior', 'Senior']

PERFORMANCE_LEVELS = ['Excellent', 'Good', 'Average', 'Below Average', 'Poor']

def render_student_table(students):
    """
    Render students in a table format
    
    Args:
        students (list): List of Student objects
    """
    if not students:
        st.info("No students to display")
        return
    
    # Convert to DataFrame
    data = []
    for student in students:
        data.append({
            'ID': student.student_id,
            'Name': student.name,
            'Age': student.age,
            'Grade': student.grade,
            'Email': student.email,
            'Phone': student.phone,
            'Performance': student.performance
        })
    
    df = pd.DataFrame(data)
    
    # Display table with styling
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

def render_add_student_form(manager):
    """
    Render form to add a new student
    
    Args:
        manager (StudentManager): Student manager instance
    """
    with st.form("add_student_form", clear_on_submit=True):
        st.subheader("Enter Student Details")
        
        col1, col2 = st.columns(2)
        
        with col1:
            student_id = st.text_input(
                "Student ID *",
                placeholder="e.g., STU001",
                help="Unique identifier for the student"
            )
            name = st.text_input(
                "Full Name *",
                placeholder="e.g., John Doe",
                help="Student's full name"
            )
            age = st.number_input(
                "Age *",
                min_value=5,
                max_value=100,
                value=15,
                help="Student's age in years"
            )
            grade = st.selectbox(
                "Grade *",
                options=GRADES,
                help="Current grade/class"
            )
        
        with col2:
            email = st.text_input(
                "Email *",
                placeholder="e.g., student@example.com",
                help="Student's email address"
            )
            phone = st.text_input(
                "Phone Number *",
                placeholder="e.g., +1234567890",
                help="Contact number"
            )
            performance = st.selectbox(
                "Performance Level *",
                options=PERFORMANCE_LEVELS,
                help="Academic performance rating"
            )
        
        submitted = st.form_submit_button("➕ Add Student", type="primary", use_container_width=True)
        
        if submitted:
            success, message = manager.add_student(
                student_id, name, age, grade, email, phone, performance
            )
            
            if success:
                st.success(f"✅ {message}")
                st.balloons()
            else:
                st.error("❌ Failed to add student:")
                for error in message:
                    st.error(f"• {error}")

def render_update_student_form(manager):
    """
    Render form to update existing student
    
    Args:
        manager (StudentManager): Student manager instance
    """
    students = manager.get_all_students()
    
    if not students:
        st.warning("No students available to update.")
        return
    
    # Select student
    student_options = {f"{s.student_id} - {s.name}": s.student_id for s in students}
    selected = st.selectbox(
        "Select Student to Update",
        options=list(student_options.keys())
    )
    
    if selected:
        student_id = student_options[selected]
        student = manager.get_student_by_id(student_id)
        
        if student:
            st.info(f"Updating: **{student.name}** (ID: {student.student_id})")
            
            with st.form("update_student_form"):
                st.subheader("Update Student Details")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    name = st.text_input("Full Name *", value=student.name)
                    age = st.number_input(
                        "Age *",
                        min_value=5,
                        max_value=100,
                        value=student.age
                    )
                    grade = st.selectbox(
                        "Grade *",
                        options=GRADES,
                        index=GRADES.index(student.grade) if student.grade in GRADES else 0
                    )
                
                with col2:
                    email = st.text_input("Email *", value=student.email)
                    phone = st.text_input("Phone Number *", value=student.phone)
                    performance = st.selectbox(
                        "Performance Level *",
                        options=PERFORMANCE_LEVELS,
                        index=PERFORMANCE_LEVELS.index(student.performance)
                    )
                
                submitted = st.form_submit_button("💾 Update Student", type="primary", use_container_width=True)
                
                if submitted:
                    success, message = manager.update_student(
                        student_id, name, age, grade, email, phone, performance
                    )
                    
                    if success:
                        st.success(f"✅ {message}")
                        st.rerun()
                    else:
                        st.error("❌ Failed to update student:")
                        for error in message:
                            st.error(f"• {error}")

def render_search_filters(manager):
    """
    Render search and filter options
    
    Args:
        manager (StudentManager): Student manager instance
    """
    st.subheader("Search Options")
    
    # Search by text
    search_query = st.text_input(
        "🔍 Search by Name, ID, or Email",
        placeholder="Type to search..."
    )
    
    st.markdown("---")
    st.subheader("Filter Options")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        filter_grade = st.selectbox(
            "Filter by Grade",
            options=["All"] + GRADES
        )
    
    with col2:
        filter_performance = st.selectbox(
            "Filter by Performance",
            options=["All"] + PERFORMANCE_LEVELS
        )
    
    with col3:
        age_range = st.slider(
            "Filter by Age Range",
            min_value=5,
            max_value=100,
            value=(5, 100)
        )
    
    # Apply filters
    filtered_students = manager.get_all_students()
    
    # Text search
    if search_query:
        filtered_students = manager.search_students(search_query)
    
    # Grade filter
    if filter_grade != "All":
        filtered_students = [s for s in filtered_students if s.grade == filter_grade]
    
    # Performance filter
    if filter_performance != "All":
        filtered_students = [s for s in filtered_students if s.performance == filter_performance]
    
    # Age range filter
    filtered_students = [s for s in filtered_students 
                        if age_range[0] <= s.age <= age_range[1]]
    
    st.markdown("---")
    st.subheader(f"Results ({len(filtered_students)} students)")
    
    if filtered_students:
        render_student_table(filtered_students)
    else:
        st.warning("No students match the search criteria.")
    
    # Statistics
    if filtered_students:
        st.markdown("---")
        st.subheader("📊 Statistics")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Students", len(filtered_students))
        
        with col2:
            avg_age = sum(s.age for s in filtered_students) / len(filtered_students)
            st.metric("Average Age", f"{avg_age:.1f}")
        
        with col3:
            # Count unique grades
            unique_grades = len(set(s.grade for s in filtered_students))
            st.metric("Grades Represented", unique_grades)
        
        with col4:
            # Count excellent performers
            excellent = len([s for s in filtered_students if s.performance == "Excellent"])
            st.metric("Excellent Performers", excellent)

def render_statistics_dashboard(manager):
    """
    Render statistics dashboard
    
    Args:
        manager (StudentManager): Student manager instance
    """
    stats = manager.get_statistics()
    
    st.header("📊 System Statistics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Total Students", stats['total'])
        st.metric("Average Age", stats['avg_age'])
    
    with col2:
        if stats['performance_distribution']:
            st.subheader("Performance Distribution")
            perf_df = pd.DataFrame(
                list(stats['performance_distribution'].items()),
                columns=['Performance', 'Count']
            )
            st.bar_chart(perf_df.set_index('Performance'))
    
    if stats['grade_distribution']:
        st.subheader("Grade Distribution")
        grade_df = pd.DataFrame(
            list(stats['grade_distribution'].items()),
            columns=['Grade', 'Count']
        )
        st.bar_chart(grade_df.set_index('Grade'))