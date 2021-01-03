import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    """
    queries necessary to drop tables
    if they exist are executed.
    
    Arguments:
        cur: cursor for database connection
        conn: connection to the database
    
    Returns:
        None
    """
        
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    queries necessary to create tables are 
    executed.
    
    Arguments:
        cur: cursor for database connection
        conn: connection to the database
    
    Returns:
        None
    """
        
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    connection to the existing DWH is created,
    functions to drop and create tables are called
    """
        
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()