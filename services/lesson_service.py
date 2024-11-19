from app.schemas.lesson_schema import LessonCreate, LessonResponse
from app.db.mongodb import database
from bson import ObjectId

# Get all lessons
async def get_all_lessons():
    lessons = await database["lessons"].find().to_list(100)
    return [LessonResponse(id=str(lesson["_id"]), **lesson) for lesson in lessons]

# Get a lesson by title (instead of ID)
async def get_lesson(lesson_title: str):
    lesson = await database["lessons"].find_one({"lessonTitle": lesson_title})
    print(lesson)
    if lesson:
        return LessonResponse(id=str(lesson["_id"]), **lesson)
    return None

# Create a lesson
async def create_lesson(lesson: LessonCreate):
    lesson_data = lesson.dict()
    result = await database["lessons"].insert_one(lesson_data)
    return LessonResponse(id=str(result.inserted_id), **lesson_data)

# Create multiple lessons
async def create_lessons_bulk(lessons: list[LessonCreate]):
    lessons_data = [lesson.dict() for lesson in lessons]
    result = await database["lessons"].insert_many(lessons_data)
    return [
        LessonResponse(id=str(inserted_id), **lesson)
        for inserted_id, lesson in zip(result.inserted_ids, lessons_data)
    ]

# Update a lesson by title (instead of ID)
async def update_lesson(lesson_title: str, lesson: LessonCreate):
    # Find the lesson by title and update it
    result = await database["lessons"].update_one(
        {"title": lesson_title}, {"$set": lesson.dict()}
    )
    if result.matched_count == 0:
        return None  # No lesson found with the given title
    updated_lesson = await database["lessons"].find_one({"title": lesson_title})
    return LessonResponse(id=str(updated_lesson["_id"]), **updated_lesson)

# Delete a lesson by title (instead of ID)
async def delete_lesson(lesson_title: str):
    result = await database["lessons"].delete_one({"title": lesson_title})
    return result.deleted_count > 0
