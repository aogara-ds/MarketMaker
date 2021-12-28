# Curri Pricing Model


# Structure of the Pricing Model
## Customer

## Driver

## Route

## Vehicle

## Fleet (composed of Drivers)

## Objective

## Optimizer


# Impact on Performance
* Lowering prices for customers by %
* Increasing wages for drivers by $ / hr
* Benefitting Curri's bottom line by $

Problems to Fix:
* Unpaid Tolls 
* Cancellation Costs (App Store review)


# Pricing Model API
## How to connect

## Questions for Asif


# Reporting
# TODO: Augment internal dashboard views of current available drivers. 




# Types of Prices
## Maximizing surplus
The gold standard of pricing. Maximizes total value created for the customer, the driver, and Curri. 

Inputs
* Request

Outputs
* Response

Model Requirements
* Customer Model: Detailed model of price sensitivity based on historical transaction data. 
* Driver Model: Detailed model of price sensitivity basedd on historical transaction data. 

## Contrained profit maximization
The run-of-the-mill, for-profit company standard. Maximizing profits while ensuring drivers and customers are taken care of. Constraints would include a minimum hourly wage for the driver and a maximum allowable profit for Curri. 

Inputs
* Request
* Constraints

Outputs
* Response

Model Requirements
* Also requires detailed models of both customer and driver. 

## Fixed profit, fixed driver wages
A good place to start. Find the lowest price that's reasonably profitable for both Curri and the driver, and leave the decision to the customer. 

Inputs
* Request
* Driver Target Wage
* Curri Target Profit

Outputs
* Response





# Future Developments
* Predicting seasonality. You should charge more on work days at driving times, and less on the off-peak hours. 

