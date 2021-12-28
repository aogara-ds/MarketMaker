import psycopg2

DB_NAME = ""
DB_USERNAME = ""
DB_PASSWORD = ""
DB_HOST = ""
DB_PORT = ""

def get_db_conn():
    """
    Yields: a psycopg connection object initialized with pricing DB credentials
    """

    return psycopg2.connect(
        host = DB_HOST,
        port = DB_PORT,
        user = DB_USERNAME,
        password = DB_PASSWORD,
        database = DB_NAME
    )