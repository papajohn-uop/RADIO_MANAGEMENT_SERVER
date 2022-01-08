from os import error
from typing import List
import json

from pydantic.typing import new_type_supertype

import pymongo
from pymongo.errors import ConnectionFailure

from pprint import pprint

from openapi_server.models.resource import Resource
from openapi_server.models.resource import Characteristic

print("MONGO_DB")
def connect():

#    client = pymongo.MongoClient('r00tusEwrlocalhost', port=32017)

    mongo_conn=None
    #USer name and password hardcoded here is not that smart
    #TODO: Move it in a conf dile
    userName="r00tusEr"
    userPwd="r00tpAss"
    port=32017
    conn_URI="mongodb://{}:{}@127.0.0.1:{}".format(userName,userPwd,port)
   
    mongo_conn = pymongo.MongoClient(conn_URI)
    try: 
       mongo_conn.admin.command('ping')
    except Exception as e: 
        print(e)
    finally:
        print("You are connected!")
        if mongo_conn is not None:
            return mongo_conn

    return None
  



def insert_resource(newResource:Resource):
    print("MONGO_DB_INSERT")
    TARGET_DB="RMS"
    TARGET_COLLECTION="gNodeBs"
    ret_list = list() #[success = True, UpdatedRecordList] / [success = False, error message]
    success = True
    message = ""
    return_code=200
    error_msg=''

    print("****************************")
    conn=connect()

    if TARGET_DB in conn.list_database_names():
        print("RMS DB is OK!")
    else:
        print("RMS DB is Missing!")
        success = False
        message = "Error DBM."
    print(conn[TARGET_DB].list_collection_names())
    if TARGET_COLLECTION in conn[TARGET_DB].list_collection_names():
        print("COLLECTION in DB is OK!")
    else:
        print("COLLECTION in DB is Missing!")
        success = False
        message = "Error CDBM."

    target_db=conn[TARGET_DB]
    target_collection=target_db[TARGET_COLLECTION]

    #TODO: Check if entry already exists
    gnodeb_exists = target_collection.count({'_id': newResource.name})
    print (gnodeb_exists)
    #Time to write
    if  gnodeb_exists != 0:
        print("OOOOPs")
        success = False
        return_code=409 #conflict
        error_msg="Resource already exists"
    if success is True:
        try:
            my_entry = { "_id":newResource.name,"resource": newResource.dict() }
            target_collection.insert_one(my_entry)
        except error as err:
            print(err)
            print("Error Code:", err.errno)
            print("Message", err.msg)
            success = False
            message = "Error Code: " + str(err.errno) + " | Message: " + err.msg
    #TODO: MAke this list a dict
    ret_list.append(success)
    ret_list.append(message)
    ret_list.append(return_code)
    ret_list.append(error_msg)
    return ret_list
