from db.connect_db import connection
# from flask import render_template
from flask import Flask, request, Response, jsonify, render_template
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
    pass
    def insertData(self, data, table_name):
        try:
            with connection.cursor() as cursor:
                datas = []
                data_value = ''
                count = 0
                datassss = []
                # msg = {}
                sss = ''
                for key in data.keys():
                    count += 1
                    datas.append(key)
                    if count < len(data):
                        addcharset = ','
                    else:
                        addcharset = ''
                    data_value += " ' " + str(data[key]) + " ' " + addcharset
                    datassss.append(str(data[key]))
                    sss += '%s' + addcharset
                feild_insert = ','.join(map(str, datas))
                cursor.execute("INSERT INTO `" + str(table_name) + "` ("+feild_insert+") VALUES ("+sss+")", datassss)
                connection.commit()
                msg = {
                    'status': True,
                    'mess': "Record successfully added"
                }
        except:
            connection.rollback()
            msg = {
                'status': False,
                'mess': "error in insert operation"
            }
        return msg
    def selectData(self, query, table_name):
        cur = connection.cursor()
        cur.execute('SELECT * FROM ' + str(table_name) + ' ' + str(query) +'')
        results = cur.fetchall()
        return results
    def selectOne(self, table_name, pkey, id):
        cur = connection.cursor()
        cur.execute('SELECT * FROM ' + str(table_name) + ' where ' + pkey + ' = ' + str(id) +'')
        results = cur.fetchone()
        return results