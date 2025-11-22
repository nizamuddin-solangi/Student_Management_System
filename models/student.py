"""
Student Model
Defines the Student class with validation
"""

class Student:
    """
    Represents a student with personal and academic information
    """
    
    def __init__(self, student_id, name, age, grade, email, phone, performance):
        """
        Initialize a Student object
        
        Args:
            student_id (str): Unique identifier for the student
            name (str): Full name of the student
            age (int): Age of the student
            grade (str): Academic grade/class
            email (str): Email address
            phone (str): Phone number
            performance (str): Academic performance level
        """
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
        self.email = email
        self.phone = phone
        self.performance = performance
    
    def to_dict(self):
        """
        Convert student object to dictionary
        
        Returns:
            dict: Student data as dictionary
        """
        return {
            'student_id': self.student_id,
            'name': self.name,
            'age': self.age,
            'grade': self.grade,
            'email': self.email,
            'phone': self.phone,
            'performance': self.performance
        }
    
    @staticmethod
    def from_dict(data):
        """
        Create a Student object from dictionary
        
        Args:
            data (dict): Dictionary containing student data
            
        Returns:
            Student: Student object
        """
        return Student(
            student_id=data['student_id'],
            name=data['name'],
            age=data['age'],
            grade=data['grade'],
            email=data['email'],
            phone=data['phone'],
            performance=data['performance']
        )
    
    def update(self, name=None, age=None, grade=None, email=None, phone=None, performance=None):
        """
        Update student attributes
        
        Args:
            name (str, optional): New name
            age (int, optional): New age
            grade (str, optional): New grade
            email (str, optional): New email
            phone (str, optional): New phone
            performance (str, optional): New performance level
        """
        if name is not None:
            self.name = name
        if age is not None:
            self.age = age
        if grade is not None:
            self.grade = grade
        if email is not None:
            self.email = email
        if phone is not None:
            self.phone = phone
        if performance is not None:
            self.performance = performance
    
    def __str__(self):
        """
        String representation of student
        
        Returns:
            str: Formatted student information
        """
        return f"Student(ID: {self.student_id}, Name: {self.name}, Grade: {self.grade}, Performance: {self.performance})"
    
    def __repr__(self):
        """
        Official string representation
        
        Returns:
            str: Representation string
        """
        return self.__str__()