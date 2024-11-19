from fastapi import APIRouter, HTTPException, status
from app.schemas.lesson_schema import LessonCreate, LessonResponse
from app.services import lesson_service

router = APIRouter()

# Get all lessons
@router.get("/", response_model=list[LessonResponse]) #use "ip_address/lessons/" as base api endpoint for all http methods
async def read_lessons():
    return await lesson_service.get_all_lessons()

# Get a lesson by title (modified to use title instead of ID)
@router.get("/{lesson_title}", response_model=LessonResponse)
async def read_lesson(lesson_title: str):
    lesson = await lesson_service.get_lesson(lesson_title)
    if lesson is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lesson not found")
    return lesson

# Create a lesson
@router.post("/", response_model=LessonResponse, status_code=status.HTTP_201_CREATED)
async def create_lesson(lesson: LessonCreate):
    return await lesson_service.create_lesson(lesson)

    # Create multiple lessons
@router.post("/bulk", response_model=list[LessonResponse], status_code=status.HTTP_201_CREATED)
async def create_lessons_bulk(lessons: list[LessonCreate]):
    return await lesson_service.create_lessons_bulk(lessons)

# Update a lesson by title (modified to use title instead of ID)
@router.put("/{lesson_title}", response_model=LessonResponse)
async def update_lesson(lesson_title: str, lesson: LessonCreate):
    updated_lesson = await lesson_service.update_lesson(lesson_title, lesson)
    if updated_lesson is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lesson not found")
    return updated_lesson

# Delete a lesson by title (modified to use title instead of ID)
@router.delete("/{lesson_title}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_lesson(lesson_title: str):
    success = await lesson_service.delete_lesson(lesson_title)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lesson not found")
