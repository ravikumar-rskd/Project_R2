from typing import List, Dict
from pydantic import BaseModel


class ProblemSchema(BaseModel):
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
