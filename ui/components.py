"""
Premium UI Components
Streamlit components with sophisticated design
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import time



GRADES = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
          'KG', 'Nursery', 'Pre-K', 'Freshman', 'Sophomore', 'Junior', 'Senior']

PERFORMANCE_LEVELS = ['Excellent', 'Good', 'Average', 'Below Average', 'Poor']

PERFORMANCE_COLORS = {
    'Excellent': '#10b981',
    'Good': '#3b82f6',
    'Average': '#f59e0b',
    'Below Average': '#f97316',
    'Poor': '#ef4444'
}

def show_popup(title, message, icon="✅", type="success"):
    """Show elegant popup notification"""
    if type == "success":
        st.success(f"{icon} **{title}**\n\n{message}")
    elif type == "error":
        st.error(f"{icon} **{title}**\n\n{message}")
    elif type == "warning":
        st.warning(f"{icon} **{title}**\n\n{message}")
    elif type == "info":
        st.info(f"{icon} **{title}**\n\n{message}")
    
    time.sleep(0.5)

def render_dashboard_header():
    """Render sophisticated dashboard header"""
    st.markdown("""
    <div style='text-align: center; padding: 1rem 0 2.5rem 0;'>
        <h1 style='font-size: 2.5rem; font-weight: 800; margin-bottom: 0.75rem; 
                   background: linear-gradient(135deg, #0f172a 0%, #334155 100%);
                   -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>
            🎓 Student Management System
        </h1>
        <p style='font-size: 1rem; color: #64748b; font-weight: 500; letter-spacing: 0.5px;'>
            Enterprise-Grade Academic Administration Platform
        </p>
    </div>
    """, unsafe_allow_html=True)

def render_student_table(students):
    """Render students in elegant table format"""
    if not students:
        st.info("📚 No students to display")
        return
    
    data = []
    for student in students:
        data.append({
            '🆔 ID': student.student_id,
            '👤 Name': student.name,
            '🎂 Age': student.age,
            '📚 Grade': student.grade,
            '📧 Email': student.email,
            '📱 Phone': student.phone,
            '⭐ Performance': student.performance
        })
    
    df = pd.DataFrame(data)
    
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        height=450
    )

def render_add_student_form(manager):
    """Render premium enrollment form"""
    with st.form("add_student_form", clear_on_submit=True):
        st.markdown("### 📋 Student Information")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 🔖 Personal Details")
            student_id = st.text_input(
                "Student ID",
                placeholder="e.g., STU001",
                help="Unique identifier"
            )
            name = st.text_input(
                "Full Name",
                placeholder="e.g., John Smith",
                help="Complete legal name"
            )
            age = st.number_input(
                "Age",
                min_value=5,
                max_value=100,
                value=15,
                help="Current age in years"
            )
            grade = st.selectbox(
                "Grade Level",
                options=GRADES,
                help="Academic grade"
            )
        
        with col2:
            st.markdown("#### 📞 Contact Details")
            email = st.text_input(
                "Email Address",
                placeholder="student@example.com",
                help="Primary email"
            )
            phone = st.text_input(
                "Phone Number",
                placeholder="+1 (234) 567-8900",
                help="Contact number"
            )
            performance = st.selectbox(
                "Academic Performance",
                options=PERFORMANCE_LEVELS,
                help="Current performance level"
            )
        
        st.markdown("---")
        
        col1, col2, col3 = st.columns([1, 1, 2])
        with col2:
            submitted = st.form_submit_button(
                "➕ Enroll Student", 
                type="primary", 
                use_container_width=True
            )
        
        if submitted:
            success, message = manager.add_student(
                student_id, name, age, grade, email, phone, performance
            )
            
            if success:
                show_popup(
                    "Student Enrolled Successfully",
                    f"✅ {name} has been added to the system.\n\n"
                    f"Student ID: {student_id}\n"
                    f"Grade: {grade} | Performance: {performance}",
                    icon="🎉",
                    type="success"
                )
                time.sleep(1)
                st.rerun()
            else:
                show_popup(
                    "Enrollment Failed",
                    "Please correct the following errors:",
                    icon="❌",
                    type="error"
                )
                for error in message:
                    st.error(f"• {error}")

def render_update_student_form(manager):
    """Render premium update form"""
    students = manager.get_all_students()
    
    if not students:
        st.warning("🎓 No students available. Please add students first.")
        return
    
    student_options = {f"🆔 {s.student_id} - 👤 {s.name}": s.student_id for s in students}
    selected = st.selectbox(
        "Select Student to Update",
        options=list(student_options.keys()),
        help="Choose student to modify"
    )
    
    if selected:
        student_id = student_options[selected]
        student = manager.get_student_by_id(student_id)
        
        if student:
            st.markdown(f"""
            <div style='background: linear-gradient(135deg, #eff6ff, #dbeafe); 
                        padding: 1.5rem; border-radius: 12px; margin: 1.5rem 0;
                        border-left: 4px solid #3b82f6;'>
                <h4 style='margin: 0; color: #1e3a8a; font-weight: 700;'>Currently Editing</h4>
                <p style='margin: 0.75rem 0 0 0; color: #475569; font-size: 0.95rem;'>
                    <strong>{student.name}</strong> • ID: {student.student_id} • Grade: {student.grade}
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            with st.form("update_student_form"):
                st.markdown("### 📝 Update Information")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("#### 🔖 Personal Details")
                    name = st.text_input("Full Name", value=student.name)
                    age = st.number_input(
                        "Age",
                        min_value=5,
                        max_value=100,
                        value=student.age
                    )
                    grade = st.selectbox(
                        "Grade Level",
                        options=GRADES,
                        index=GRADES.index(student.grade) if student.grade in GRADES else 0
                    )
                
                with col2:
                    st.markdown("#### 📞 Contact Details")
                    email = st.text_input("Email Address", value=student.email)
                    phone = st.text_input("Phone Number", value=student.phone)
                    performance = st.selectbox(
                        "Academic Performance",
                        options=PERFORMANCE_LEVELS,
                        index=PERFORMANCE_LEVELS.index(student.performance)
                    )
                
                st.markdown("---")
                
                col1, col2, col3 = st.columns([1, 1, 2])
                with col2:
                    submitted = st.form_submit_button(
                        "💾 Save Changes", 
                        type="primary", 
                        use_container_width=True
                    )
                
                if submitted:
                    success, message = manager.update_student(
                        student_id, name, age, grade, email, phone, performance
                    )
                    
                    if success:
                        show_popup(
                            "Student Updated Successfully",
                            f"✅ {name}'s information has been updated.\n\n"
                            f"Student ID: {student_id}\n"
                            f"Grade: {grade} | Performance: {performance}",
                            icon="💾",
                            type="success"
                        )
                        time.sleep(1)
                        st.rerun()
                    else:
                        show_popup(
                            "Update Failed",
                            "Please correct the following errors:",
                            icon="❌",
                            type="error"
                        )
                        for error in message:
                            st.error(f"• {error}")

def render_search_filters(manager):
    """Render sophisticated search interface"""
    st.markdown("### 🔎 Quick Search")
    search_query = st.text_input(
        "",
        placeholder="🔍 Search by name, ID, or email...",
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("### 🎯 Advanced Filters")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        filter_grade = st.selectbox(
            "📚 Grade Level",
            options=["All Grades"] + GRADES
        )
    
    with col2:
        filter_performance = st.selectbox(
            "⭐ Performance",
            options=["All Levels"] + PERFORMANCE_LEVELS
        )
    
    with col3:
        age_range = st.slider(
            "🎂 Age Range",
            min_value=5,
            max_value=100,
            value=(5, 100)
        )
    
    filtered_students = manager.get_all_students()
    
    if search_query:
        filtered_students = manager.search_students(search_query)
    
    if filter_grade != "All Grades":
        filtered_students = [s for s in filtered_students if s.grade == filter_grade]
    
    if filter_performance != "All Levels":
        filtered_students = [s for s in filtered_students if s.performance == filter_performance]
    
    filtered_students = [s for s in filtered_students 
                        if age_range[0] <= s.age <= age_range[1]]
    
    st.markdown("---")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"### 📋 Results")
    with col2:
        st.markdown(f"<div style='text-align: right; padding-top: 0.5rem;'>"
                   f"<span style='background: linear-gradient(135deg, #3b82f6, #2563eb); "
                   f"color: white; padding: 0.5rem 1.25rem; border-radius: 20px; font-weight: 600; font-size: 0.9rem;'>"
                   f"{len(filtered_students)} Found</span></div>", unsafe_allow_html=True)
    
    if filtered_students:
        render_student_table(filtered_students)
        
        st.markdown("---")
        st.markdown("### 📊 Search Statistics")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("👥 Total", len(filtered_students))
        
        with col2:
            avg_age = sum(s.age for s in filtered_students) / len(filtered_students)
            st.metric("🎂 Avg Age", f"{avg_age:.1f}")
        
        with col3:
            unique_grades = len(set(s.grade for s in filtered_students))
            st.metric("📚 Grades", unique_grades)
        
        with col4:
            excellent = len([s for s in filtered_students if s.performance == "Excellent"])
            st.metric("⭐ Top", excellent)
    else:
        st.info("🔍 No students match your criteria. Try adjusting the filters.")

def render_statistics_overview(manager):
    """Render comprehensive premium dashboard"""
    students = manager.get_all_students()
    stats = manager.get_statistics()
    
    st.markdown("## 📊 Analytics Dashboard")
    st.markdown(f"*Updated: {datetime.now().strftime('%B %d, %Y • %I:%M %p')}*")
    
    if not students:
        st.info("🎓 No data available. Add students to see comprehensive analytics.")
        return
    
    # Premium Metric Cards
    st.markdown("### 📈 Overview Metrics")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%); 
                    padding: 2rem 1.5rem; border-radius: 16px; text-align: center; color: white;
                    box-shadow: 0 10px 30px rgba(59, 130, 246, 0.3);'>
            <div style='font-size: 2.5rem; font-weight: 800; margin-bottom: 0.5rem;'>{stats['total']}</div>
            <div style='font-size: 0.9rem; opacity: 0.95; font-weight: 500; letter-spacing: 1px;'>TOTAL STUDENTS</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #10b981 0%, #059669 100%); 
                    padding: 2rem 1.5rem; border-radius: 16px; text-align: center; color: white;
                    box-shadow: 0 10px 30px rgba(16, 185, 129, 0.3);'>
            <div style='font-size: 2.5rem; font-weight: 800; margin-bottom: 0.5rem;'>{stats['avg_age']}</div>
            <div style='font-size: 0.9rem; opacity: 0.95; font-weight: 500; letter-spacing: 1px;'>AVERAGE AGE</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        unique_grades = len(stats['grade_distribution'])
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%); 
                    padding: 2rem 1.5rem; border-radius: 16px; text-align: center; color: white;
                    box-shadow: 0 10px 30px rgba(139, 92, 246, 0.3);'>
            <div style='font-size: 2.5rem; font-weight: 800; margin-bottom: 0.5rem;'>{unique_grades}</div>
            <div style='font-size: 0.9rem; opacity: 0.95; font-weight: 500; letter-spacing: 1px;'>GRADE LEVELS</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        excellent_count = stats['performance_distribution'].get('Excellent', 0)
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); 
                    padding: 2rem 1.5rem; border-radius: 16px; text-align: center; color: white;
                    box-shadow: 0 10px 30px rgba(245, 158, 11, 0.3);'>
            <div style='font-size: 2.5rem; font-weight: 800; margin-bottom: 0.5rem;'>{excellent_count}</div>
            <div style='font-size: 0.9rem; opacity: 0.95; font-weight: 500; letter-spacing: 1px;'>TOP PERFORMERS</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Secondary Metrics
    st.markdown("### 📊 Detailed Analytics")
    col1, col2, col3, col4, col5 = st.columns(5)
    
    good_performers = len([s for s in students if s.performance in ['Excellent', 'Good']])
    poor_performers = len([s for s in students if s.performance in ['Below Average', 'Poor']])
    youngest = min(s.age for s in students)
    oldest = max(s.age for s in students)
    median_age = sorted([s.age for s in students])[len(students)//2]
    
    with col1:
        st.metric("🟢 High Achievers", good_performers, 
                 delta=f"{(good_performers/len(students)*100):.0f}%")
    
    with col2:
        st.metric("🔴 Need Support", poor_performers,
                 delta=f"{(poor_performers/len(students)*100):.0f}%",
                 delta_color="inverse")
    
    with col3:
        st.metric("👶 Youngest", f"{youngest} yrs")
    
    with col4:
        st.metric("👴 Oldest", f"{oldest} yrs")
    
    with col5:
        st.metric("📊 Median", f"{median_age} yrs")
    
    st.markdown("---")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🎯 Performance Analysis")
        if stats['performance_distribution']:
            perf_df = pd.DataFrame(
                list(stats['performance_distribution'].items()),
                columns=['Level', 'Count']
            )
            perf_df['Percentage'] = (perf_df['Count'] / perf_df['Count'].sum() * 100).round(1)
            perf_df['Color'] = perf_df['Level'].map(PERFORMANCE_COLORS)
            
            fig = go.Figure(data=[
                go.Bar(
                    x=perf_df['Level'],
                    y=perf_df['Count'],
                    marker_color=perf_df['Color'],
                    text=perf_df['Percentage'].apply(lambda x: f'{x}%'),
                    textposition='outside',
                    hovertemplate='<b>%{x}</b><br>Students: %{y}<br>Percentage: %{text}<extra></extra>'
                )
            ])
            
            fig.update_layout(
                showlegend=False,
                height=350,
                margin=dict(l=20, r=20, t=20, b=20),
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                xaxis=dict(showgrid=False, title=None),
                yaxis=dict(showgrid=True, gridcolor='rgba(0,0,0,0.05)', title="Students")
            )
            
            st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### 📚 Grade Breakdown")
        if stats['grade_distribution']:
            grade_df = pd.DataFrame(
                list(stats['grade_distribution'].items()),
                columns=['Grade', 'Count']
            ).sort_values('Count', ascending=False)
            
            colors = ['#3b82f6', '#10b981', '#f59e0b', '#8b5cf6', '#ef4444', 
                     '#06b6d4', '#ec4899', '#84cc16', '#f97316', '#14b8a6']
            
            fig = go.Figure(data=[
                go.Pie(
                    labels=grade_df['Grade'],
                    values=grade_df['Count'],
                    hole=0.5,
                    marker_colors=colors[:len(grade_df)],
                    textinfo='label+percent',
                    textfont_size=12,
                    hovertemplate='<b>Grade %{label}</b><br>%{value} students<br>%{percent}<extra></extra>'
                )
            ])
            
            fig.update_layout(
                showlegend=False,
                height=350,
                margin=dict(l=20, r=20, t=20, b=20),
                paper_bgcolor='rgba(0,0,0,0)'
            )
            
            st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Performance Insights
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🌟 Top Performers")
        top_performers = [s for s in students if s.performance == 'Excellent']
        if top_performers:
            for student in top_performers[:5]:
                st.markdown(f"""
                <div style='background: linear-gradient(135deg, #ecfdf5, #d1fae5); 
                            padding: 1rem 1.25rem; border-radius: 10px; 
                            margin-bottom: 0.75rem; border-left: 3px solid #10b981;'>
                    <div style='font-weight: 700; color: #065f46; font-size: 1rem;'>{student.name}</div>
                    <div style='color: #059669; font-size: 0.875rem; margin-top: 0.25rem;'>
                        Grade {student.grade} • ID: {student.student_id} • Age: {student.age}
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No excellent performers yet")
    
    with col2:
        st.markdown("### ⚠️ Needs Attention")
        need_support = [s for s in students if s.performance in ['Below Average', 'Poor']]
        if need_support:
            for student in need_support[:5]:
                st.markdown(f"""
                <div style='background: linear-gradient(135deg, #fef2f2, #fee2e2); 
                            padding: 1rem 1.25rem; border-radius: 10px; 
                            margin-bottom: 0.75rem; border-left: 3px solid #ef4444;'>
                    <div style='font-weight: 700; color: #991b1b; font-size: 1rem;'>{student.name}</div>
                    <div style='color: #dc2626; font-size: 0.875rem; margin-top: 0.25rem;'>
                        Grade {student.grade} • ID: {student.student_id} • Age: {student.age}
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.success("✅ All students performing well!")
    
    st.markdown("---")
    st.markdown("### 📋 Complete Student Directory")
    render_student_table(students)

    