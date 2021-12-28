

class Vehicle:
    """
    The Vehicle Class represents the possible vehicles held by drivers and requested by customers. 
    This data abstraction allows us to represent common costs and benefits of different vehicles, 
    such as fuel efficiency, cost of maintenance, speed, and environmental impact. 

    TODO: Build and query Vehicle database table with information on each vehicle type. 

    """

    def __init__(self, request):
        """
        Instantiates Vehicle object using vehicle_type provided by request. 
        Retrieves the following information: mpg, Repairs, Depreciation. 

        # TODO: Parse States from addresses to find gas prices. 
        
        """
        # Store Vehicle attributes from request
        self.vehicle_type = request.get('vehicle_type', None)

        # Validate vehicle_type input
        self.validate_vehicle_type()

        # Fetch other information
        self.hardcode_vehicle()

        return
    
    def validate_vehicle_type(self):
        """
        Validates that the vehicle type provided by the request
        is one of the 11 vehicle types listed on Curri.com. 

        """
        vehicle_types = ('Car', 'SUV', 'Cargo Van', 'Pickup Truck',
                         'Rack Vehicle', 'Sprinter Van', 'Box Truck',
                         'Box Truck w/ Liftgate', 'Flatbed', 
                         'Stakebed', 'Freight')
        
        vehicle_valid = self.vehicle_type in vehicle_types

        vehicle_error_message = f"""Check vehicle_type.
        Not one of the {len(vehicle_types)} acceptable types:
        {vehicle_types}"""

        assert vehicle_valid, vehicle_error_message

        return

    
    def hardcode_vehicle(self):
        """
        Hardcodes values for vehicle attributes. 
        To be replaced by pricing DB query to vehicles table. 

        """

        self.mpg = 25
        self.repairs_rate = 0.04
        self.depreciation_rate = 0.10

        return
    
    def report(self):
        """
        Reports key information about the Vehicle. 
        
        """

        print("### Vehicle Report ###")
        print(f"Vehicle Type: {self.vehicle_type}")
        print(f"Fuel Efficiency (MPG): {self.mpg}")
        print()






    








