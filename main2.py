from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

DATABASE_URL = "sqlite:///./ticket.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
class FlightModel(BaseModel):
    id:int
    space_count: int
    from_to:str
class Flight(Base):
    __tablename__ = "flight"
    id = Column(Integer, primary_key=True, index=True)
    space_count = Column(Integer)
    from_to = Column(String)
    tickets = relationship("Ticket", back_populates="flight")

class Passenger(Base):
    __tablename__ = "passenger"
    id = Column(Integer, primary_key=True, index=True)
    passport = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    tickets = relationship("Ticket", back_populates="passenger")

class Ticket(Base):
    __tablename__ = "ticket"
    id = Column(Integer, primary_key=True, index=True)
    flight_id = Column(Integer, ForeignKey("flight.id"))
    passenger_id = Column(Integer, ForeignKey("passenger.id"))
    price = Column(Integer)
    date = Column(DateTime)
    flight = relationship("Flight", back_populates="tickets")
    passenger = relationship("Passenger", back_populates="tickets")

class Order(Base):
    __tablename__ = "order"
    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(Integer, ForeignKey("ticket.id"))
    amount = Column(Integer)

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/add_flight/")
def add_flight(space_count: int, from_to: str):
    db = SessionLocal()
    new_flight = Flight(space_count=space_count, from_to=from_to)
    db.add(new_flight)
    db.commit()
    db.refresh(new_flight)
    db.close()
    return {"space": new_flight.space_count, "from_to": new_flight.from_to}
@app.get("/get_flights")
def get_flights():
    db = SessionLocal()
    data = db.query(Flight).all()
    db.close()
    return list(data)
@app.delete("/delete_flight/{id}")
def del_flight(id:int):
    db = SessionLocal()
    flight = db.query(Flight).filter(Flight.id == id).first()
    if not flight:
        db.close()
        raise HTTPException(status_code=404, detail="flight not found")
    db.delete(flight)
    db.commit()
    db.close()
    return {"Message": "Student deleted succesfully"}
@app.put('/update/{id}')
def update(id:int,space_count: int, from_to: str):
    db = SessionLocal()
    flight = db.query(Flight).filter(Flight.id == id).first()
    if not flight:
        db.close()
        raise HTTPException(status_code=404, detail="Student not found")
    if space_count:
        flight.space_count = space_count
    if from_to:
        flight.from_to = from_to
    db.commit()
    db.refresh(flight)
    db.close()
    return flight
