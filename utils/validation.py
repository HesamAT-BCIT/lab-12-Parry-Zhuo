from __future__ import annotations

from flask import jsonify, request


def validate_profile_data(first_name: str, last_name: str, student_id: str):
    """Validate that required profile fields are present and well-formed."""
    normalized_first_name = first_name.strip() if isinstance(first_name, str) else ""
    normalized_last_name = last_name.strip() if isinstance(last_name, str) else ""
    normalized_student_id = str(student_id).strip() if student_id is not None else ""

    if not normalized_first_name or not normalized_last_name or not normalized_student_id:
        return "All fields are required."
    if not normalized_student_id.isdigit() or len(normalized_student_id) != 8:
        return "The student ID must be a 8-digit number."
    return None


def normalize_profile_data(first_name: str, last_name: str, student_id: str):
    """Normalize profile field values (strip whitespace, stringify student_id)."""
    return {
        "first_name": first_name.strip() if first_name else "",
        "last_name": last_name.strip() if last_name else "",
        "student_id": str(student_id).strip() if student_id else "",
    }


def require_json_content_type():
    """Ensure the request is JSON; returns an error response tuple if not."""
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 415
    return None
