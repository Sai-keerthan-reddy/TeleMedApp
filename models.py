from sqlalchemy import create_engine,Integer, String, Boolean,DateTime, Column,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__='users'
    
    id=Column(Integer,primary_key=True)
    name= Column(String,nullable=False)
    email =Column(String,unique=True, nullable=False)
    hashed_password =Column(String)

    #relationships 
    appointments_as_patient = relationship("Appointment", foreign_keys="Appointment.patient_id")
    appointments_as_doctor = relationship("Appointment", foreign_keys="Appointment.doctor_id")
    health_records = relationship("HealthRecord", back_populates="patient")
    prescriptions_given = relationship("Prescription", foreign_keys="Prescription.doctor_id")
    prescriptions_received = relationship("Prescription", foreign_keys="Prescription.patient_id")

    
class Appointments(Base):
    __tablename__='appointments'

    id= Column(Integer,primary_key=True)
    patient_id=Column(Integer,ForeignKey('users.id'))
    doctor_id= Column(Integer,ForeignKey('users.id'))
    datetime=Column(DateTime,default=datetime.utcnow)
    status=Column(String)

    patient = relationship("User",foreign_keys=[patient_id])
    doctor = relationship("User",foreign_keys=[doctor_id])

class healthRecord(Base):
    __tablename__ = 'health_records'

    id= Column(Integer,primary_key=True)
    patient_id = Column(Integer, ForeignKey('users.id'))
    date = Column(DateTime, default =datetime.utcnow)
    metric_type = Column(String)
    metric_value = Column(String)

    patient = relationship("User", back_populates="health_records")

class Prescription(Base):
    __tablename__ ='prescription'

    id= Column(Integer,primary_key=True)
    patient_id = Column(Integer, ForeignKey('users.id'))
    doctor_id = Column(Integer, ForeignKey('users.id'))
    medication_name = Column(String)
    dosage= Column(String)
    instructions = Column(String)
    date_issued= Column(DateTime, default = datetime.utcnow)

    doctor = relationship("User",foreign_keys=[doctor_id])
    patient= relationship("User",foreign_keys=[patient_id])


