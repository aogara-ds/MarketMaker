

# Decide whether the fleet will be uniform or dynamic. 
# Dynamic fleet requires runtime access to production DB. 

DYNAMIC_FLEET = False


# Set the type of optimization to be performed by the model. 
# See README.md for differences between models. 

OPTIMIZATION_TYPE = "DETERMINISTIC"

OPTIMIZATION_TYPES = ("DETERMINISTIC",
                      "MAX CONSTRAINED PROFIT",
                      "MAX TOTAL SURPLUS")

OPTIMIZATION_PARAMS = {"DETERMINISTIC": 
                            {"hourly_wage": 25,
                             "fixed_wage": 5,
                             "target_profit": 0.20},

                       "MAX CONSTRAINED PROFIT": 
                            {"minimum_wage": 20,
                             "maximum_profit": 0.40},

                       "MAX TOTAL SURPLUS": None}


# Build the Optimizer. init imports the optimization type and runs the ifelse chain. 
# Deterministic Optimization gives the bid. 
# Run Objective for reporting. 
# Build response. 



