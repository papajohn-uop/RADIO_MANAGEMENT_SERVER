# coding: utf-8

from typing import Dict, List  # noqa: F401

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
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from openapi_server.models.error import Error
from openapi_server.models.event_subscription import EventSubscription
from openapi_server.models.resource_attribute_value_change_event import ResourceAttributeValueChangeEvent
from openapi_server.models.resource_create_event import ResourceCreateEvent
from openapi_server.models.resource_delete_event import ResourceDeleteEvent
from openapi_server.models.resource_state_change_event import ResourceStateChangeEvent


router = APIRouter()


@router.post(
    "/listener/resourceAttributeValueChangeEvent",
    responses={
        201: {"model": EventSubscription, "description": "Notified"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        405: {"model": Error, "description": "Method Not allowed"},
        409: {"model": Error, "description": "Conflict"},
        500: {"model": Error, "description": "Internal Server Error"},
    },
    tags=["notification listeners (client side)"],
    summary="Client listener for entity ResourceAttributeValueChangeEvent",
)
async def listen_to_resource_attribute_value_change_event(
    data: ResourceAttributeValueChangeEvent = Body(None, description="The event data"),
) -> EventSubscription:
    """Example of a client listener for receiving the notification ResourceAttributeValueChangeEvent"""
    ...


@router.post(
    "/listener/resourceCreateEvent",
    responses={
        201: {"model": EventSubscription, "description": "Notified"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        405: {"model": Error, "description": "Method Not allowed"},
        409: {"model": Error, "description": "Conflict"},
        500: {"model": Error, "description": "Internal Server Error"},
    },
    tags=["notification listeners (client side)"],
    summary="Client listener for entity ResourceCreateEvent",
)
async def listen_to_resource_create_event(
    data: ResourceCreateEvent = Body(None, description="The event data"),
) -> EventSubscription:
    """Example of a client listener for receiving the notification ResourceCreateEvent"""
    ...


@router.post(
    "/listener/resourceDeleteEvent",
    responses={
        201: {"model": EventSubscription, "description": "Notified"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        405: {"model": Error, "description": "Method Not allowed"},
        409: {"model": Error, "description": "Conflict"},
        500: {"model": Error, "description": "Internal Server Error"},
    },
    tags=["notification listeners (client side)"],
    summary="Client listener for entity ResourceDeleteEvent",
)
async def listen_to_resource_delete_event(
    data: ResourceDeleteEvent = Body(None, description="The event data"),
) -> EventSubscription:
    """Example of a client listener for receiving the notification ResourceDeleteEvent"""
    ...


@router.post(
    "/listener/resourceStateChangeEvent",
    responses={
        201: {"model": EventSubscription, "description": "Notified"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        405: {"model": Error, "description": "Method Not allowed"},
        409: {"model": Error, "description": "Conflict"},
        500: {"model": Error, "description": "Internal Server Error"},
    },
    tags=["notification listeners (client side)"],
    summary="Client listener for entity ResourceStateChangeEvent",
)
async def listen_to_resource_state_change_event(
    data: ResourceStateChangeEvent = Body(None, description="The event data"),
) -> EventSubscription:
    """Example of a client listener for receiving the notification ResourceStateChangeEvent"""
    ...
