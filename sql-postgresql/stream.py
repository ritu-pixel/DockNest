conn = psycopg2.connect( # type: ignore
    dbname="testdb",
    user="ritu",
    password="secret",
    host="localhost",
    port="5432"
)
