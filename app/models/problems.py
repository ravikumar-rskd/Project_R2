from typing import List, Dict
from pydantic import BaseModel
# from motor.motor_asyncio import AsyncIOMotorDatabase


class Problem(BaseModel):
    id: str
    title: str
    description: str
    difficulty: str
    hints: List[str]
    solution: str
    testCases: List[Dict[str, str]]
    moduleId: str

    class Config:
        orm_mode = True


# async def get_problem_by_id(db: AsyncIOMotorDatabase, problem_id: str) -> Problem:
#     problem = await db.problems.find_one({"_id": problem_id})
#     return Problem(**problem) if problem else None
