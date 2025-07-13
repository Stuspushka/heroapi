from pydantic import BaseModel

class HeroBase(BaseModel):
    name: str

class HeroCreate(HeroBase):
    pass

class Hero(HeroBase):
    id: int
    intelligence: int
    strength: int
    speed: int
    power: int

    class Config:
        from_attributes = True
