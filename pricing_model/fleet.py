import numpy as np
import requests
from driver import Driver
from customer import Customer
from vehicle import Vehicle
from route import Route
from globals import DYNAMIC_FLEET


class Fleet(Customer, Route, Vehicle):
    """
    The Fleet class represents all of the drivers available for a particular delivery. By aggregating their
    individual cost curves, Fleet finds the probability that each driver will accept a particular bid and, 
    in aggregate, the overall probability of delivery for a particular price. 


    """

    def __init__(self, customer, route, vehicle, request):
        """
        Instantiates the Fleet object. 

        """

        self.receive(request)

        self.customer = customer
        self.route = route
        self.vehicle = vehicle

        self.get_driver_list()

        return

    def receive(self, request):
        """
        Store Fleet attributes from request

        """

        self.request = request

        self.available_drivers = self.request.get('available_drivers', None)

        self.available_drivers = int(self.available_drivers)

        available_drivers_error_message = """Did not receive integer input
                                             for available_drivers:
                                                 {self.available_drivers}
                                                 {type.available_drivers}"""

        assert type(self.available_drivers) == int, available_drivers_error_message
        
        return

    def get_driver_list(self):
        """
        Builds the Driver objects. Default settings assume all drivers are uniform,
        but supports future dynamic driver functionality that fetches information
        about individual drivers from the production database. 

        """

        if DYNAMIC_FLEET == True:

            return self.dynamic_drivers()
            
        else:
            
            return self.uniform_drivers()

    
    def uniform_drivers(self) -> list:
        """
        Builds a fleet of identical drivers. 

        """

        self.driver_list = list()

        for i in range(self.available_drivers):

            deh = Driver(self.route, self.vehicle)

            self.driver_list.append(deh)

        self.available_drivers = len(self.driver_list)

        return

    
    def dynamic_drivers(self) -> list:
        """
        DB query to production database to find available drivers. 

        """
        dynamic_drivers = []

        self.available_drivers = len(self.drivers)

        return dynamic_drivers


    def sort_driver_list(self):
        """
        Sorts list of drivers in-place by average estimated costs. 

        TODO: Activate DYNAMIC_FLEET, connect to BountyHunter. 

        """
        self.driver_list = sorted(self.driver_list, 
                                     key=lambda x: x.avg_cost)

        return self.driver_list


    def get_completion_probability(self, driver_price, ):
        """
        Inputs: driver_price
        Function: For each driver, report probability of acceptance using 
        Output: completion_probability = 1 - the probability that no driver accepts the price. 

        """

        driver_probabilities = []

        for driver in self.sorted_drivers:
            driver_probabilities.append(driver.get_driver_probability())
        
        inverse_probabilities = [1 - i for i in driver_probabilities]
        self.completion_probability = np.prod(inverse_probabilities)

        return self.completion_probability

    
    def report(self):
        """
        Reports key information about the fleet of drivers. 

        """
        print('------------')
        print('Fleet Report')
        print('------------')
        
        self.customer.report()
        self.route.report()
        self.vehicle.report()

        print("### Driver Report ###")
        for i in range(self.available_drivers):
            print()
            print(f'Driver #{i+1}')
            driver = self.driver_list[i]
            driver.report()
            print()

        return


