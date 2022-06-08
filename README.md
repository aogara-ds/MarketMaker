# Introduction
This repository prototypes a dynamic pricing algorithm for a delivery marketplace. 

# Model Architecture
The model is built on seven data structures:
* __Customer:__ Submits a request for a delivery consisting of an origin, destination, vehicle type, priority status, and metadata. 
* __Driver:__ Models each individual driver that can fulfill delivery requests. Includes methods for calculating driver willingness-to-supply curve. 
* __Route:__ Stores key information about a requested delivery route, including estimated travel time, toll costs, and traffic. 
* __Vehicle:__ Stores the fuel efficiency, cost of repairs, cost of insurance, and other relevant information about the costs of operating each vehicle type. 
* __Fleet:__ Composed of individual Drivers, the Fleet class enables estimation of the market's current clearing price. 
* __Objective:__ The algorithm is designed for three potential objective functions:
  1. _Cost-Plus Pricing_: Drivers are paid an hourly target take-home wage. Profit is fixed. The customer price is driver payout plus profit.  
  2. _Constrained Profit Maximization_: Maximizes expected profit by optimizing customer price and driver payout, subject to constraints on prices, wages, and profit. Requires estimation of the price elasticities of supply and demand. Expected profit is defined as:
     $$ E(Profit) = (Customer Price - Driver Payout) * P(Customer Bid | Customer Price) * P(Driver Fulfillment | Customer Bid, Driver Payout)$$
  3. _Total Surplus Maximization_: Maximizes the sum of profit, driver surplus, and customer surplus. _Preferred long-run objective._ 
* __Optimizer:__ Calculates the optimal customer price and driver payout for a given request. 
