from motor.motor_asyncio import AsyncIOMotorDatabase
from app.schemas import ProblemSchema
from bson import ObjectId
from typing import List

# Fetch problems by lessonId
async def get_problems_by_lesson_id(problems_collection, lesson_id: str) -> List[ProblemSchema]:
    problems = await problems_collection.find({"lessonId": lesson_id}).to_list(length=100)
    if problems:
        return [ProblemSchema(**problem) for problem in problems]  # Return a list of problems as Pydantic schemas
    return []
