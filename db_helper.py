import psycopg2
from psycopg2 import Error
import os

# Connect to an existing database
db_user = os.environ.get("DB_USER")
db_pw = os.environ.get("DB_PW")
db_host = os.environ.get("DB_HOST")
db_port = os.environ.get("DB_PORT")
db_name = os.environ.get("DB_NAME")
connection = psycopg2.connect(
                                user=db_user,
                                password=db_pw,
                                host=db_host,
                                port=db_port,
                                database=db_name
                                )

def insert(count):
    cur = connection.cursor()
    insert_query = """ 
                    INSERT INTO cmd (SKILL,COUNT) 
                    VALUES ('calc',%s)
                    """
    cur.execute(insert_query,count)
    connection.commit()
    cur.close()

def update(c):
    cur = connection.cursor()
    update_query = """
                    Update cmd
                    set count = %s
                    where skill = 'calc'
                    """
    cur.execute(update_query,(c,))
    connection.commit()
    cur.close()


def retrieve():
    cur = connection.cursor()
    cur.execute("SELECT count FROM cmd ORDER BY count")
    row = cur.fetchone()
    while row is not None:
        count = int(row[0])
        row = cur.fetchone()
    connection.commit()
    cur.close()
    return count
