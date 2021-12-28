import numpy as np
import psycopg2
from get_db_conn import *
from utils import validate_iso_string

class Customer:
    def __init__(self, request):
        """
        Initializes Customer object with request information. 
        Stores the request information, but does not calculate
        the customer probability until called by Optimizer. 


        """
        # Store Customer attributes from request
        self.user = request.get('user', None)
        self.account = request.get('account', None)
        self.request_time_iso = request.get('request_time', None)

        # Validate inputs from request
        self.request_time_dt = validate_iso_string(self.request_time_iso)
        # self.validate_user()
        # self.validate_account()

        # Calculate Route information

        
        return


    def customer_conversion_query(self):
        """
        Function: Build DB query for customer conversion with Nathan Jones.

        """

        return

    def get_customer_probability(self, customer_price):
        """
        Returns probability that the customer accepts a customer_price. 
        
        TODO: Generate customer probability from conversion query data. 
        TODO: Make customer probability responsive to price. 
        """

        print('running')

        return np.random.uniform(0,1)
    
    def report(self):
        """
        Reports key information about the Customer. 
        
        """
        print()
        print("### Customer Report ###")
        print(f"User: {self.user}")
        print(f"Account: {self.account}")
        print()