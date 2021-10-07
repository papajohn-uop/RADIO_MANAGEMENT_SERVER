from typing import List
import mysql.connector
from mysql.connector import connect, Error
import json

from pydantic.typing import new_type_supertype


from openapi_server.models.resource import Resource
from openapi_server.models.resource import Characteristic

print("FFFFFFFFFFF")

def connect():
    """ Connect to MySQL database """

    #db_config = read_db_config()
    conn = None
    try:
        print('Connecting to MySQL database...')
#        conn =mysql.connector.connect(host='rc_mysql_cont',
        conn =mysql.connector.connect(host='127.0.0.1',
                                       database='radio_config',
                                       user='user',
                                       password='password')
        '''
        if conn.is_connected():
            print('Connection established.')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM devices")
            rows = cursor.fetchall()
            print('Total Row(s):', cursor.rowcount)
            for row in rows:
                print(row)
            else:
                print('Connection failed.')
        '''
    except Error as error:
        print(error)

    finally:
        if conn is not None and conn.is_connected():
            #conn.close()
            #print('Connection closed.')
            return conn


# def getAllDevices():
#     conn=connect()

#     if conn.is_connected():
#         print('Connection established.')
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM amari_radios")
#         rows = cursor.fetchall()

#         print('Total Row(s):', cursor.rowcount)
#         for row in rows:
#             print(row)
#         else:
#             print('No more data.')
        
#         conn.close()
#         print('Connection closed.')

#         row_headers=[x[0] for x in cursor.description] #this will extract row headers
#         #rv = cur.fetchall()
#         json_data=[]
#         for result in rows:
#             json_data.append(dict(zip(row_headers,result)))
#         return json_data
#         return json.dumps(json_data)

#         return(json.dumps(rows))
#         return rows    


def insert_resource(newResource:Resource):
    print("DB")
    print(newResource)
    print("****************************")
    print( newResource.resource_characteristic)

    print("****************************")
    conn=connect()
    #TODO: try...catch
    if conn.is_connected():
        print('Connection established.')
        cursor = conn.cursor()
       # insert_command="INSERT INTO  amari_radios (UUID, name, description, resourceVersion, resource_characteristic) VALUES (\"{}\",\"{}\",\"{}\",\"{}\",\"{}\")".format(newResource.id,newResource.name, newResource.description,newResource.resource_version, str(newResource.resource_characteristic))
        insert_command="INSERT INTO  amari_radios (UUID, name, description, resourceVersion, resource_characteristic) VALUES (\"{}\",\"{}\",\"{}\",\"{}\",\"{}\")".format(newResource.id,newResource.name, newResource.description,newResource.resource_version, newResource.dict())
      #  insert_command="INSERT INTO  amari_radios (UUID, name, description, resourceVersion, resource_characteristic) VALUES (\"{}\",\"{}\",\"{}\",\"{}\",\"{}\")".format(newResource.id,newResource.name, newResource.description,newResource.resource_version, newResource.dict())
       # insert_command="INSERT INTO  amari_radios (UUID, name, description, resourceVersion, resource_characteristic,placeholder) VALUES (\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\")".format(newResource.id,newResource.name, newResource.description,newResource.resource_version, newResource.dict(),newResource.dict())
       # insert_command="INSERT INTO  amari_radios (UUID, name, description, resourceVersion, resource_characteristic) VALUES (\"{}\",\"{}\",\"{}\",\"{}\",\"{}\")".format(newResource.id,newResource.name, newResource.description,newResource.resource_version, newResource.json())
        print(insert_command)
        cursor.execute(insert_command)
        conn.commit()
        conn.close()


def get_resource(id=None):
    conn=connect()

    if conn.is_connected():
        #return(query_db(conn,"SELECT * FROM devices where id=",(id),False))
        print('Connection established.')
        cursor = conn.cursor()
        if id is None:
            get_command="SELECT * FROM amari_radios"
        else:
            get_command="SELECT * FROM amari_radios where id="+str(id)
        cursor.execute(get_command)
        
        rows = cursor.fetchall()

        print('Total Row(s):', cursor.rowcount)
        for row in rows:
            

            print(row[5])
            newResource=Resource(id=row[0],href="")

            mmm=str(row[5]).replace("\'","\"").replace("None","\"None\"")
           
            res_as_jsn=json.loads(mmm)
            newResource.category=res_as_jsn["category"]
            newResource.name=res_as_jsn["name"]
            newResource.description=res_as_jsn["description"]
            newResource.resource_version=res_as_jsn["resource_version"]

            newResource.resource_characteristic=res_as_jsn["resource_characteristic"]
            return newResource
        else:
            print('No more data.')
        
    
# def getDeviceWithID(id):
#     conn=connect()

#     if conn.is_connected():
#         #return(query_db(conn,"SELECT * FROM devices where id=",(id),False))
#         print('Connection established.')
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM devices where id="+id)
#         rows = cursor.fetchall()

#         print('Total Row(s):', cursor.rowcount)
#         for row in rows:
#             print(row)
#         else:
#             print('No more data.')
        
#         res_json=json.dumps(rows)
#         print("22222222222")
#         print(res_json)
#         print("33333333333333")
#         print(res_json[0])
#         print(res_json[0][0])
#         print("444444444444")
#         for e in rows:
#             print(json.dumps(rows, sort_keys=True, indent=4, separators=(',', ': '), default=str))


#         conn.close()
#         print('Connection closed.')
#         return(json.dumps(rows[0]))
#         #return res_json

#         #return rows

# def getConnectionInfoForDeviceWithID(id):
#     conn=connect()

#     if conn.is_connected():
#         print('Connection established.')
        
#         cursor = conn.cursor()
#         cursor.execute("SELECT connectionInfo FROM devices where id="+id)
#         rows = cursor.fetchall()

#         print('Total Row(s):', cursor.rowcount)
#         for row in rows:
#             print(row)
#         else:
#             print('No more data.')
#         conn.close()
#         if rows:
#             res_json=json.loads(rows[0][0])
#         else:
#             return None

#         return res_json
        
#         return rows

# def getCommandInfoForDeviceWithID(id):
#     conn=connect()

#     if conn.is_connected():
#         print('Connection established.')
        
#         cursor = conn.cursor()
#         cursor.execute("SELECT availableCommands FROM devices where id="+id)
#         rows = cursor.fetchall()

#         print('Total Row(s):', cursor.rowcount)
#         for row in rows:
#             print(row)
#         else:
#             print('No more data.')
#         conn.close()
#         if rows:
#             res_json=json.loads(rows[0][0])
#         else:
#             return None
#         return res_json
        
#         return rows