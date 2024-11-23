from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()
""""
post: whenever you want to write something into your database
get: whenever you want to read from database
Delete: whenever you want to delete the information
put:- whenever you want to update the existing information


"""

class Information(BaseModel):
    name: str
    age: int
    email: str
@app.post("/save_information")
async def save_information(request_prams:Information):
    return {
        "name": request_prams.name,
        "age": request_prams.age,
        "email": request_prams.email
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)