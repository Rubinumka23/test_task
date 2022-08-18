from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv


load_dotenv()

SQLALCHEMY_DATABASE_URL = f'postgresql://{os.getenv("POSTGRES_USER")}:{os.getenv("POSTGRES_PASSWORD")}@{os.getenv("HOST_DB")}:{os.getenv("PORT")}/{os.getenv("POSTGRES_DB")}'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
