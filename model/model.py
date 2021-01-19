from db.connect_db import connection
from flask import render_template

class Model:
    @classmethod
    def listRoom(self):
        try:
            with connection.cursor() as cursor:
                # SQL
                sql = "SELECT * FROM room"
                # Execute query.
                cursor.execute(sql)
                print("cursor.description: ", cursor.description)
                row = cursor.fetchall()
                return row
        except:
            connection.close()
