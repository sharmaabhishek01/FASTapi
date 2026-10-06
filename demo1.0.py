## Data validation Concepts
from pydantic import BaseModel , EmailStr ,AnyUrl, Field
from typing import List,Dict,Optional,Annotated

class Student(BaseModel):  

    name : Annotated[str,Field(max_length=50,title="Name of the student",description="Give me the name of the student less the 50 char",examples=['Amit','Anup'])]
    email : EmailStr
    linkedin_url : AnyUrl
    age : int
    weight : Annotated[float, Field(gt=0 , Strict=True)]
    married : Annotated[bool,Field(default=None,description="Is student maried or no")]
    allergies: Annotated[
    Optional[List[str]],
    Field(default=None, max_length=5)
]
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
    print(student.email)
    print("Updated")   

student_info = {"name":"Abhishek sharma","age": 21, "email":"abhc@gmail.com","linkedin_url":"http://Linkedin.com/1234" ,"weight":23.6,"married":False,"allergies":['Eaching','Polen'],"contact_details":{"phone":"7779971644"}}      
student1 =  Student(**student_info)

update_student_data(student1)