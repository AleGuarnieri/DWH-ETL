import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """
    queries necessary to EXTRACT data
    from S3 and load them into Redshift
    are executed.
    
    Arguments:
        cur: cursor for database connection
        conn: connection to the database
    
    Returns:
        None
    """
    
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """
    queries necessary to TRANSFORM data
    and LOAD them from staging tables into 
    analytical tables in Redshift
    are executed.
    
    Arguments:
        cur: cursor for database connection
        conn: connection to the database
    
    Returns:
        None
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
