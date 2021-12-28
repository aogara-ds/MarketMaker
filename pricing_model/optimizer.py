
from globals import OPTIMIZATION_TYPE, OPTIMIZATION_PARAMS


class Optimizer:
        """
        Class: Optimizer finds the optimal bid according to the Objective. 
        """
        def __init__(self, transaction):
            """
            Initializes the Optimizer with a particular objective type. 

            """

            self.optimization_type = OPTIMIZATION_TYPE
            self.optimization_params = OPTIMIZATION_PARAMS

            if self.optimization_type == "Deterministic":
                """
                Run deterministic pricing model. 

                """

                print("Implement Deterministic Model.")

            
            else:
                print("Maximizing models require further implementation.")