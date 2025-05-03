import pytest

from src.demo.AdvancedTypingDemo import SCHOOL_NAME, Student, StudentProfile


def test_school_name_constant():
    assert SCHOOL_NAME == "Python High"

def test_typed_dict_profile():
    s = Student("Alice", 20, [95.0])
    profile: StudentProfile = s.get_profile()
    assert isinstance(profile, dict)
    assert profile["name"] == "Alice"
    assert profile["average_grade"] == 95.0

def test_letter_grades():
    s = Student("Bob", 22, [85.0])
    assert s.get_letter_grade() == "B"

    s2 = Student("Charlie", 22, [50.0])
    assert s2.get_letter_grade() == "F"

    s3 = Student("Dana", 22, [])
    assert s3.get_letter_grade() is None
