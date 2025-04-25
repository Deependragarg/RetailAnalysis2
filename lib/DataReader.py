from lib import ConfigReader
from pathlib import Path

#defining customer schema
def get_customer_schema():
    schema="customer_id int,customer_fname string,customer_lname string,username string,password string,address string,city string,state string,pincode string"
    return schema 

#creating customer dataframe
def read_customers(spark,env):
    conf = ConfigReader.get_app_config(env)
    #customers_file_path = conf["customers.file.path"]
    base_path = Path(__file__).resolve().parent.parent  # Go to project root
    customers_file_path = str(base_path / "data" / "customers.csv")
    return spark.read \
    .format("csv") \
    .option("header","true") \
    .schema(get_customer_schema()) \
    .load(customers_file_path)

#defining order schema
def get_order_schema():
    schema = "order_id int,order_date string,customer_id int,order_status string"
    return schema

def read_orders(spark,env):
    conf = ConfigReader.get_app_config(env)
    base_path = Path(__file__).resolve().parent.parent  # Go to project root
    orders_file_path = str(base_path / "data" / "orders.csv")
    #orders_file_path = conf["orders_file_path"]
    return spark.read \
    .format("csv") \
    .option("header","true") \
    .schema(get_order_schema()) \
    .load(orders_file_path)