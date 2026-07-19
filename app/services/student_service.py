"""
router layer = resp for handling HTTP - GET, POST, HTTPException, Response
Service layer = Business Logic = Can this student be deleted or
send email after creation
Repository later = data access responsibility = Find, create, Update, Delete from DB
"""

from app.repositories import student_repositories
from app.schemas.student import Student


def get_all_students(db):
    return student_repositories.get_all_students(db)


def get_student_by_id(db,student_id: int):
    return student_repositories.get_student_by_id(db,student_id)


def create_student(db,student_data:dict):
    return student_repositories.create_student(db,student_data)


def update_student(db,student_id: int, updated_data: dict):
    return student_repositories.update_student(db,student_id, updated_data)


def delete_student(db,student_id: int):
    return student_repositories.delete_student(db,student_id)
