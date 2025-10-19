from fastapi import FastAPI
from models import Product
from database import session , engine
import database_models 

app=FastAPI()

database_models.Base.metadata.create_all(bind = engine)

@app.get("/")
def greet():
    return {"message": "Welcome"}

products=[
    Product(id=1, name="Laptop", price=999.99, description="A high-performance laptop", in_stock=True,quantity= 10),
    Product(id=2, name="Smartphone",price= 499.99,description= "A latest model smartphone",in_stock= True, quantity= 25),
    Product(id=3, name="Headphones", price=199.99,description= "Noise-cancelling headphones",in_stock= False,quantity=0),
]

def get_db():
    db=session()
    try:
        yield db
    finally:
        db.close()
    
    
    
def initialize_database():
  db = session()
  count=db.query(database_models.Product).count()
  if count==0:
     for product in products:
        db.add(database_models.Product(**product.model_dump()))
  db.commit()  

@app.get("/products")
def get_products():
    db=session()
    db.query()
    return products

@app.get("/products/{product_id}")
def get_product_by_id(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    return {"error": "Product not found"}

@app.post("/products")
def add_product(product: Product):
    products.append(product)
    return product

@app.put("/products/{id}")
def update_product(id:int, product: Product):
  for i in range(len(products)):
    if products[i].id == id:
        products[i] = product
        return product
    
    return {"error": "Product not found"}
  

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for i in range(len(products)):
        if products[i].id == product_id:
            deleted_product = products.pop(i)
            return deleted_product
    return {"error": "Product not found"} 
