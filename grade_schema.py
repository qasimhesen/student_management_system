from pydantic import BaseModel

# Qiymət əlavə etmək üçün schema
class GradeCreateSchema(BaseModel):
    course_id: int
    grade: str

    class Config:
        orm_mode = True
