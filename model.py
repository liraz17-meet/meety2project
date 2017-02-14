
from sqlalchemy import Column,Integer,String, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, func
from passlib.apps import custom_app_context as pwd_context
import random, string
from itsdangerous import(TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

Base = declarative_base()

class Questions(Base):
	__tablename__ = 'questions'
	id = Column(integer, primary_key=True)
	subject = Column(string)
	sub_subject = Column(string)
	image = 
	description = Column(TextArea)
	answers = relationship("Answers", back_populates="questions")


class Answers(Base):
	__tablename__ = 'answers'
	id = Column()
	image = 
	description = 
	question_id = Column(Integer, ForeignKey=True)
	questions = relationship("Questions", back_populates="answers")

class Users(Base):
	__tablename__ = 'users'
	id = Column(integer, primary_key=True)
	name = Column(string)
	password = Column(string) 
	email = Column(string) 
	answerscount = Column(string) 



Liraz = User(id = 2. name = Liraz Shahar, password = pass, email = )





engine = create_engine('sqlite:///fizzBuzz.db')


Base.metadata.create_all(engine)