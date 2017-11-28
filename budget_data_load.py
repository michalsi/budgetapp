import psycopg2
import names
from datetime import datetime


# 2017-11-26 20:29:08.703323
# TODO: setup DB user first

# hashed Password1
USER_PASSWORD='79140b5312f64f7ccc7a3cdea8d2981be3925116598d14b0e997ef40e04bd609ff22248d1f273151'

conn = psycopg2.connect("dbname=budgetapp user=michals")
cur = conn.cursor()

cur.execute("SELECT MAX(id) FROM users;")
max_id = cur.fetchone()

timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')
user_name = names.get_full_name()