from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey,func
from sqlalchemy.orm import sessionmaker, relationship, declarative_base, joinedload
from datetime import timedelta
from models import department_model
from models import organization_model
from models import technician_model
from models import ticket_line_model
from models import ticket_model
from models import user_model
from models import base_model

# FastAPI setup
# app = FastAPI(
#     title="IT Ticketing System API",
#     description="API for Group 1's IT Ticketing System",
#     version="0.1",
# )

from flask import Flask, jsonify, request

app = Flask(__name__)

def run():
    # Start the API server
    app.run(debug=True)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.get("/Technicians/")
def read_technician_names():
    '''
    Returns the first and last names of all the technicians
    '''
    technician_model.read_technician_names()

@app.get("/Technicians/AvgTicketTimes/")
def read_technician_avg_ticket_times():
    '''
    TODO: Insert tooltip documentation here
    '''
    technician_model.read_technician_avg_ticket_times()

@app.get("/Users/TicketCounts/")
def read_user_ticket_counts(user_id=None):
    '''
    TODO: Insert tooltip documentation here
    '''
    user_model.read_user_ticket_counts(user_id=None)

@app.get("/Departments/AvgResolutionTimes")
def read_department_avg_resolution_time():
    '''
    Retrieve and print the average resolution times for each department.
    '''
    department_model.read_department_avg_resolution_time()

@app.get("/Technicians/TicketsInfo")
def read_technician_ticketinfo():
    '''
    Retrieve and print ticket information for each technician based on technician ID.
    '''
    technician_model.read_technician_ticketinfo()

@app.get("/Organizations/TicketCounts")
def read_organizations_tickets_count():
    '''
    Retrieve ticket counts for each organization.
    '''
    organization_model.read_organizations_tickets_count()

