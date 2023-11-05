from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from YelpGoogleAPI import getYelpGoogle

app = FastAPI()

origins = [
    "http://localhost:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/food")
async def getFood(keyword, price_range, user_radius, start_location, end_location): 
    print(keyword, price_range, user_radius, start_location, end_location)
    
    result = getYelpGoogle(keyword, price_range, user_radius, start_location, end_location)
    print(result)
    return result