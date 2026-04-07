import pytest
from utils.validation import normalize_profile_data, validate_profile_data


@pytest.mark.parametrize(
    ("first_name", "last_name", "student_id", "expected"),
    [
        ("Alice", "Smith", "12345678", None),
        (" Alice ", " Smith ", "12345678", None),
        ("", "Smith", "12345678", "All fields are required."),
        ("Alice", "", "12345678", "All fields are required."),
        ("Alice", "Smith", "", "All fields are required."),
        (None, "Smith", "12345678", "All fields are required."),
        ("Alice", None, "12345678", "All fields are required."),
        ("Alice", "Smith", None, "All fields are required."),
        ("   ", "Smith", "12345678", "All fields are required."),
        ("Alice", "   ", "12345678", "All fields are required."),
        ("Alice", "Smith", "   ", "All fields are required."),
        ("", "", "", "All fields are required."),
        ("Alice", "Smith", "1234", "The student ID must be a 8-digit number."),
        ("Alice", "Smith", "12AB5678", "The student ID must be a 8-digit number."),
    ],
)
def test_validate_profile_data(first_name, last_name, student_id, expected):
    assert validate_profile_data(first_name, last_name, student_id) == expected


@pytest.mark.parametrize(
    ("first_name", "last_name", "student_id", "expected"),
    [
        (
            "  Alice  ",
            "  Smith  ",
            " 12345678 ",
            {"first_name": "Alice", "last_name": "Smith", "student_id": "12345678"},
        ),
        (
            None,
            None,
            None,
            {"first_name": "", "last_name": "", "student_id": ""},
        ),
        (
            "Jane",
            "Doe",
            12345678,
            {"first_name": "Jane", "last_name": "Doe", "student_id": "12345678"},
        ),
        (
            "  ",
            "Brown",
            " 00001234 ",
            {"first_name": "", "last_name": "Brown", "student_id": "00001234"},
        ),
        (
            "Chris",
            "  ",
            "  87654321",
            {"first_name": "Chris", "last_name": "", "student_id": "87654321"},
        ),
    ],
)
def test_normalize_profile_data(first_name, last_name, student_id, expected):
    assert normalize_profile_data(first_name, last_name, student_id) == expected