import pandas as pd
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

df=pd.read_excel("InternshipData.xlsx")
print("Records extracted:", len(df))

con=None
cursor=None

try:
    con=mysql.connector.connect(
        host=os.getenv("Db_host"),user=os.getenv("Db_user"),password=os.getenv("Db_PW")
    )
    print("Connection Established.")
    cursor=con.cursor()
    cursor.execute("create database if not exists internship_db")
    cursor.execute("use internship_db")
    cursor.execute("""
        create table if not exists ExampleData (
            order_id bigint primary key,region varchar(100),country varchar(100),item_type varchar(100),sales_channel varchar(50),
            order_priority varchar(20),order_date date,ship_date date,units_sold int,unit_price decimal(12,2),unit_cost decimal(12,2),
            total_revenue decimal(15,2),total_cost decimal(15,2),total_profit decimal(15,2)
        )
    """)
    print("Database and table created.")

    df.columns=[
        "order_id","region","country","item_type","sales_channel","order_priority","order_date",
        "ship_date","units_sold","unit_price","unit_cost","total_revenue","total_cost","total_profit"
    ]

    rows=list(df.itertuples(index=False, name=None))

    sql="""
        insert into ExampleData (
            order_id, region, country, item_type,
            sales_channel, order_priority, order_date,
            ship_date, units_sold, unit_price, unit_cost,
            total_revenue, total_cost, total_profit
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s)
    """

    cursor.execute("delete from ExampleData")
    cursor.executemany(sql, rows)

    print("Records loaded:", cursor.rowcount)

    cursor.execute("select count(*) from ExampleData")
    loaded=cursor.fetchone()[0]
    expected=len(df)

    print("Rows in database:", loaded)
    if loaded!=expected:
        raise RuntimeError(
            print("Load failed. \nExpected:",expected, " rows.\nOutput:",loaded,".")
        )

    con.commit()
    print("Data verification successful!")

except Exception as e:
    if con is not None and con.is_connected():
        con.rollback()
    print("Pipeline failed:", e)
finally:
    if cursor is not None:
        cursor.close()

    if con is not None and con.is_connected():
        con.close()

    print("Connection closed.")
