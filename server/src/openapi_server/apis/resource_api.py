# coding: utf-8

from typing import Dict, List

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
    HTTPException,
    
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from openapi_server.models.error import Error
from openapi_server.models.resource import Resource
from openapi_server.models.resource_create import ResourceCreate
from openapi_server.models.resource_update import ResourceUpdate

import uuid
import requests
#from openapi_server import db
from openapi_server import mongo_db


from fastapi import BackgroundTasks
from fastapi.responses import JSONResponse

from . import ws

router = APIRouter()

from openapi_server.models.resource_administrative_state_type import ResourceAdministrativeStateTypeEnum
from openapi_server.models.resource_operational_state_type import ResourceOperationalStateTypeEnum
from openapi_server.models.resource_status_type import ResourceStatusTypeEnum
from openapi_server.models.resource_usage_state_type import ResourceUsageStateTypeEnum

from openapi_server.models.characteristic import Characteristic

from datetime import datetime




@router.post(
    "/resource",
    responses={
        201: {"model": Resource, "description": "Created"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        405: {"model": Error, "description": "Method Not allowed"},
        409: {"model": Error, "description": "Conflict"},
        500: {"model": Error, "description": "Internal Server Error"},
    },
    tags=["resource"],
    summary="Creates a Resource",
)
async def create_resource(
    resource: ResourceCreate = Body(None, description="The Resource to be created"),
) -> Resource:
    """This operation creates a Resource entity."""
    ...
    #TODO: Check for each member value (if exists)
    #newResource=Resource(id=str(uuid.uuid1()),href="")
    newResource=Resource(id=str(resource.name),href="")
    newResource.category=resource.category
    newResource.name=resource.name
    newResource.description=resource.description
    newResource.resource_version=resource.resource_version
    #TODO: if the key is erroneous in agetn_Cfg (i.e. state=unlked) there is an excpetion. Must fix it
    if (resource.administrative_state):
        newResource.administrative_state=ResourceAdministrativeStateTypeEnum[resource.administrative_state.value].value
    else:
        newResource.administrative_state=ResourceAdministrativeStateTypeEnum.shutdown.value
    if (resource.operational_state):
        newResource.operational_state=ResourceOperationalStateTypeEnum[resource.operational_state.value].value#resource.administrative_state
    else:
        newResource.operational_state=ResourceOperationalStateTypeEnum.disable.value
    if (newResource.resource_status):
        newResource.resource_status=ResourceStatusTypeEnum[resource.resource_status.value].value#resource.administrative_state
    else:
        newResource.resource_status=ResourceStatusTypeEnum.unknown.value
    if (newResource.usage_state):
        newResource.usage_state=ResourceUsageStateTypeEnum[resource.usage_state.value].value#resource.administrative_state
    else:
        newResource.usage_state=ResourceUsageStateTypeEnum.idle.value

    newResource.resource_characteristic=resource.resource_characteristic
    for characteristic in newResource.resource_characteristic:
        characteristic.id=str(uuid.uuid1())
        print(characteristic)
    print(newResource)
    print("Lets start mongo")
    #If all Ok insert resource
    insert_result=mongo_db.insert_resource(newResource)
    #insert_result = db.insert_resource(newResource)
    
    if insert_result[0] == True: #success
 #       return newResource
        return JSONResponse(status_code=201, content=newResource.dict())
    else:
        #TODO: At the moment all fialures are retunre as 500
        #This is propably wrong, Need to check tha failure and add the 
        # correct error codes depending on the situation
        error_resp=Error(code= insert_result[2], reason=insert_result[3])
        return JSONResponse(status_code=insert_result[2], content=error_resp.dict())
      #  return JSONResponse(status_code=insert_result[2], content={"code": insert_result[2], "reason":insert_result[3], "message": "", "status":"", "reference_error":"", "base_type":"","schema_location":"", "type":""})
     #   return JSONResponse(status_code=500, content={"code": "500", "reason":"Internal Server Error", "message": insert_result[1], "status":"", "reference_error":"", "base_type":"","schema_location":"", "type":""})


@router.delete(
    "/resource/{id}",
    responses={
        204: {"description": "Deleted"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        405: {"model": Error, "description": "Method Not allowed"},
        409: {"model": Error, "description": "Conflict"},
        500: {"model": Error, "description": "Internal Server Error"},
    },
    tags=["resource"],
    summary="Deletes a Resource",
)
async def delete_resource(
    id: str = Path(None, description="Identifier of the Resource"),
) -> None:
    """This operation deletes a Resource entity."""
# INS_TZANIS
    ...
    db.delete_resource(id)
# END_INS_TZANIS

@router.get(
    "/resource",
    responses={
        200: {"model": List[Resource], "description": "Success"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        405: {"model": Error, "description": "Method Not allowed"},
        409: {"model": Error, "description": "Conflict"},
        500: {"model": Error, "description": "Internal Server Error"},
    },
    tags=["resource"],
    summary="List or find Resource objects",
)
async def list_resource(
    fields: str = Query(None, description="Comma-separated properties to be provided in response"),
    offset: int = Query(None, description="Requested index for start of resources to be provided in response"),
    limit: int = Query(None, description="Requested number of resources to be provided in response"),
) -> List[Resource]:
    print("GET")
    """This operation list or find Resource entities"""
    res_list=list()

    print("Retrieve stored resources from the MONGO DB")
    StoredResourceList = mongo_db.get_resource()
    
    #tmp_res=db.get_resource()

    success = StoredResourceList[0]
     
    if success == False:
        message = StoredResourceList[1]
        return JSONResponse(status_code=500, content={"code": "500", "reason":"Internal Server Error", "message": message, "status":"", "reference_error":"", "base_type":"","schema_location":"", "type":""})
    
    return StoredResourceList[1]
    ...


@router.patch(
    "/resource/{id}",
    responses={
        200: {"model": Resource, "description": "Updated"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        405: {"model": Error, "description": "Method Not allowed"},
        409: {"model": Error, "description": "Conflict"},
        500: {"model": Error, "description": "Internal Server Error"},
    },
    tags=["resource"],
    summary="Updates partially a Resource",
)
async def patch_resource(
    id: str = Path(None, description="Identifier of the Resource"),
    resource: ResourceUpdate = Body(None, description="The Resource to be updated"),
) -> Resource:
    """This operation updates partially a Resource entity."""
    ...
    print("Tshis operation updates partially 111a Resource entity and forwards PATCH actions")

    print("Retrieve stored resource from the MONGO DB")
    StoredResourceList = mongo_db.get_resource(id)
    #TODO: Check if not found
    target_res=StoredResourceList[1][0]
    if not target_res:
        print("PATCH COMMAND. Record not found. Use POST to insert new record")
        return JSONResponse(status_code=200, content={"code": "200", "reason":"", "message": "Record not found. Use POST to insert new record", "status":"", "reference_error":"", "base_type":"","schema_location":"", "type":""})


    print("Check if action included")
    IP =""
    action_included = False
    soft_action_included=False
    
    #check if activation_feature is present
    #Init variable to avoid exception
    soft_action_included=None
    if "activation_feature" in resource.dict():
        if resource.dict()["activation_feature"]:
            for characteristic in resource.dict()["activation_feature"][0]["feature_characteristic"]:
                if characteristic["name"] == "action":
                    action_included = True
                if characteristic["name"] == "soft_action":
                    print("Lets do something with ws")
                    soft_action_included = True

            if action_included:
                for characteristic in (target_res["resource_characteristic"]):
                    if characteristic["name"] == "IP":
                        IP = characteristic["value"]["value"]
                        print(IP)
            if soft_action_included:
                for characteristic in (target_res["resource_characteristic"]):
                    if characteristic["name"] == "IP":
                        IP = characteristic["value"]["value"]
                        print(IP)
                    if characteristic["name"] == "gtp_iface":
                        GTP_ADDR = characteristic["value"]["value"]
                        print(GTP_ADDR)

    patch_result=None    

    if soft_action_included:
        now = datetime.now() 
        current_time = now.strftime("%H:%M:%S")
        ft_timestamp=Characteristic(name="timestamp",value={"value":current_time})
        resource.activation_feature[0].feature_characteristic.append(ft_timestamp)
        #IP has the fastapi server of the agent as well.
        #Just get the IP part only
        ws_IP=IP.split(":")[0]
        resp=ws.ws_command(ws_IP, GTP_ADDR, resource)
        ft_resp=Characteristic(name="ws_response",value={"value":resp})
        resource.activation_feature[0].feature_characteristic.append(ft_resp)
        
    if action_included:
        ...
        #send patch to agent
        #TODO: check operational state
         # ACTION found. Perform PATCH request
        print("Perform PATCH ACTION request")
        
        try:
            x = requests.patch("http://" + IP +"/resource/1", json=resource.dict(), timeout=10)
            print(x.status_code)
            print(x.text)
            print("PATCH request complete")
            
            now = datetime.now() 
            current_time = now.strftime("%H:%M:%S")
            print(current_time)
            #add timestamp
           # print(resource.dict()["activation_feature"][0]["feature_characteristic"][0]["value"])
            ft_timestamp=Characteristic(name="patch_result",value={"timestamp":current_time,"html_code":x.status_code,"html_text":x.text})
            resource.activation_feature[0].feature_characteristic.append(ft_timestamp)
            # print(ft_timestamp)
            # print(resource.activation_feature[0].feature_characteristic)

            # if x.status_code==200:
            #     return JSONResponse(status_code=200, content={"code": "200", "reason":"", "message": "Patch send succesfully to Radio", "status":"OK", "reference_error":"", "base_type":"","schema_location":"", "type":""})
            # else:
            #     return JSONResponse(status_code=405, content={"code": "405", "reason":"", "message": "Patch send to Radio FAILED", "status":"FAIL", "reference_error":"", "base_type":"","schema_location":"", "type":""})

            # return x
        except requests.exceptions.RequestException as e:
            print(repr(e))
            return JSONResponse(status_code=504, content={"code": "504", "reason":"Bad Gateway", "message": "Connection Timeout", "status":"", "reference_error":"", "base_type":"","schema_location":"", "type":""})
   # else:
    patch_result=mongo_db.patch_resource(id,resource)


    StoredResourceList = mongo_db.get_resource(id)
   
    target_res=StoredResourceList[1][0]

    success = StoredResourceList[0]  

    if success == False:
        message = StoredResourceList[1]
        return JSONResponse(status_code=500, content={"code": "500", "reason":"Internal Server Error", "message": message, "status":"", "reference_error":"", "base_type":"","schema_location":"", "type":""})

    if not StoredResourceList[1]:
        print("Record not found. Use POST to insert new record")
        return JSONResponse(status_code=200, content={"code": "200", "reason":"", "message": "Record not found. Use POST to insert new record", "status":"", "reference_error":"", "base_type":"","schema_location":"", "type":""})
    print("=--------------------->2")
    return target_res


    
@router.get(
    "/resource/{id}",
    responses={
        200: {"model": Resource, "description": "Success"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        405: {"model": Error, "description": "Method Not allowed"},
        409: {"model": Error, "description": "Conflict"},
        500: {"model": Error, "description": "Internal Server Error"},
    },
    tags=["resource"],
    summary="Retrieves a Resource by ID",
)
async def retrieve_resource(
    id: str = Path(None, description="Identifier of the Resource"),
    fields: str = Query(None, description="Comma-separated properties to provide in response"),
) -> Resource:
    """This operation retrieves a Resource entity. Attribute selection is enabled for all first level attributes."""
    ...
    print("Retrieve stored resource from the MONGO DB")
    StoredResourceList = mongo_db.get_resource(id)
   


    success = StoredResourceList[0]  

    if success == False:
        message = StoredResourceList[1]
        return JSONResponse(status_code=500, content={"code": "500", "reason":"Internal Server Error", "message": message, "status":"", "reference_error":"", "base_type":"","schema_location":"", "type":""})

    if not StoredResourceList[1]:
        print("Record not found. Use POST to insert new record")
        return JSONResponse(status_code=200, content={"code": "200", "reason":"", "message": "Record not found. Use POST to insert new record", "status":"", "reference_error":"", "base_type":"","schema_location":"", "type":""})

    return StoredResourceList[1][0]
