from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from grade_schema import GradeCreateSchema
from grade_service import create_grade_by_course_id, get_grades_by_student, get_grades_by_course, calculate_gpa, update_grade, delete_grade
from db import get_db
from jwt import get_current_user

grade_router = APIRouter(tags=["grade"], prefix="/grades")

# Qiymət əlavə etmək
@grade_router.post("/{course_id}")
def add_mark_for_student(
    item: GradeCreateSchema,
    student_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    msg = create_grade_by_course_id(student_id=student_id, data=item, db=db, current_user=current_user)
    return msg

# Tələbənin qiymətlərini əldə etmək
@grade_router.get("/{student_id}")
def get_student_grades(student_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    grades = get_grades_by_student(student_id=student_id, db=db, current_user=current_user)
    return grades

# Kurs üzrə qiymətləri əldə etmək
@grade_router.get("/course/{course_id}")
def get_course_grades(course_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    grades = get_grades_by_course(course_id=course_id, db=db, current_user=current_user)
    return grades

# GPA hesablamaq
@grade_router.get("/gpa/{student_id}")
def get_student_gpa(student_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    gpa = calculate_gpa(student_id=student_id, db=db, current_user=current_user)
    return gpa

# Qiyməti yeniləmək
@grade_router.put("/{course_id}")
def update_mark_for_student(
    course_id: int,
    student_id: int,
    grade: str,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    msg = update_grade(course_id=course_id, student_id=student_id, grade=grade, db=db, current_user=current_user)
    return msg

# Qiyməti silmək
@grade_router.delete("/{course_id}")
def delete_mark_for_student(
    course_id: int,
    student_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    msg = delete_grade(course_id=course_id, student_id=student_id, db=db, current_user=current_user)
    return msg
