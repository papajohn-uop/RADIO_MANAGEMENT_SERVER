from os import error
from typing import List
import json

from pydantic.typing import new_type_supertype

import pymongo
from pymongo.errors import ConnectionFailure

from pprint import pprint

from openapi_server.models.resource import Resource
from openapi_server.models.resource_update import ResourceUpdate
from openapi_server.models.resource import Characteristic


from openapi_server.models.resource_administrative_state_type import ResourceAdministrativeStateTypeEnum
from openapi_server.models.resource_operational_state_type import ResourceOperationalStateTypeEnum
from openapi_server.models.resource_status_type import ResourceStatusTypeEnum
from openapi_server.models.resource_usage_state_type import ResourceUsageStateTypeEnum

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

def checkConnection():
    TARGET_DB="RMS"
    TARGET_COLLECTION="gNodeBs"


    print("****************************")
    conn=connect()

    if TARGET_DB in conn.list_database_names():
        print("RMS DB is OK!")
    else:
        print("RMS DB is Missing!")
        success = False
        message = "Error DBM."
        return None
    print(conn[TARGET_DB].list_collection_names())
    if TARGET_COLLECTION in conn[TARGET_DB].list_collection_names():
        print("COLLECTION in DB is OK!")
    else:
        print("COLLECTION in DB is Missing!")
        success = False
        message = "Error CDBM."
        return None
    return conn


def get_resource(id=None):
    print("MONGO_DB_GET")
    TARGET_DB="RMS"
    TARGET_COLLECTION="gNodeBs"
    ret_list = list() #[success = True, UpdatedRecordList] / [success = False, error message]
    resources_list=list()
    success = True
    
    conn=checkConnection()

    if conn:
        target_db=conn[TARGET_DB]
        target_collection=target_db[TARGET_COLLECTION]
        resourcesCursor=None
        #TODO: add try/catch
        if id is None:
            resourcesCursor = target_collection.find()
        else:
            resourcesCursor = target_collection.find_one({"_id":id})
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        # for document in resourcesCursor:
        #     print(document)
        # print(resourcesCursor)
        # print(type(resourcesCursor))

    ret_list.append(success)
    ret_list.append(resourcesCursor)
    return ret_list
    



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

def patch_resource(id:str, patch_resource:ResourceUpdate):
    print("MONGO_DB_PATCH")
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
    if success is True:
        try:
            print("PAPA2")
            #only allow certain fields to be patched
            print(patch_resource.dict())
            for key, value in patch_resource.dict().items():
                if value:
                    print (key, value)
                    print (value)
                    print(ResourceOperationalStateTypeEnum.enable.value)
                    print(ResourceOperationalStateTypeEnum["enable"].value)
                    print(ResourceOperationalStateTypeEnum.enable)
                    print(ResourceOperationalStateTypeEnum["enable"])

                    tar="resource."+key
                    print(tar)
                    print(ResourceOperationalStateTypeEnum[value.value].value)
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

                    target_collection.update_one({'_id': id},{"$set": {tar:ResourceOperationalStateTypeEnum[value.value].value}}, upsert=False)
            
           # my_entry = { "_id":newResource.name,"resource": newResource.dict() }
            #target_collection.replace_one({'_id': id},{'_id': id,"resource": patch_resource.dict()}, upsert=True)
            #target_collection.replace_one({'_id': id},{"DFDFD":"dfdf"}, upsert=True)
            print("PAPA3")
        except error as err:
            print("PAPA3.4")
            print(err)
            print("Error Code:", err.errno)
            print("Message", err.msg)
            success = False
            message = "Error Code: " + str(err.errno) + " | Message: " + err.msg
    #TODO: MAke this list a dict
    print(success)
    ret_list.append(success)
    ret_list.append(message)
    ret_list.append(return_code)
    ret_list.append(error_msg)
    return ret_list
    return
    print("PAPA1")
    if success is True:
        try:
            print("PAPA2")
            print(patch_resource.dict())
           # my_entry = { "_id":newResource.name,"resource": newResource.dict() }
            target_collection.replace_one({'_id': id},{'_id': id,"resource": patch_resource.dict()}, upsert=True)
            #target_collection.replace_one({'_id': id},{"DFDFD":"dfdf"}, upsert=True)
            print("PAPA3")
        except error as err:
            print("PAPA3.4")
            print(err)
            print("Error Code:", err.errno)
            print("Message", err.msg)
            success = False
            message = "Error Code: " + str(err.errno) + " | Message: " + err.msg
    #TODO: MAke this list a dict
    print(success)
    ret_list.append(success)
    ret_list.append(message)
    ret_list.append(return_code)
    ret_list.append(error_msg)
    return ret_list