import json

class Objective:
        """
        Class: Objective is the class whose result is maximized by the Optimizer class. 
        """
        def __init__(self, transaction):
                """
                Initializer: Stores JSON object inputs and database connection inputs as class attributes. 
                """
                self.customer_price = transaction.get('customer_price', None)
                self.driver_price = transaction.get('driver_price', None)
                self.bid_probability = transaction.get('bid_probability', None)
                self.completed_probability = transaction.get('completed_probability', None)
        
        def calculate_expected_profit(self):
                """
                Function: Calculates gross profit given both prices and both probabilities. 

                TODO: New inputs for the cost function. 
                Curri unit costs. Bounty Hunter markup. 
                What else?

                """
                self.conditional_unit_profit = self.customer_price - self.driver_price
                self.expected_profit = self.bid_probability * self.completed_probability * self.conditional_unit_profit
        
                return self.expected_profit