from motor.motor_asyncio import AsyncIOMotorDatabase
from app.schemas.course_schema import CourseSchema
from bson import ObjectId
from typing import List
from app.db.mongodb import courses_collection

# Fetch all courses
async def get_all_courses() -> List[CourseSchema]:
    # Assuming that each course has a key like "dsa" or "python" in the document
    courses = await courses_collection.find().to_list(length=100)
    return [CourseSchema(**course) for course in courses] if courses else []

# Fetch a course by its ID (either "dsa-course" or "python-course")
async def get_course_by_id(course_id: str) -> CourseSchema:
    course = await courses_collection.find_one({"dsa.id": course_id})
    if course:
        return CourseSchema(**course["dsa"])  # Return the `dsa` or `python` field from the document
    course = await courses_collection.find_one({"python.id": course_id})
    if course:
        return CourseSchema(**course["python"])  # Return the `python` field from the document
    return None

# # Fetch module by moduleId inside a specific course
# async def get_module_by_id(courses_collection, course_id: str, module_id: str) -> ModuleSchema:
#     course = await courses_collection.find_one({"_id": ObjectId(course_id)})
#     if not course:
#         return None

#     # Check if the module_id exists inside the course
#     module = None
#     for mod in course.get('modules', []):
#         if str(mod['moduleId']) == module_id:
#             module = mod
#             break

#     if module:
#         return ModuleSchema(**module)
#     return None

