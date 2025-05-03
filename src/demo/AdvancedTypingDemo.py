from typing import List, Dict, Optional, Union, Tuple, Literal, TypedDict, Protocol, runtime_checkable, Final

# -- Final -- #
SCHOOL_NAME: Final[str] = "Python High"

# -- TypedDict for student profile -- #
class StudentProfile(TypedDict):
    name: str
    age: int
    average_grade: Optional[float]

# -- Protocol: defines interface for any object that acts like a Student -- #
@runtime_checkable
class StudentLike(Protocol):
    name: str
    age: int
    grades: List[float]

    def add_grade(self, grade: float) -> None:
        ...
    def average_grade(self) -> Optional[float]:
        ...
    def get_profile(self) -> StudentProfile:
        ...

# -- Literal: used to constrain accepted values -- #
GradeType = Literal["A", "B", "C", "D", "F"]

class Student:
    def __init__(self, name: str, age: int, grades: Optional[List[float]] = None):
        self.name: str = name
        self.age: int = age
        self.grades: List[float] = grades if grades is not None else []

    def add_grade(self, grade: float) -> None:
        self.grades.append(grade)

    def average_grade(self) -> Optional[float]:
        if not self.grades:
            return None
        return sum(self.grades) / len(self.grades)

    def get_profile(self) -> StudentProfile:
        return {
            "name": self.name,
            "age": self.age,
            "average_grade": self.average_grade()
        }

    def get_letter_grade(self) -> Optional[GradeType]:
        avg = self.average_grade()
        if avg is None:
            return None
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

class School:
    def __init__(self):
        self.students: Dict[str, StudentLike] = {}

    def add_student(self, student: StudentLike) -> None:
        self.students[student.name] = student

    def get_all_profiles(self) -> List[StudentProfile]:
        return [student.get_profile() for student in self.students.values()]
