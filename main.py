from fastapi import FastAPI
from models import Product

app=FastAPI()
@app.get("/")
def greet():
    return {"message": "Welcome"}

products=[
    Product(id=1, name="Laptop", price=999.99, description="A high-performance laptop", in_stock=True,quantity= 10),
    Product(id=2, name="Smartphone",price= 499.99,description= "A latest model smartphone",in_stock= True, quantity= 25),
    Product(id=3, name="Headphones", price=199.99,description= "Noise-cancelling headphones",in_stock= False,quantity=0),
]

@app.get("/products")
def get_products():
    return products
