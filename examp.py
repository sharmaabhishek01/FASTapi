from fastapi import FastAPI , HTTPException , Query,Path
import json
from pydantic import BaseModel , Field , computed_field 
from typing import Annotated , Literal 

app = FastAPI()

class patients(BaseModel):

    id : Annotated[int,Field(...,description="ID of the patient",examples=['1001'])]
    name: Annotated[int,Field(...,description="Name of the patient")]
    city: Annotated[int,Field(...,description="City of patient")]
    age: Annotated[int,Field(...,gt=0 , lt=120,description="Age of the patient")]
    gender: Annotated[Literal['male','female','other'],Field(...,description="Gender of patient")]
    height : Annotated[float,Field(...,gt=0,description="Height of the patient in  meters")]
    weight : Annotated[float,Field(...,gt=0,description="Weight of patient in kg")]


    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi

    @computed_field
    @property
    def verdict(self) -> str:

        if self.bmi < 18.5:
            return 'underweight'
        elif self.bmi < 25:
            return 'normal'
        elif self.bmi < 30:
            return 'normal'
        else:
            return 'obes'

def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)

        return data        
    




