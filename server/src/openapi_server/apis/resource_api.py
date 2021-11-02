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
from openapi_server import db
from fastapi import BackgroundTasks
from fastapi.responses import JSONResponse

router = APIRouter()


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
    newResource=Resource(id=str(uuid.uuid1()),href="")
    newResource.category=resource.category
    newResource.name=resource.name
    newResource.description=resource.description
    newResource.resource_version=resource.resource_version
    # print("**************************************************")
    # newResource.resource_characteristic=list()
    # for characteristic in resource.resource_characteristic:
    #     print(characteristic.json())
    #     newResource.resource_characteristic.append(characteristic.json())
    # print("**************************************************")
    # print(newResource.resource_characteristic)
    # print("**************************************************")
    
    newResource.resource_characteristic=resource.resource_characteristic
    for characteristic in newResource.resource_characteristic:
        characteristic.id=str(uuid.uuid1())
        print(characteristic)
    print(newResource)
    #TODO: Check for success/fail of command
    insert_result = db.insert_resource(newResource)
    print("**************************")
    print(resource)
    print("**************************")
    print(newResource.dict())
    print(type(resource))
    print(type(resource.resource_characteristic))
    print(resource)
    print("**************************")
    print("**************************")

    if insert_result[0] == True: #success
        return newResource
    else:
        return JSONResponse(status_code=500, content={"code": "500", "reason":"Internal Server Error", "message": insert_result[1], "status":"", "reference_error":"", "base_type":"","schema_location":"", "type":""})


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
    tmp_res=db.get_resource()

    success = tmp_res[0]
    

    if success == False:
        message = tmp_res[1]
        return JSONResponse(status_code=500, content={"code": "500", "reason":"Internal Server Error", "message": message, "status":"", "reference_error":"", "base_type":"","schema_location":"", "type":""})
    
    return tmp_res[1]
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
    print("This operation updates partially a Resource entity and forwards PATCH actions")


    print("Retrieve stored resource from the DB")
    StoredResourceList = db.get_resource(id)
    
    print("Check if resource with this id is storded in the database")
    if StoredResourceList[0] == False:
        return JSONResponse(status_code=500, content={"code": "500", "reason":"Internal Server Error", "message": StoredResourceList[1], "status":"", "reference_error":"", "base_type":"","schema_location":"", "type":""})
    if not StoredResourceList[1]:
        print("Record not found. Use POST to insert new record")
        return JSONResponse(status_code=200, content={"code": "200", "reason":"", "message": "Record not found. Use POST to insert new record", "status":"", "reference_error":"", "base_type":"","schema_location":"", "type":""})
        
        
    print("record with id is stored in the database. Perform PATCH action")
    # print(StoredResourceList[1][0])

    patch_resource = db.patch_resource(id, resource, StoredResourceList[1][0])
    if patch_resource[0] == False:
        return JSONResponse(status_code=500, content={"code": "500", "reason":"Internal Server Error", "message": patch_resource[1], "status":"", "reference_error":"", "base_type":"","schema_location":"", "type":""})
    else:       
        UpdatedResource:Resource= db.get_resource(id)[1][0]
        print("Resource successfully updated in the DB")
        
    # print(UpdatedResource)

    print("Check if action included")
    IP =""
    action_included = False
    for characteristic in UpdatedResource.resource_characteristic:
        if characteristic["name"] == "action":
            print("ACTION field found")
            action_included = True
        if characteristic["name"] == "IP":
            IP = characteristic["value"]["value"]
            print(IP)


    # NewResource:ResourceResource= db.get_resource(id)[0]
    if not action_included:
        print("No action included. PATCH action completed")
        return UpdatedResource
      

    # ACTION found. Perform PATCH request
    print("Perform PATCH request")
    
    try:
        x = requests.patch("http://" + IP +"/resource/1", json=dict(UpdatedResource), timeout=2)
        print(x.status_code)
        print("PATCH request complete")
    except requests.exceptions.RequestException as e:
        return JSONResponse(status_code=500, content={"code": "500", "reason":"Internal Server Error", "message": "Connection Timeout", "status":"", "reference_error":"", "base_type":"","schema_location":"", "type":""})

    
    print(UpdatedResource)
    return UpdatedResource

    
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
    #Atm for easier debug we use the ID field of the DB
    #When moving on production we should switch to UUID.
    #Nothing will change here, the change is in the db module
    tmp_res=db.get_resource(id)

    success = tmp_res[0]  

    if success == False:
        message = tmp_res[1]
        return JSONResponse(status_code=500, content={"code": "500", "reason":"Internal Server Error", "message": message, "status":"", "reference_error":"", "base_type":"","schema_location":"", "type":""})

    if not tmp_res[1]:
        print("Record not found. Use POST to insert new record")
        return JSONResponse(status_code=200, content={"code": "200", "reason":"", "message": "Record not found. Use POST to insert new record", "status":"", "reference_error":"", "base_type":"","schema_location":"", "type":""})

    return tmp_res[1][0]