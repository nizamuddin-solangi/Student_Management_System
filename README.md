# 🎓 Student Management System

A complete Student Management System built with Python OOP principles and Streamlit for the user interface.

## 📋 Features

- **Complete CRUD Operations**: Add, Update, Delete, and View students
- **Advanced Search & Filtering**: Search by name/ID/email, filter by grade, age range, and performance
- **Data Persistence**: JSON-based storage for reliability
- **Input Validation**: Comprehensive validation for all fields
- **Clean OOP Architecture**: Well-structured, modular codebase
- **Modern UI**: Intuitive Streamlit interface with forms, tables, and alerts
- **Statistics Dashboard**: View system statistics and distributions

## 🏗️ Project Structure

```
student-management-system/
│
├── main.py                     # Main Streamlit application
│
├── models/
│   └── student.py              # Student class definition
│
├── services/
│   ├── student_manager.py      # CRUD operations and business logic
│   └── validation.py           # Input validation utilities
│
├── ui/
│   └── components.py           # Streamlit UI components
│
├── data/
│   └── students.json           # JSON data storage
│
└── README.md                   # Documentation
```

## 🚀 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Step 1: Install Dependencies

```bash
pip install streamlit pandas
```

### Step 2: Create Project Structure

Create the following directory structure:

```
student-management-system/
├── main.py
├── models/
│   └── student.py
├── services/
│   ├── student_manager.py
│   └── validation.py
├── ui/
│   └── components.py
└── data/
    └── students.json
```

### Step 3: Add Files

Copy all the provided code files into their respective locations as shown in the project structure above.

### Step 4: Run the Application

```bash
streamlit run main.py
```

The application will open in your default web browser at `http://localhost:8501`

## 📖 Usage Guide

### View All Students

- Navigate to "View All Students" from the sidebar
- See all students in a clean table format
- View total student count

### Add New Student

1. Navigate to "Add Student"
2. Fill in all required fields:
   - **Student ID**: Unique identifier (e.g., STU001)
   - **Name**: Full name of the student
   - **Age**: Student's age (5-100)
   - **Grade**: Select from dropdown
   - **Email**: Valid email address
   - **Phone**: Contact number
   - **Performance**: Academic performance level
3. Click "Add Student" button
4. Success message with confetti animation on successful addition

### Update Student

1. Navigate to "Update Student"
2. Select student from dropdown
3. Modify any fields you want to update
4. Click "Update Student" button
5. Changes are saved immediately

### Delete Student

1. Navigate to "Delete Student"
2. Select student from dropdown
3. Review student details
4. Click "Confirm Delete" button
5. Student is permanently removed

### Search & Filter

1. Navigate to "Search & Filter"
2. Use text search for name, ID, or email
3. Apply filters:
   - Filter by Grade
   - Filter by Performance Level
   - Filter by Age Range
4. View filtered results with statistics

## 🔍 Features in Detail

### Input Validation

All fields are validated with comprehensive checks:

- **Name**: 2-100 characters, letters, spaces, hyphens, and apostrophes only
- **Age**: Between 5 and 100 years
- **Grade**: Must be valid grade level
- **Email**: Valid email format (example@domain.com)
- **Phone**: 10-15 digits with optional formatting
- **Performance**: Must be one of: Excellent, Good, Average, Below Average, Poor
- **Student ID**: 3-20 characters, alphanumeric with hyphens/underscores

### Data Persistence

- Data is stored in `data/students.json`
- Automatic backup on each operation
- Rollback on save failures
- Creates data directory automatically if missing

### OOP Architecture

**Student Class** (`models/student.py`)
- Encapsulates student data
- Methods for dictionary conversion
- Update functionality

**StudentManager Class** (`services/student_manager.py`)
- Manages all CRUD operations
- Handles data persistence
- Provides search and filter methods
- Calculates statistics

**Validator Class** (`services/validation.py`)
- Validates all input fields
- Returns detailed error messages
- Ensures data integrity

## 🎨 UI Components

- **Forms**: Clean input forms with validation feedback
- **Tables**: Responsive data tables with all student information
- **Alerts**: Success, error, warning, and info messages
- **Metrics**: Statistics cards showing key numbers
- **Charts**: Visual representation of distributions

## 📊 Sample Data

The system comes with 10 sample students covering various grades and performance levels. You can:
- View the sample data
- Modify it
- Delete it
- Add your own students

## 🛠️ Customization

### Adding New Grades

Edit the `GRADES` list in `ui/components.py`:

```python
GRADES = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
          'KG', 'Nursery', 'Pre-K', 'Freshman', 'Sophomore', 'Junior', 'Senior']
```

### Adding New Performance Levels

Edit the `PERFORMANCE_LEVELS` list in `ui/components.py`:

```python
PERFORMANCE_LEVELS = ['Excellent', 'Good', 'Average', 'Below Average', 'Poor']
```

### Changing Data Storage Location

Modify the `data_file` parameter in `main.py`:

```python
st.session_state.manager = StudentManager(data_file='custom/path/students.json')
```

## 🔧 Troubleshooting

### Application Won't Start

- Ensure all dependencies are installed: `pip install streamlit pandas`
- Check Python version: `python --version` (should be 3.8+)
- Verify all files are in correct directories

### Data Not Saving

- Check write permissions in the `data/` directory
- Ensure `data/` directory exists
- Check console for error messages

### Validation Errors

- Review validation rules in `services/validation.py`
- Ensure input matches expected format
- Check error messages for specific issues

## 📝 Technical Details

### Dependencies

- **Streamlit**: Web interface framework
- **Pandas**: Data manipulation and display
- **JSON**: Built-in Python module for data storage
- **re**: Built-in Python module for validation

### Python Version

- Requires Python 3.8 or higher
- Tested on Python 3.8, 3.9, 3.10, 3.11

### Data Format

Students are stored in JSON format:

```json
{
  "student_id": "STU001",
  "name": "John Doe",
  "age": 16,
  "grade": "10",
  "email": "john@example.com",
  "phone": "+1234567890",
  "performance": "Excellent"
}
```

## 🤝 Contributing

To extend the system:

1. Add new methods to `StudentManager` class for business logic
2. Add new UI components in `ui/components.py`
3. Update validation rules in `services/validation.py`
4. Maintain the existing OOP structure

## 📄 License

This project is provided as-is for educational purposes.

## 👨‍💻 Support

For issues or questions:
- Check the troubleshooting section
- Review the code comments
- Verify all files are correctly placed

## 🎯 Future Enhancements

Potential features to add:
- Export to CSV/Excel
- Import from CSV/Excel
- Student photos
- Attendance tracking
- Grade history
- Parent contact information
- Email notifications
- Advanced reporting
- Database integration (SQLite, PostgreSQL)
- User authentication
- Multi-language support

---

**Built with ❤️ using Python OOP and Streamlit**