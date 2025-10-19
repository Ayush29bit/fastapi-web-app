from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = "postgresql://postgres:Ayush%4029@localhost:5432/ayush_db"

engine = create_engine(db_url)
Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)
session = Session()