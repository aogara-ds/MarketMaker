
from route import Route
import json

# TODO: Fix the relative import of objective.py from ../pricing_model
# https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time

from objective import Objective 

# Initialize the Objective class for a transaction
transaction = {'customer_price': 100, 
               'driver_price': 60,
               'bid_probability': .20, 
               'completed_probability': .80}

obj = Objective(transaction)

# Calculate expected profit for the transaction
expected_profit = obj.calculate_expected_profit()

# Print results
print(f"Probability that the customer bids: {round(obj.bid_probability,2)}")
print(f"Probability that a driver accepts: {round(obj.completed_probability,2)}")
print(f"Profit if the transaction happens: ${round(obj.conditional_unit_profit,2)}")
print()
print(f"Expected Unit Profit: ${round(expected_profit,2)}")
print()

