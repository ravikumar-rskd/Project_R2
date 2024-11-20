from typing import List, Optional
from pydantic import BaseModel
# from motor.motor_asyncio import AsyncIOMotorDatabase


class Lesson(BaseModel):
    id: str
    title: str
    videoUrl: str
    duration: str
    isFree: bool
    resources: dict
    problemIds: List[str] = []


class Module(BaseModel):
    id: str
    title: str
    isFree: bool
    order: int
    description: str
    lessons: List[Lesson]


class Course(BaseModel):
    dsa: Optional[dict] = None
    python: Optional[dict] = None

    class Config:
        orm_mode = True


# async def get_course_by_id(db: AsyncIOMotorDatabase, course_id: str) -> Course:
#     course = await db.courses.find_one({"_id": course_id})
#     return Course(**course) if course else None
