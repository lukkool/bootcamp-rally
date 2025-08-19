from config import get_snowflake_connection
import pandas as pd


def query(sql, params=None):
    conn = get_snowflake_connection()
    df = pd.read_sql(sql, conn, params=params)
    conn.close()
    return df


def execute(sql, params=None):
    conn = get_snowflake_connection()
    cur = conn.cursor()
    if params:
        cur.execute(sql, params)
    else:
        cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()