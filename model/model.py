from db.connect_db import connection
from flask import render_template

class Model():
    @classmethod
    def listRoom(self):
        try:
            with connection.cursor() as cursor:
                # SQL
                sql = "SELECT * FROM room"
                # Execute query.
                cursor.execute(sql)
                print("cursor.description: ", cursor.description)
                print()
                for row in cursor:
                    print(row)
        finally:
            # Close connection.
            connection.close()
        return row

