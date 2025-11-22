"""
Validation Utilities
Provides input validation functions for student data
"""

import re

class ValidationError(Exception):
    """Custom exception for validation errors"""
    pass

class Validator:
    """Handles all validation logic for student data"""
    
    @staticmethod
    def validate_name(name):
        """
        Validate student name
        
        Args:
            name (str): Name to validate
            
        Returns:
            tuple: (is_valid, error_message)
        """
        if not name or not name.strip():
            return False, "Name cannot be empty"
        
        if len(name.strip()) < 2:
            return False, "Name must be at least 2 characters long"
        
        if len(name.strip()) > 100:
            return False, "Name must be less than 100 characters"
        
        if not re.match(r'^[a-zA-Z\s\'-]+$', name):
            return False, "Name can only contain letters, spaces, hyphens, and apostrophes"
        
        return True, ""
    
    @staticmethod
    def validate_age(age):
        """
        Validate student age
        
        Args:
            age (int): Age to validate
            
        Returns:
            tuple: (is_valid, error_message)
        """
        try:
            age = int(age)
        except (ValueError, TypeError):
            return False, "Age must be a valid number"
        
        if age < 5:
            return False, "Age must be at least 5 years"
        
        if age > 100:
            return False, "Age must be less than 100 years"
        
        return True, ""
    
    @staticmethod
    def validate_grade(grade):
        """
        Validate student grade
        
        Args:
            grade (str): Grade to validate
            
        Returns:
            tuple: (is_valid, error_message)
        """
        if not grade or not grade.strip():
            return False, "Grade cannot be empty"
        
        valid_grades = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
                       'KG', 'Nursery', 'Pre-K', 'Freshman', 'Sophomore', 'Junior', 'Senior']
        
        if grade not in valid_grades:
            return False, f"Grade must be one of: {', '.join(valid_grades)}"
        
        return True, ""
    
    @staticmethod
    def validate_email(email):
        """
        Validate email address
        
        Args:
            email (str): Email to validate
            
        Returns:
            tuple: (is_valid, error_message)
        """
        if not email or not email.strip():
            return False, "Email cannot be empty"
        
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if not re.match(email_pattern, email):
            return False, "Invalid email format (example: user@example.com)"
        
        if len(email) > 254:
            return False, "Email is too long"
        
        return True, ""
    
    @staticmethod
    def validate_phone(phone):
        """
        Validate phone number
        
        Args:
            phone (str): Phone number to validate
            
        Returns:
            tuple: (is_valid, error_message)
        """
        if not phone or not phone.strip():
            return False, "Phone number cannot be empty"
        
        # Remove common separators
        cleaned_phone = re.sub(r'[\s\-\(\)\+]', '', phone)
        
        if not cleaned_phone.isdigit():
            return False, "Phone number can only contain digits, spaces, hyphens, and parentheses"
        
        if len(cleaned_phone) < 10 or len(cleaned_phone) > 15:
            return False, "Phone number must be between 10 and 15 digits"
        
        return True, ""
    
    @staticmethod
    def validate_performance(performance):
        """
        Validate performance level
        
        Args:
            performance (str): Performance level to validate
            
        Returns:
            tuple: (is_valid, error_message)
        """
        valid_levels = ['Excellent', 'Good', 'Average', 'Below Average', 'Poor']
        
        if performance not in valid_levels:
            return False, f"Performance must be one of: {', '.join(valid_levels)}"
        
        return True, ""
    
    @staticmethod
    def validate_student_id(student_id):
        """
        Validate student ID
        
        Args:
            student_id (str): Student ID to validate
            
        Returns:
            tuple: (is_valid, error_message)
        """
        if not student_id or not student_id.strip():
            return False, "Student ID cannot be empty"
        
        if len(student_id) < 3:
            return False, "Student ID must be at least 3 characters long"
        
        if len(student_id) > 20:
            return False, "Student ID must be less than 20 characters"
        
        if not re.match(r'^[a-zA-Z0-9_-]+$', student_id):
            return False, "Student ID can only contain letters, numbers, hyphens, and underscores"
        
        return True, ""
    
    @classmethod
    def validate_all(cls, student_id, name, age, grade, email, phone, performance):
        """
        Validate all student fields
        
        Args:
            student_id (str): Student ID
            name (str): Name
            age (int): Age
            grade (str): Grade
            email (str): Email
            phone (str): Phone
            performance (str): Performance level
            
        Returns:
            tuple: (is_valid, list_of_errors)
        """
        errors = []
        
        # Validate each field
        checks = [
            cls.validate_student_id(student_id),
            cls.validate_name(name),
            cls.validate_age(age),
            cls.validate_grade(grade),
            cls.validate_email(email),
            cls.validate_phone(phone),
            cls.validate_performance(performance)
        ]
        
        for is_valid, error_msg in checks:
            if not is_valid:
                errors.append(error_msg)
        
        return len(errors) == 0, errors