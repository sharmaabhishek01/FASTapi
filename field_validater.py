from pydantic import BaseModel , EmailStr ,AnyUrl, Field, field_validator
from typing import List,Dict,Optional,Annotated

class Student(BaseModel):  

    name : str
    age : int
    email : EmailStr
    weight : float
    married : bool 
    allergies : List[str]
    contact_details : Dict[str, str]

    @field_validator('email')
    @classmethod

    def email_validator(cls , value):

        valid_domain = ['hdfc.com','icici.com']
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domain:
            raise ValueError('No a valid domain')

        return value
    

    @field_validator('name')
    @classmethod

    def transform_name(cls, value):
        return value.upper()
    

    @field_validator('name', mode='after')
    @classmethod

    def validate_age(cls , value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age in should between 0 and 100')

        

def student_updated_info(student : Student):
    print(student.name)
    print(student.age)
    print(student.weight)
    print(student.married)
    print(student.allergies)
    print(student.contact_details)
    print(student.email)
    print('updated')

student_info = {"name":"Abhishek sharma","age": 21, "email":"abc@hdfc.com" ,"weight":23.6,"married":False,"allergies":['Eaching','Polen'],"contact_details":{"phone":"7779971644"}}      
student1 =  Student(**student_info)

student_updated_info(student1)