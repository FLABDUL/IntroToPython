from typing import List, Dict, Optional, Union, Tuple

class Student:
    def __init__(self, name: str, age: int, grades: Optional[List[float]] = None):
        # Type hinting for name and age as string and integer
        # grades is an optional list of float values
        self.name: str = name
        self.age: int = age
        self.grades: List[float] = grades if grades is not None else []

    def add_grade(self, grade: float) -> None:
        # grade must be a float, return nothing
        self.grades.append(grade)

    def average_grade(self) -> Optional[float]:
        # Returns average as float or None if no grades
        if not self.grades:
            return None
        return sum(self.grades) / len(self.grades)

    def get_profile(self) -> Dict[str, Union[str, int, float, None]]:
        # Return a dictionary with student's profile data
        return {
            "name": self.name,
            "age": self.age,
            "average_grade": self.average_grade()
        }

class School:
    def __init__(self):
        self.students: Dict[str, Student] = {}

    def add_student(self, student: Student) -> None:
        # Add student by name as key
        self.students[student.name] = student

    def get_student(self, name: str) -> Optional[Student]:
        # Return student object if found, otherwise None
        return self.students.get(name)

    def get_all_profiles(self) -> List[Dict[str, Union[str, int, float, None]]]:
        # Return a list of student profile dictionaries
        return [student.get_profile() for student in self.students.values()]
