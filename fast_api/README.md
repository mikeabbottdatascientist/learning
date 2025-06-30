# Purpose
This folder is for putting together a basic fastapi

# Notes
1. The *convention* when building any http api is to use the following methods for the following purposes, but note that fastapi does not enforce this in any way. you can use the methods however you want.:
  * POST: to create data
  * GET: to read data
  * PUT: to update data
  * DELETE: to delete data
2. Note that you can use a pydantic AfterValidator in the annotation part of an annotated type for a request parameter


# Questions
1. When you refer to the "path", does that include query items? (things that come after the question mark)
2. What if I wanted my request parameter validation to depend on something external, like values in a database?
  * See "fastapi Dependencies"

# Terminology
* Path: the part of the URL that comes after the host address. Also called an "endpoint" or "route"
* OpenAPI: An open specification for defining the schema of APIs
* Operation: How the OpenAPI specification refers to the HTTP "Methods" (POST, GET, PUT, DELETE, OPTIONS, HEAD, PATCH, TRACE)