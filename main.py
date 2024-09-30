from datetime import datetime
from typing import Union
from fastapi import FastAPI, Body

app = FastAPI()

product = []

@app.get("/api/v1/")
def index():
    return {"Hello": "World"}

@app.get("/api/v1/{isim}")
def deneme(isim:str,soyisim:str =None):
    return {"isim":isim, "soyisim":soyisim}

@app.get("/api/v1/ping")
async def isServiceActive():
    context = {
        "status" : True,
        "running" : "Service is Running on port :8000",
        "time": datetime.now()
    }
    return {"context":context}


@app.get("/api/v1/products/{item_id}")
async  def getProducts(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/api/v1/products")
async def createProduct(item =Body()):
    if item not in product:
        product.append(item)
    return {"product":product}
