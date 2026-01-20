import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        host='database-1.cluster-c7uksu4gqdh3.ap-northeast-2.rds.amazonaws.com',
        database='trip_advisor',
        user='user',
        password='qwer1234'
    )
    return conn
