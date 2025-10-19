from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Boolean 
from database import session

Base=declarative_base()

class Product(Base):

    __tablename__="products"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    price=Column(Float,nullable=False)
    description=Column(String,nullable=False)
    in_stock=Column(Boolean,nullable=False)
    quantity=Column(Integer,nullable=False)