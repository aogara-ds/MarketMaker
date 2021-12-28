import numpy as np
import math
import random
import requests

from datetime import datetime
from dateutil.parser import isoparse

from utils import validate_iso_string


class Route:
    """
    Route calculates and stores information about the customer's requested route. It is received by
    the API as part of the JSON payload from the customer request and stored in this Route class. 
    Then the object calculates new information about the route, learning distances and travel times
    until being passed onto a Driver for cost estimation, bidding, and delivery. 


    Initializing Information:
        * Address A
        * Address B
        * Pickup Time
    
    Outputs:
        * Distance
        * Route Time
        * Tolls
    

    TODO: Build multiple stop functionality. 

    """

    def __init__(self, request):
        """
        Initializes the Route object from the provided request by
        parsing, validating, and storing request information. 

        Calculates new Route information including:
            * Distance
            * Route Time
            * Gas Price
            * Tolls

        """
        # Store Route attributes from request
        self.address_a = request.get('address_a', None)
        self.address_b = request.get('address_b', None)
        self.pickup_time_iso = request.get('pickup_time', None)
        self.priority_status = request.get('priority_status', None)


        # Validate inputs from request
        self.pickup_time_dt = validate_iso_string(self.pickup_time_iso)
        # self.validate_address('address_a', 'address_b')
        self.validate_priority_status()


        # Calculate Route information
        self.get_route_time()
        self.get_distance()
        self.get_tolls()
        self.get_gas_price()
        
        return
    
    def validate_priority_status(self):
        """
        Validates that provided priority status string 
        matches one of the three possible values. 

        """
        priority_statuses = ('Rush', 'Same Day', 'Scheduled')
        priority_valid = self.priority_status in priority_statuses
        priority_error_message = f"""Check priority status. 
        Not one of the three acceptable inputs: {priority_statuses}"""

        assert priority_valid, priority_error_message

        return


    def get_route_time(self):
        """
        HTTP request to Google Maps API for driving time. 
        Calculates optimal route and driving time in minutes. 

        Currently pulls from normal distribution with mean = 60.

        """

        self.route_time = max(np.random.normal(60, 30), 0)

        return
    

    def get_distance(self):
        """
        HTTP request to Google Maps API for driving distance. 

        Currently pulls from normal distribution with mean = 35.
        """

        self.distance = max(np.random.normal(35, 15), 0)

        return


    def get_tolls(self):
        """
        Connects to third-party API to find the toll price of a route. 

        Currently randomly assigns a $10 toll to 20% of routes. 

        """
        toll_price = 10
        toll_prob = 0.20
        toll_roll = random.random()

        self.tolls = toll_price if toll_roll < toll_prob else 0

        return

    def get_gas_price(self):
        """
        Connects to third-party API to find the price for a gallon of gas. 
        Will likely require geographic information to calibrate prices. 

        Currently hardcodes gas_prices at 3.50 ($ / gallon) 

        """
        self.gas_price = 3.50

        return


    def get_directions():
        """
        Inputs: Address A, Address B, Pickup Time
        Outputs: Distance, Driving Time (Best Guess, Optimistic, and Pessimistic), Tolls?
        Body: Returns the results of an HTTP request to the Google Maps Directions API. 
        
        Directions Documentation here: https://developers.google.com/maps/documentation/directions/overview

        Returns:
            * Best Guess Time
            * Optimistic Time
            * Pessimistic Time


        """

        return
    
    def report(self):
        """
        Reports key information about the Route. 
        
        """
        print()
        print("### Route Report ###")
        print(f"Address A: {self.address_a}")
        print(f"Address B: {self.address_b}")
        print(f"Pickup Time: {self.pickup_time_iso}")
        print(f"Priority Status: {self.priority_status}")
        print()
        print(f"Route Time (minutes): {round(self.route_time,2)}")
        print(f"Distance (miles): {round(self.distance,2)}")
        print()
        print(f"Gas Price ($ / gallon): {round(self.gas_price,2)}")
        print(f"Tolls ($): {round(self.tolls,2)}")
        print()
        print()

        return
