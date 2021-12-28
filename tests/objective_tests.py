from ..pricing_model.objective import Objective 

# Initialize the Objective class for a transaction
transaction = {'customer_price': 1500, 
               'driver_price': 1000,
               'bid_probability': .8, 
               'completed_probability': .8}

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