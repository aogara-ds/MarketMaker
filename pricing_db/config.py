import psycopg2

"""
Creates the pricing database and establishes some metadata.

Currently erroneous. Figure out how to create the pricing database. 
Maybe even throw a vehicles table in there. 

Then, once you have an ORM, Build the pricing db. 
Start with a vehicles table, and query it from Driver.  

"""


#establishing the connection
conn = psycopg2.connect(
   database="pricing", 
   user='postgres', 
   password='postgres', 
   host='127.0.0.1', 
   port= '5432'
)
conn.autocommit = True
cursor = conn.cursor()

# Create the database
sql_create_db = '''CREATE database pricing'''
cursor.execute()

# Create the vehicles table
sql_create_vehicles = """


"""


#Closing the connection
conn.close()