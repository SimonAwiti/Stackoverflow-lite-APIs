# Stackoverflow-lite-APIs

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)]

# The application endpoints

## The following are API endpoints enabling one to: 
* Create account and log in
* Post a question
* View answers to the posted question
* view other questions and answers  
* Post answers to random questions  

## Here is a list of the functioning endpoints

| EndPoint                      | Functionality                    |  Actual routes                |
| :---                          |     :---:                        |    :---:                      |
| POST /Register user           |   Adds a new user                |  /api/v1/auth/sign up              |
| POST /log in   | User log in     |  /api/v1/auth/login    |
| GET /get questions  | Get a list of all questions |  /api/v1/questions     |

## Testing the endpoints

* Install python then using pip install .. install flask
* clone the repo
* Ensure that postman is installed
* From your terminal locate the repo and run: python run.py
* open postman and test the endpoints
* Use unittest to run the the tests

## Setting up and how to start the application

* Install python then using pip instal .. install flask
* clone the repo
* From your terminal Ensure that the virtual environment is activated
* From the terminal locate the repo and run: python run.py

## Technology used

* Python 3.6
* Flask framework
* Unittest for testing

## Background context 

Published POSTMAN documentation
[Documentation](https://documenter.getpostman.com/view/5353857/RWgtTwtr#intro)

# Written by: Simon Awiti
#### Copyright © Andela 2018 