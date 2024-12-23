from fastapi import Depends
from models import *
from jwt import get_current_user
from sqlalchemy.orm import Session
from exceptions import *
from grade_schema import *
from datetime import date

def get_grade_by_student_id():
    pass

def get_grades_by_course_id():
    pass

def calculate_gpa_by_student_id():
    pass

def create_grade_by_course_id(db:Session , data:GradeCreateSchema , current_user = Depends(get_current_user)):
    this_user = db.query(User).filter_by(username = current_user['username']).first()

    if this_user.role != "admin":
        raise Unauthorized
    
    course_check = db.query(Course).filter_by(id = data.course_id).first()

    course_check_in_registration = db.qu






def update_grade_by_course_id():
    pass

def delete_grade_by_course_id():
    pass