from datetime import datetime
from dateutil.parser import isoparse

def validate_iso_string(iso_string):
    """
    Converts ISO string to datetime. Throws error if conversion fails, 
    otherwise stores the new datetime object as a class attribute. 
    """
    dt_var = isoparse(iso_string)
    assert type(dt_var)==datetime, "Check ISO format of: " + iso_string
    return dt_var