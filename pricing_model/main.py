import numpy as np
import pandas as pd

from customer import Customer
from route import Route
from vehicle import Vehicle
from driver import Driver
from fleet import Fleet
from objective import Objective
from optimizer import Optimizer
from transponder import receive, deliver

import get_db_conn as db
import json

# Handle request: store, parse, validate
# request = receive()
request = json.load(open('api/request_v1.json')).get('request', None)

# Build three new custom-designed data structures
customer = Customer(request)
route = Route(request)
vehicle = Vehicle(request)

# Assemble your fleet of Curri drivers
fleet = Fleet(customer, route, vehicle, request)
fleet.report()

"""
# Generate optimal bid
objective = Objective(customer, route, vehicle, fleet)
optimizer = Optimizer(objective)

# Deliver API response
response = optimizer.response()
deliver(request, response)

"""

# Store results in pricing DB


# Pricing Database Connection
# TODO: Set up pricing DB
"""
conn = db.get_db_conn()
curson = conn.cursor()

"""