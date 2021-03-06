# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from openapi_server.models.resource_state_change_event_payload import ResourceStateChangeEventPayload


class ResourceStateChangeEvent(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ResourceStateChangeEvent - a model defined in OpenAPI

        event: The event of this ResourceStateChangeEvent [Optional].
        event_id: The event_id of this ResourceStateChangeEvent [Optional].
        event_time: The event_time of this ResourceStateChangeEvent [Optional].
        event_type: The event_type of this ResourceStateChangeEvent [Optional].
        correlation_id: The correlation_id of this ResourceStateChangeEvent [Optional].
        domain: The domain of this ResourceStateChangeEvent [Optional].
        title: The title of this ResourceStateChangeEvent [Optional].
        description: The description of this ResourceStateChangeEvent [Optional].
        priority: The priority of this ResourceStateChangeEvent [Optional].
        time_ocurred: The time_ocurred of this ResourceStateChangeEvent [Optional].
    """

    event: Optional[ResourceStateChangeEventPayload] = None
    event_id: Optional[str] = None
    event_time: Optional[datetime] = None
    event_type: Optional[str] = None
    correlation_id: Optional[str] = None
    domain: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    time_ocurred: Optional[datetime] = None

ResourceStateChangeEvent.update_forward_refs()
