import pytest

from src.demo.TypingDemo import Student, School


def test_student_creation():
    s = Student("Alice", 20)
    assert s.name == "Alice"
    assert s.age == 20
    assert s.grades == []

def test_add_grade_and_average():
    s = Student("Bob", 22)
    s.add_grade(90.0)
    s.add_grade(80.0)
    assert s.grades == [90.0, 80.0]
    assert s.average_grade() == 85.0

def test_average_grade_none():
    s = Student("Charlie", 23)
    assert s.average_grade() is None

def test_get_profile():
    s = Student("Dana", 21, [100.0, 90.0])
    profile = s.get_profile()
    assert profile["name"] == "Dana"
    assert profile["age"] == 21
    assert profile["average_grade"] == 95.0

def test_school_add_get_student():
    school = School()
    student = Student("Eve", 19)
    school.add_student(student)
    assert school.get_student("Eve") == student
    assert school.get_student("Unknown") is None

def test_get_all_profiles():
    school = School()
    s1 = Student("Frank", 20, [70.0, 80.0])
    s2 = Student("Grace", 21, [90.0])
    school.add_student(s1)
    school.add_student(s2)
    profiles = school.get_all_profiles()
    assert len(profiles) == 2
    names = [profile["name"] for profile in profiles]
    assert "Frank" in names
    assert "Grace" in names
