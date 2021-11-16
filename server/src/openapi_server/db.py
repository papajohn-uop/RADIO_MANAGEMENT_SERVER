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
        conn =mysql.connector.connect(host='rc_mysql_cont',
        #conn =mysql.connector.connect(host='127.0.0.1',
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


    ret_list = list() #[success = True, UpdatedRecordList] / [success = False, error message]
    success = True
    message = ""

    print("****************************")
    conn=connect()
    #TODO: try...catch
    if conn.is_connected():
        print('Connection established.')
        cursor = conn.cursor()
        insert_command="INSERT INTO  amari_radios (UUID, name, description, resourceVersion, resource_characteristic) VALUES (\"{}\",\"{}\",\"{}\",\"{}\",\"{}\")".format(newResource.id,newResource.name, newResource.description,newResource.resource_version, newResource.dict())
        print(insert_command)
        
        try:
            cursor.execute(insert_command)
            conn.commit()
            conn.close()
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("Message", err.msg)
            success = False
            message = "Error Code: " + str(err.errno) + " | Message: " + err.msg
        
        ret_list.append(success)
        ret_list.append(message)
        return ret_list


def get_resource(id=None):
    ret_list = list() #[success = True, UpdatedRecordList] / [success = False, error message]
    resources_list=list()
    success = True
    
    conn=connect()

    if conn.is_connected():
        print('Connection established.')
        cursor = conn.cursor()
        if id is None:
            get_command="SELECT * FROM amari_radios"
        else:
            #https://stackoverflow.com/questions/51876317/mysql-query-compare-string-with-int-value
            get_command="SELECT * FROM amari_radios where CAST(id as char(255))='"+str(id) + "' or UUID='"+str(id) +"'"
        try:
            print(get_command)
            cursor.execute(get_command)  
            rows = cursor.fetchall()
            

            print('Total Row(s):', cursor.rowcount)
            for row in rows:
                
                print("row[5]")
                print(row[5])
                newResource=Resource(id=row[0],href=row[1])


                mmm=str(row[5]).replace("\'","\"").replace("None","\"None\"")
                # mmm=str(row[5]).replace("\'None\'","None").replace("\'","\"").replace("None","\"None\"")
                
                print("mmm")
                print(mmm)
            
                res_as_jsn=json.loads(mmm)
                newResource.category=res_as_jsn["category"]
                newResource.name=res_as_jsn["name"]
                newResource.description=res_as_jsn["description"]
                newResource.resource_version=res_as_jsn["resource_version"]

                newResource.resource_characteristic=res_as_jsn["resource_characteristic"]
                resources_list.append(newResource)
                print("New resource")
                print(newResource)
            else:
                print('No more data.')

        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("Message", err.msg)
            success = False
            resources_list = "Error Code: " + str(err.errno) + " | Message: " + err.msg

        ret_list.append(success)
        ret_list.append(resources_list)
        return ret_list
       
           


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

        delete_command="DELETE FROM amari_radios where CAST(id as char(255))='"+str(id) + "' or UUID='"+str(id) +"'"

        print(delete_command)
        cursor.execute(delete_command)
        conn.commit()
        conn.close()
# END_INS_TZANIS   

# INS_TZANIS

# UPDATE amari_radios SET name = 'AMARI' WHERE id = 32;

def patch_resource(id:str, resource:Resource, storedResource:Resource):
    print("****************************")
    print("patch resource with id "+str(id))
    print("****************************")

    return_res_list=list() #[success = True, UpdatedRecord] / [success = False, error message]
    success = False
    return_result = ""
    
    UpdatedRecord = UpdateRecord (resource, storedResource)
    
    conn=connect()
    #TODO: try...catch
    if conn.is_connected():
        print('Connection established.')
        cursor = conn.cursor()
        print("resourceVersion")
        print(resource.resource_version)
        print(type(resource.resource_version))
        patch_command="UPDATE amari_radios SET name = \"{}\", description = \"{}\", resourceVersion = \"{}\", resource_characteristic = \"{}\" WHERE id = \"{}\";".format(resource.name, resource.description, resource.resource_version, resource.dict(), id)
        # patch_command="UPDATE amari_radios SET name = \"{}\", description = \"{}\", resourceVersion = \"{}\", resource_characteristic = \"{}\" WHERE id = \"{}\";".format(resource.name, resource.description, resource.resource_version, resource.dict(), id)
        print(patch_command)
        try:

            cursor.execute(patch_command)
            success = True
            return_result = UpdatedRecord
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("Message", err.msg)
            success = False
            return_result = err.msg


        conn.commit()
        conn.close()

    print("DB patch complete")
    return_res_list.append(success)
    return_res_list.append(return_result)
    return return_res_list



def UpdateRecord(NewResource:Resource, StoredResource:Resource):
    print("*******New Resource*******")
    print(NewResource)
    print("*******Stored Resource*******")
    print(StoredResource)
    # print("*******New Resource name*******")
    # print(NewResource.name)
    print("*******Stored Resource name*******")
    print(StoredResource.name)
    print(type(StoredResource.name))

    
    #TODO blows up whne stored value is 'None'
    # if NewResource.name == None: 
    #     print("*******New Resource name is  None*******")
    #     if StoredResource.name != None: 
    #         print("*******Stored Resource name is not None*******")
    #         NewResource.name = StoredResource.name

    if NewResource.name == None:
        if StoredResource.name != "None": NewResource.name = StoredResource.name      
        else: NewResource.name = None

    
    if NewResource.description == None:
        if StoredResource.description != "None": NewResource.description = StoredResource.description
        else: NewResource.description = None
    
    if NewResource.category == None:
        if StoredResource.category != "None": NewResource.category = StoredResource.category
        else: NewResource.category = None

    if NewResource.resource_version == None:
        if StoredResource.resource_version != "None": NewResource.resource_version = StoredResource.resource_version        
        else: NewResource.resource_version = None
    


    print("Update resource_characteristic")
    for stored_char in StoredResource.resource_characteristic:
        print("stored_char.name is: " + stored_char["name"])
        stored_char_found = False
        for new_char in NewResource.resource_characteristic:
            print("new_char.name is: " + new_char.name)
            if new_char.name == stored_char["name"]:
                print("characteristic found: " + new_char.name)
                stored_char_found = True
        if stored_char_found == False:
            print("Not found")
            char = Characteristic (name = stored_char["name"], value = stored_char["value"])
            char.id = stored_char["id"]
            # char.name = stored_char["name"]
            # char.value = stored_char["value"]
            char.value_type = stored_char["value_type"]
            NewResource.resource_characteristic.append(char)   

    print("Update Function NewResource")
    print(NewResource)
    
    return NewResource

# END_INS_TZANIS   

