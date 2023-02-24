# ALDA PROJECT

## About this repo

Python project that generates a table with 50 random data from a Colombian census, the number of rows is generated by a parameter entered by a user, response files are .csv and .xlsx 

## Python Version

Python 3.10.5 

## Running locally and testing

* Create virtual enviroment: `virtualenv env`
* To install dependencies: `pip install -r requirements.txt`
* To run test: `./test.sh` 
* To run main.py: `./run.sh`

## Current Coverage

To run `coverage`, make sure that you have it installed in your pc, if not run `pip install coverage`, then run the requirements.txt. After that run `coverage run -m unittest discover` and `coverage report` it show you the following table:

![image](https://user-images.githubusercontent.com/90010884/220839080-686c48c9-eb2a-43a3-9f97-dee8c53504ab.png)


## Code Beautifer

After install Black, run de comand `black . -l 120` to beautifier you code
