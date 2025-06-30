'''Minimal fastapi
'''
## Imports
# Built-in
import logging

# Installed
from fastapi import FastAPI
import uvicorn

# Local
##

# Create Logger
logger = logging.getLogger(__name__)


from fastapi import FastAPI
app = FastAPI()

# Basic
@app.get("/")
def root():
    return {"message": "Hello World"}

# Path parameters This is what will show if you go to url
# "host/view_params/param_1" Note that the parameter name in the
# decorator must match what's used in the function definition
@app.get("/view_param/{param_1}")
def view_param(param_1:str):
    return {"param_1":f"{param_1}"}

@app.get("/view_params/{param_1}/{param_2}")
def view_params(param_1:str,param_2:str):
    return {"param_1":f"{param_1}", "param_2":f"{param_2}"}


##### Order of path declarations matters. Fastapi will always go with whichever
##### path is matched first. Consider the following two
##### approaches, which give different behavior:

### Approach 1:
# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "the current user"}

# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}
###

### Approach 2
# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}

# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "the current user"}
###
#####


### What if you only want some options to be available as path parameters?
from enum import Enum
# Here, hs, cb, and csr are the "enum members" and "house", "cobb" and
# "caesar" are their corresponding "values". (values can be accessed
# using member.value) When something is defined as a type Salad, it must
# be one of the members, not one of the values. (eg. cool_var:Salad = Salad.hs)
class Salad(str,Enum):
    hs = "house" 
    cb = "cobb"
    csr = "caesar"

# When entering the url in an http request, you enter the param as one
# of the values (not members). However, once it gets passed into the
# function it becomes a member type. So going to (salads/house) will
# make "type" in the function be Salad.hs. so print(saltype) will show
# Salad.hs. But, when you return a member in the json, it automatically
# converts it back to its value. Basically, as long as you are in python
# function-land, it is the member, but at the interface with http
# request and response it is the value of that member.
@app.get("/salads/{saltype}")
def print_salad(saltype:Salad):
    print(saltype)
    return {'salad type': saltype}
###


### Query Parameters
# In an http request, query parameters are "key=value" pairs that come
# at the end of the URL after a "?" and separated by "&". eg.
# wow.com/accounts?user_id=34&account=checking. Any parameter included
# in the function definition which is NOT listed as a path parameter is
# assumed to be a query parameter.
@app.get("/greet/{greeting}")
def greeting(greeting:str, name:str = 'generic person'):
    return{'message':f'{greeting}, {name}'}
###

##### Request body
# You can tell a fastapi function to use the request body as a parameter
# in the same way that you do for query parameters. 
# NOTE THAT EVEN THOUGH FASTAPI SUPPORTS REQUEST BODIES IN GET
# OPERATIONS, THIS IS HIGHLY DISCOURAGED AS THE GET METHOD IS NOT
# INTENDED TO CARRY A REQUEST BODY. Fastapi determines
from pydantic import BaseModel
class Hero(BaseModel):
    name: str
    power: str
    team: str
###
@app.post('/hero')
def post_hero(hero:Hero):
    # Typically there would be some sort of storing of the object, but
    # for the purposes of demonstration I am just having it return the
    # same info
    return hero
###

### Passing multiple body parameters
# An html request only has one body, so you would think there could only
# be one request body parameter. Not so! If you define more than one
# param as a pydantic model, then it will treat all of them as key-value
# pairs in the request body. So in the following example it would expect
# the request body to look like this:
#    {
#        "hero1": {
#            "name": x
#            "power": y
#            "team": z
#        },
#        "hero2": {
#            "name": i
#            "power": j
#            "team": k
#        },
#        "hero3": {
#            "name": a
#            "power": b
#            "team": c
#        },
#    }
@app.post('/teamofthree')
def post_team_of_three(hero1:Hero, hero2:Hero, hero3:Hero):
    return {'message':'wow'}
###

#####

# BUT HOW DOES FASTAPI DIFFERENTIATE path parameters, query parameters,
# and request bodies? for each parameter in the function definition, it
# does the following:
#   1. If it matches a parameter in the decorator path, then it is a
#      path parameter
#   2. If it has a type hint of Annotated[some_type, X] where X is an
#      explicit fastapi validation function (including Query(), Path(),
#      Body(), Header(), etc), then it will be explicitly that type of
#      parameter. (for example if you have a pydantic model with
#      multiple attributes, it would normally be treated as a request
#      body, but if you explicitly do Query() in the annotation, then it
#      will instead treat each attribute as a separate query parameter)
#   3. If it is a singular type (float, int, bool, string, Enum, etc), then it is a
#      query parameter
#   4. If it is a Pydantic model (or inherits from one), then it is
#      treated as the request body.




# This section is not necessary, but can be useful. Typically, in
# production you would pass this file as an argument to use something
# like gunicorn instead of running this as a script directly (in which
# case this part wouldn't even run anyway). but for dev purposes this is
# completely sufficient.
if __name__ == '__main__':
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
        reload=True
    )