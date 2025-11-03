#!pip install snowflake-connector-python

import snowflake.connector

# snowflake connection
conn = snowflake.connector.connect(
    user='<user>',
    password='<password>',
    account='<account>',
    warehouse='<warehouse>',
    database='<database>',
    schema='<schema>'
)

cursor = conn.cursor()

# create table
cursor.execute("""
CREATE OR REPLACE TABLE <tb_name> (
    id INT,
    nome STRING,
    email STRING
)
""")

# insert data
cursor.execute("""
INSERT INTO <tb_name> (id, name, email)
VALUES 
    (1, 'Alex', 'alex@email.com'),
    (2, 'Maria', 'maria@email.com')
""")

# validation
cursor.execute("SELECT * FROM <tb_name>")
for row in cursor.fetchall():
    print(row)

# close connection
cursor.close()
conn.close()