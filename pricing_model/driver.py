import numpy as np
from scipy.stats import norm

from route import Route
from vehicle import Vehicle
from globals import OPTIMIZATION_TYPE, OPTIMIZATION_PARAMS


class Driver(Route, Vehicle):
    """
    An instance of the Driver Class represents a single driver within the Curri fleet. 
    The Driver has preferences and utility, and makes a decision about whether to accept a bid. 

    
    """
    def __init__(self, route, vehicle):
        """
        Initializes the Driver object. The driver represents one driver in the Curri fleet. 
        
        Properties are hard-coded to represent a driver who owns a 2011 Toyota Camry. 

        """

        self.route = route
        self.vehicle = vehicle

        self.get_driving_time()
        self.get_labor_costs()
        self.get_cost_curve()

        return
    
    def get_driving_time(self):
        """
        Finds the total time the driver spends driving: route_time + commute_time. 

        """

        self.commute_time = 20

        self.driving_time = self.commute_time + self.route.route_time

        return
    
    def get_labor_costs(self):
        """
        Cost of the Driver's time and energy. 
        
        """

        if OPTIMIZATION_TYPE == "DETERMINISTIC":
            """
            Deterministic Model sets a fixed target wage for drivers. 
            
            For contrast, the total surplus model or constrained profit maximization models 
            find the driver wage that best fits the customer's willingness to pay. These 
            models require more detailed models of customer and driver price sensitivity. 
            """
            # print(OPTIMIZATION_PARAMS)
            # print(OPTIMIZATION_PARAMS.get('DETERMINISTIC'))
            # print(OPTIMIZATION_PARAMS.get('DETERMINISTIC').get('hourly_wage'))
            self.hourly_wage_mean = OPTIMIZATION_PARAMS.get('DETERMINISTIC').get('hourly_wage')
            self.hourly_wage_stdev = 0.4 * self.hourly_wage_mean

            self.fixed_wage = OPTIMIZATION_PARAMS.get('DETERMINISTIC').get('fixed_wage')
        

        elif OPTIMIZATION_TYPE in ("MAX PROFIT", "MAX SURPLUS"): 
            """
            Maxizing models do not have a target wage. Instead, they solve for the wage that best
            fulfills the objective function. If there are lots of drivers on the road at a peak time,
            that wage will likely be lower than usual. If a drive is particularly unusual, asking for 
            e.g. a flatbed trailer in the middle of Maine at midnight, you might need to pay a bit more.

            The maximizing model sets each driver's hourly wage at their historical willingness-to-drive.

            """

            # Mean and stdev of distribution, $ / hour
            self.hourly_wage_mean = 25
            self.hourly_wage_stdev = 10

            # Point estimate of $
            self.fixed_wage = 5

        return

    
    def get_cost_curve(self):
        """
        Returns the probability distribution of potential driver costs. 

        Fixed
            Fixed Wage ($)
            Tolls ($)

        Distance
            MPG ($/M)
            Repairs ($/M)
            Depreciation ($/M)
        
        Distributional
            Time (build an average hourly cost rate)
            Hourly Wage (own distribution, multiply by)

        Fixed + Distance + Time

        Fixed = 
        Distance = 
        Time = Driving Time * Dist(Hourly Wage)

        Time (Median and SD)
        Hourly Wage (Median and SD)
        Time Costs = (Median and SD)

        Total Costs = Distribution. 
            Median: Time + Distance + Fixed
            SD: Time SD
        
        TODO: Fit hourly wage mean and stdev to historical data. 
        TODO: Truncate the distribution with a minimum wage. 

        """

        self.fixed_cost = self.fixed_wage + self.route.tolls

        self.distance_cost = self.route.distance * (self.route.gas_price / self.vehicle.mpg + \
                                    self.vehicle.repairs_rate + self.vehicle.depreciation_rate)

        self.time_cost_mean = self.route.route_time * self.hourly_wage_mean / 60
        self.time_cost_stdev = self.route.route_time * self.hourly_wage_stdev / 60

        self.total_cost_mean = self.fixed_cost + self.distance_cost + self.time_cost_mean
        self.total_cost_stdev = self.time_cost_stdev

        self.hourly_wage_dist = norm(loc = self.hourly_wage_mean,
                                     scale = self.hourly_wage_stdev)

        self.cost_curve = norm(loc = self.total_cost_mean,
                               scale = self.total_cost_stdev)

        return self.cost_curve

    
    def get_driver_probability(self, driver_price):
        """
        Returns the probability that bid > total_costs. 

        """
        driver_probability = self.cost_curve.cdf(driver_price)

        return driver_probability
    

    def report(self):
        """
        Reports key information about the driver.

        """

        print(f'Expected Driving Time: {round(self.driving_time,2)}')
        print(f'Expected Hourly Wage: {round(self.hourly_wage_mean,2)}')
        print(f'Expected Ride Cost: {round(self.total_cost_mean,2)}')

        print(f'Hourly Wage Distribution')
        print(f'    10th: ${round(self.hourly_wage_dist.ppf(.10),2)}')
        print(f'    25th: ${round(self.hourly_wage_dist.ppf(.25),2)}')
        print(f'    50th (Median): ${round(self.hourly_wage_dist.ppf(.50),2)}')
        print(f'    75th: ${round(self.hourly_wage_dist.ppf(.75),2)}')
        print(f'    90th: ${round(self.hourly_wage_dist.ppf(.90),2)}')

        print(f'Total Cost Distribution')
        print(f'    10th: ${round(self.cost_curve.ppf(.10),2)}')
        print(f'    25th: ${round(self.cost_curve.ppf(.25),2)}')
        print(f'    50th (Median): ${round(self.cost_curve.ppf(.50),2)}')
        print(f'    75th: ${round(self.cost_curve.ppf(.75),2)}')
        print(f'    90th: ${round(self.cost_curve.ppf(.90),2)}')

        print(f'Costs by Source')
        print(f'    Cost of Gas: ${round(self.route.distance * self.route.gas_price / self.vehicle.mpg,2)}')
        print(f'    Cost of Tolls: ${round(self.route.tolls,2)}')
        print(f'    Cost of Repairs: ${round(self.route.distance * self.vehicle.repairs_rate,2)}')
        print(f'    Cost of Depreciation: ${round(self.route.distance * self.vehicle.depreciation_rate,2)}')
        print(f'    Cost of Driver Hourly Wages: ${round(self.route.route_time * self.hourly_wage_mean / 60,2)}')
        print(f'    Cost of Driver Fixed Wages: ${round(self.fixed_wage,2)}')

        return
