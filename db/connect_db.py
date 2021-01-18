import pymysql.cursors
import os
# Connect to the database
connection = pymysql.connect(host=os.getenv('DB_HOST'),
                             user=os.getenv('DB_USERNAME'),
                             password=os.getenv('DB_PASSWORD'),
                             db=os.getenv('DB_DATABASE'),
                             cursorclass=pymysql.cursors.DictCursor)
