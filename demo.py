## Type validation Concepts
from pydantic import BaseModel
from typing import List,Dict,Optional

class Student(BaseModel):  

    name : str
    age : int
    weight : float
    married : bool = False
    allergies : Optional[List[str]] = None
    contact_details : Dict[str, str]

def insert_student_data(student:Student):
    print(student.name)
    print(student.age)
    print(student.weight)
    print("Inserted")

def update_student_data(student:Student):
    print(student.name)
    print(student.age)
    print(student.weight)
    print(student.allergies)
    print(student.married)
    print("Updated")   

student_info = {"name":"Abhishek sharma","age": 21, "weight":23,"married":False,"allergies":['Eaching','Polen'],"contact_details":{"email":"abhisheksharma200201@gmail.com","phone":"7779971644"}}      
student1 =  Student(**student_info)

update_student_data(student1)