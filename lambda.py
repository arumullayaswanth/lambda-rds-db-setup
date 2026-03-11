import os
import pymysql
import boto3

db_host = os.environ['DB_HOST']
db_user = os.environ['DB_USER']
db_pass = os.environ['DB_PASS']
new_db_name = "test"
table_name = "mytable"

def connect_to_rds():
    connection = pymysql.connect(
        host=db_host,
        user=db_user,
        password=db_pass,
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

def lambda_handler(event, context):
    connection = None
    try:
        connection = connect_to_rds()
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {new_db_name};")
            cursor.execute(f"USE {new_db_name};")
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
            return {
                'statusCode': 200,
                'body': f"Database '{new_db_name}' and table '{table_name}' created successfully."
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
    finally:
        if connection:
            connection.close()
