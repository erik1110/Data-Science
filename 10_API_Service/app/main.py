from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import models
from database import engine
# import uvicorn

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get('/about')
def about():
    return {"data": "about page"}

@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    # only get 10 published
    if published:
        return {"data": f"{limit} published blogs from db" }
    else:
        return {"data": f"{limit} blogs from db" }

@app.get('/blog/unmatch')
def unmatch():
    # you should push this function before show
    # cause fastapi sequentially find the route
    return {"data": "unmatch" }

@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {"data": id }

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(request: Blog):
    return {'data': f'the title is {request.title}'}

# if __name__ == '__main__':
#     uvicorn.run(app, host="127.0.0.1", port=8000)