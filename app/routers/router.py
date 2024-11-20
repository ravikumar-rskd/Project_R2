from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.schemas.course_schema import CourseSchema, ModuleSchema
from app.schemas.problem_schema import ProblemSchema
# from app.services.course_service import get_course_by_id, get_module_by_id
from app.services.problem_service import get_problems_by_lesson_id
from db.mongodb import courses_collection, problems_collection  # Import the collections
from app.services.course_service import get_all_courses, get_course_by_id

router = APIRouter()

# Fetch all courses
@router.get("/courses", response_model=List[CourseSchema])
async def fetch_all_courses():
    courses = await get_all_courses()
    if not courses:
        raise HTTPException(status_code=404, detail="No courses found")
    return courses

# Fetch a course by its ID
@router.get("/courses/{course_id}", response_model=CourseSchema)
async def fetch_course(course_id: str):
    course = await get_course_by_id(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course
# Fetch problems by lessonId
@router.get("/problems/lesson/{lesson_id}", response_model=List[ProblemSchema])
async def fetch_problems_by_lesson(lesson_id: str):
    problems = await get_problems_by_lesson_id(problems_collection, lesson_id)
    if not problems:
        raise HTTPException(status_code=404, detail="Problems not found")
    return problems
