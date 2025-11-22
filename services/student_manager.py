"""
Student Manager Service
Handles all CRUD operations and data persistence
"""

import json
import os
from models.student import Student
from services.validation import Validator

class StudentManager:
    """
    Manages student data and operations
    """
    
    def __init__(self, data_file='data/students.json'):
        """
        Initialize the student manager
        
        Args:
            data_file (str): Path to the JSON data file
        """
        self.data_file = data_file
        self.students = []
        self._ensure_data_directory()
        self.load_data()
    
    def _ensure_data_directory(self):
        """Create data directory if it doesn't exist"""
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
    
    def load_data(self):
        """Load student data from JSON file"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.students = [Student.from_dict(item) for item in data]
            else:
                self.students = []
                self.save_data()  # Create empty file
        except Exception as e:
            print(f"Error loading data: {e}")
            self.students = []
    
    def save_data(self):
        """Save student data to JSON file"""
        try:
            with open(self.data_file, 'w') as f:
                data = [student.to_dict() for student in self.students]
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
    
    def add_student(self, student_id, name, age, grade, email, phone, performance):
        """
        Add a new student
        
        Args:
            student_id (str): Unique student ID
            name (str): Student name
            age (int): Student age
            grade (str): Student grade
            email (str): Student email
            phone (str): Student phone
            performance (str): Student performance level
            
        Returns:
            tuple: (success, message)
        """
        # Validate all fields
        is_valid, errors = Validator.validate_all(
            student_id, name, age, grade, email, phone, performance
        )
        
        if not is_valid:
            return False, errors
        
        # Check for duplicate ID
        if self.get_student_by_id(student_id):
            return False, ["Student ID already exists"]
        
        # Create and add student
        student = Student(student_id, name, int(age), grade, email, phone, performance)
        self.students.append(student)
        
        if self.save_data():
            return True, "Student added successfully"
        else:
            self.students.pop()  # Rollback
            return False, ["Failed to save data"]
    
    def update_student(self, student_id, name=None, age=None, grade=None, 
                      email=None, phone=None, performance=None):
        """
        Update an existing student
        
        Args:
            student_id (str): Student ID to update
            name (str, optional): New name
            age (int, optional): New age
            grade (str, optional): New grade
            email (str, optional): New email
            phone (str, optional): New phone
            performance (str, optional): New performance
            
        Returns:
            tuple: (success, message)
        """
        student = self.get_student_by_id(student_id)
        
        if not student:
            return False, ["Student not found"]
        
        # Prepare validation data (use existing values if not provided)
        val_name = name if name is not None else student.name
        val_age = age if age is not None else student.age
        val_grade = grade if grade is not None else student.grade
        val_email = email if email is not None else student.email
        val_phone = phone if phone is not None else student.phone
        val_performance = performance if performance is not None else student.performance
        
        # Validate
        is_valid, errors = Validator.validate_all(
            student_id, val_name, val_age, val_grade, val_email, val_phone, val_performance
        )
        
        if not is_valid:
            return False, errors
        
        # Store old values for rollback
        old_data = student.to_dict()
        
        # Update student
        student.update(
            name=name,
            age=int(age) if age is not None else None,
            grade=grade,
            email=email,
            phone=phone,
            performance=performance
        )
        
        if self.save_data():
            return True, "Student updated successfully"
        else:
            # Rollback
            student.update(**old_data)
            return False, ["Failed to save data"]
    
    def delete_student(self, student_id):
        """
        Delete a student
        
        Args:
            student_id (str): Student ID to delete
            
        Returns:
            bool: Success status
        """
        student = self.get_student_by_id(student_id)
        
        if not student:
            return False
        
        self.students.remove(student)
        
        if self.save_data():
            return True
        else:
            self.students.append(student)  # Rollback
            return False
    
    def get_student_by_id(self, student_id):
        """
        Get a student by ID
        
        Args:
            student_id (str): Student ID
            
        Returns:
            Student or None: Student object if found
        """
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
    
    def get_all_students(self):
        """
        Get all students
        
        Returns:
            list: List of all Student objects
        """
        return self.students
    
    def search_students(self, query):
        """
        Search students by name or ID
        
        Args:
            query (str): Search query
            
        Returns:
            list: List of matching Student objects
        """
        query = query.lower()
        results = []
        
        for student in self.students:
            if (query in student.name.lower() or 
                query in student.student_id.lower() or
                query in student.email.lower()):
                results.append(student)
        
        return results
    
    def filter_by_grade(self, grade):
        """
        Filter students by grade
        
        Args:
            grade (str): Grade to filter by
            
        Returns:
            list: List of Student objects in the grade
        """
        return [s for s in self.students if s.grade == grade]
    
    def filter_by_age_range(self, min_age, max_age):
        """
        Filter students by age range
        
        Args:
            min_age (int): Minimum age
            max_age (int): Maximum age
            
        Returns:
            list: List of Student objects in age range
        """
        return [s for s in self.students 
                if min_age <= s.age <= max_age]
    
    def filter_by_performance(self, performance):
        """
        Filter students by performance level
        
        Args:
            performance (str): Performance level
            
        Returns:
            list: List of Student objects with performance level
        """
        return [s for s in self.students if s.performance == performance]
    
    def get_statistics(self):
        """
        Get system statistics
        
        Returns:
            dict: Statistics about students
        """
        if not self.students:
            return {
                'total': 0,
                'avg_age': 0,
                'performance_distribution': {},
                'grade_distribution': {}
            }
        
        total = len(self.students)
        avg_age = sum(s.age for s in self.students) / total
        
        # Performance distribution
        performance_dist = {}
        for student in self.students:
            perf = student.performance
            performance_dist[perf] = performance_dist.get(perf, 0) + 1
        
        # Grade distribution
        grade_dist = {}
        for student in self.students:
            grade = student.grade
            grade_dist[grade] = grade_dist.get(grade, 0) + 1
        
        return {
            'total': total,
            'avg_age': round(avg_age, 1),
            'performance_distribution': performance_dist,
            'grade_distribution': grade_dist
        }