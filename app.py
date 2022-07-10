# import is datetime, NumPy, and Pandas
import datetime as dt
import numpy as np
import pandas as pd

# the dependencies we need for SQLAlchemy, 
# which will help us access our data in the SQLite database.
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from flask import Flask, jsonify

# add the code to import the dependencies that we need for Flask.
from sqlalchemy import create_engine, func

# Access the SQLIte database
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect the database into our classes
Base = automap_base()
Base.prepare(engine, reflect=True)

# create a variable for each of the classes so that we can reference them later
Measurement = Base.classes.measurement
Station = Base.classes.station

# create a session link from Python to our database
session = Session(engine)

# create a Flask application called "app."
app = Flask(__name__)

@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Hawaii Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

