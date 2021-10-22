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
        #conn =mysql.connector.connect(host='rc_mysql_cont',
        conn =mysql.connector.connect(host='127.0.0.1',
                                       database='radio_config',
                                       user='user',
                                       password='password')
    except Error as error:
        print(error)

    finally:
        if conn is not None and conn.is_connected():
            #conn.close()
            #print('Connection closed.')
            return conn




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
        insert_command="INSERT INTO  amari_radios (UUID, name, description, resourceVersion, resource_characteristic) VALUES (\"{}\",\"{}\",\"{}\",\"{}\",\"{}\")".format(newResource.id,newResource.name, newResource.description,newResource.resource_version, newResource.dict())
        print(insert_command)
        cursor.execute(insert_command)
        conn.commit()
        conn.close()


def get_resource(id=None):
    conn=connect()

    if conn.is_connected():
        print('Connection established.')
        cursor = conn.cursor()
        if id is None:
            get_command="SELECT * FROM amari_radios"
        else:
            get_command="SELECT * FROM amari_radios where id="+str(id)
        cursor.execute(get_command)
        
        rows = cursor.fetchall()
        return_res_list=list()

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
            return_res_list.append(newResource)
#            return newResource
        else:
            print('No more data.')
        return return_res_list


# INS_TZANIS
def delete_resource(id=None):
    print("****************************")
    print("delete resource with id"+str(id))
    print("****************************")
    conn=connect()
    #TODO: try...catch
    if conn.is_connected():
        print('Connection established.')
        cursor = conn.cursor()

        delete_command="DELETE FROM amari_radios where id="+str(id)

        print(delete_command)
        cursor.execute(delete_command)
        conn.commit()
        conn.close()
# END_INS_TZANIS   

# INS_TZANIS

# UPDATE amari_radios SET name = 'AMARI' WHERE id = 32;

def patch_resource(id:str, resource:Resource):
    print("****************************")
    print("patch resource with id "+str(id))
    print("****************************")

    return_res_list=list()
    success = False
    return_message = ""

    conn=connect()
    #TODO: try...catch
    if conn.is_connected():
        print('Connection established.')
        cursor = conn.cursor()
        search_command="SELECT COUNT(*) FROM amari_radios WHERE id = \"{}\"".format(id)
        print(search_command)
        cursor.execute(search_command)
        rows = cursor.fetchone()
        print(rows[0])
        print("***********END*************")

        if rows[0] == 1:
            print("Record found. Update record")

            patch_command="UPDATE amari_radios SET name = \"{}\", description = \"{}\", resourceVersion = \"{}\", resource_characteristic = \"{}\" WHERE id = \"{}\";".format(resource.name, resource.description, resource.resource_version, resource.dict(), id)
            try:

                cursor.execute(patch_command)
                success = True
                return_message = "Record Successfully Updated"
            except mysql.connector.Error as err:
                print(err)
                print("Error Code:", err.errno)
                print("Message", err.msg)
                success = False
                return_message = err.msg

        else:
            print("Record not found. Use POST to insert new record")
            return_message = "Record not found. Use POST to insert new record"



        conn.commit()
        conn.close()
        return_res_list.append(success)
        return_res_list.append(return_message)
        return return_res_list
        
# END_INS_TZANIS   

