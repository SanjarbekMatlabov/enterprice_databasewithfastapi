# from fastapi import FastAPI
# from pydantic import BaseModel,Field
# from sqlalchemy import create_engine,Column,Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "sqlite:///./dars.db"
# engine = create_engine(DATABASE_URL,connect_args={"check_same_thread": False})
# SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
# # bu bazoviy class hioblanib shundan barcha modellar voris oladi.
# Base = declarative_base()


# app = FastAPI()
# class Group(BaseModel):
#     direction: str
#     group_number: int
#     room_number: int
# class Student(BaseModel):
#     name: str
#     surname:str
#     age: int
#     address:str
# groups = []
# student = []
# group_students = []
# @app.post("/addgroup")
# def addGroup(data:Group):
#     groups.append(data)
#     return f"Group {data.group_number} muvaffaqiyatli qo'shildi"
# @app.post("/add_student")
# def add_student(data:Student,group_id:int):
#     student.append(data)
#     for group in groups:
#         if group.group_number == group_id:
#             group_students[group_id] = data
#         else: 
#             return f"{group_id} bunday guruh mavjud emas"
#     return f"{group_id} ga {data} muvaffaqiyatli qoshildi"
# @app.get("/get_student")
# def get_student(name:str,surname:str):
#     for i in student:
#         if i.name == name and i.surname == surname:
#             return f"{i} qidiruvingiz boyicha topildi"
#         else:
#             continue
#     return f"{name} {surname} ushbu talaba topilmadi"
# @app.get("/get_group")
# def get_group(g_number:int):
#     for i in groups:
#         if i.group_number == g_number:
#             return f"{i} seccess"
#         else:
#             continue
#     return f"{g_number} bunday guruh topilmadi"
# @app.delete("/delete_student")
# def delete_student(name:str,surname:str):
#     for i in student:
#         if i.name == name and i.surname == surname:
#             student.remove(i)
#             return f"{name} {surname} muvaffaqiyatli o'chirildi"
#         else:
#             continue
#     return f"{name} {surname} ushbu talaba topilmadi" 
# @app.delete("/delete_group")
# def delete_group(g_number:int):
#     for i in groups:
#         if i.group_number == g_number:
#             groups.remove(i)
#             return f"{g_number} guruh muvaffaqiyatli o'chirildi"
#         else:
#             continue
#     return f"{g_number} bunday guruh topilmadi"
# @app.put("/update_student")
# def update_student(name:str,surname:str):
#     for i in student:
#         if i.name == name and i.surname == surname:
#             i.name = name
#             i.surname = surname
#             return f"{name} {surname} muvaffaqiyatli tahrirlandi"
#         else:
#             continue
#     return f"{name} {surname} ushbu talaba topilmadi"
# @app.put("/update_group")
# def update_group(g_number:int,group:Group):
#     for i in groups:
#         if i.group_number == g_number:
#             i.direction = group.direction
#             i.group_number = group.group_number
#             i.room_number = group.room_number
#             return f"{g_number} guruh muvaffaqiyatli tahrirlandi"
#         else:
#             continue
#     return f"{g_number} bunday guruh topilmadi"

# from fastapi import FastAPI,HTTPException
# from sqlalchemy import create_engine,Column,Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "sqlite:///./dars.db"
# engine = create_engine(DATABASE_URL,connect_args={"check_same_thread": False})
# SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
# # bu bazoviy class hioblanib shundan barcha modellar voris oladi.
# Base = declarative_base()

# class Student(Base):
#     __tablename__ = "students"
#     id = Column(Integer,primary_key=True,index=True)
#     name = Column(String,index=True)
#     age = Column(Integer)

# Base.metadata.create_all(bind=engine)

# app = FastAPI()
# @app.post("/students/")
# def create_students(name:str,age:int):
#     db = SessionLocal()
#     new_student = Student(name=name, age=age)
#     db.add(new_student)
#     db.commit()
#     db.refresh(new_student)
#     db.close()
#     return {"id": new_student.id, "name":new_student.name,"age":new_student.age}
# @app.get("/students/")
# def get_students():
#     db = SessionLocal()
#     students = db.query(Student).all()
#     db.close()
#     return students
# # only one student
# @app.get("/students/{student_id}")
# def get_student(student_id: int):
#     db = SessionLocal()
#     student = db.query(Student).filter(Student.id == student_id).first()
#     db.close()
#     if student:
#         return student
#     raise HTTPException(status_code=404,detail="Student not found")

# @app.put("/student/{student_id}")
# def update_student(student_id:int,name:str = None, age:int = None):
#     db = SessionLocal()
#     student = db.query(Student).filter(Student.id == student_id).first()
#     if not student:
#         db.close()
#         raise HTTPException(status_code=404, detail="Student not found")
#     if name:
#         student.name = name
#     if age:
#         student.age = age
#     db.commit()
#     db.refresh(student)
#     db.close()
#     return student
# @app.delete("/students/{student_id}")
# def delete_student(student_id:int):
#     db = SessionLocal()
#     student = db.query(Student).filter(Student.id == student_id).first()
#     if not student:
#         db.close()
#         raise HTTPException(status_code=404, detail="Student not found")
#     db.delete(student)
#     db.commit()
#     db.close()
#     return {"Message": "Student deleted succesfully"}
from fastapi import FastAPI
app = FastAPI()
@app.post("/yuza")
def yuza(a:int,b:int):
    return {"result": a*b}