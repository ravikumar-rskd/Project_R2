from pydantic import BaseModel
from typing import List, Optional, Dict

class Resources(BaseModel):
    notes: str
    practice: str

class Lesson(BaseModel):
    id: str
    title: str
    videoUrl: str
    duration: str
    isFree: bool
    resources: Resources

class Module(BaseModel):
    id: str
    title: str
    description: str
    isFree: bool
    order: Optional[int]
    lessons: List[Lesson]

class Course(BaseModel):
    id: str
    title: str
    description: str
    modules: List[Module]

# To represent a course creation request
class CourseCreate(BaseModel):
    title: str
    description: str
    modules: List[Module]

# To represent a course response with an ID
class CourseResponse(BaseModel):
    id: str
    title: str
    description: str
    modules: List[Module]

    class Config:
        orm_mode = True
