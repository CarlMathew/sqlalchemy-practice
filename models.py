from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from credentials import Credentials
import os

Base = declarative_base()



class Job(Base):

    """_summary_
        Emit Job Database
    """

    __tablename__ = "jobs"
    job_id = Column("job_id", String(200), primary_key = True)
    job_name = Column("job_name", String(200))
    average_salary = Column("avg_salary", DECIMAL(10, 2))

    def __init__(self, job_id, job_name, average_salary):

        self.job_id = job_id
        self.job_name = job_name
        self.average_salary = average_salary
    

    def __repr__(self):
        return f"{self.job_name}: {self.avg_salary}"
    

class Person(Base):
    """
        Emit People Database

    """
    __tablename__ = "people"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    firstname = Column("firstname", String(200))
    lastname = Column("lastname", String(200))
    age = Column("age", Integer)
    gender = Column("gender", CHAR(1))
    job = Column("job_id", ForeignKey("jobs.job_id"))


    def __init__(self, id, firstname, lastname, age, gender, job):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.job = job

    
    def __repr__(self):
        return f"({self.lastname}, {self.firstname}), Age: {self.age}, Gender: {self.gender}"




if __name__ == "__main__":
    user, password, host, port, database = Credentials()
    engine =  create_engine(url = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, database))
    Base.metadata.create_all(bind=engine)
    print("Successfully updated the database")

