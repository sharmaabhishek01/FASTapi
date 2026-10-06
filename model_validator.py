from pydantic import BaseModel , EmailStr ,AnyUrl, Field, field_validator , model_validator
from typing import List,Dict,Optional,Annotated

class Student(BaseModel):  

    name : str
    age : int
    email : EmailStr
    weight : float
    married : bool 
    allergies : List[str]
    contact_details : Dict[str, str]

    
    

        

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