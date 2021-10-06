# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from openapi_server.models.resource_attribute_value_change_event_payload import ResourceAttributeValueChangeEventPayload


class ResourceAttributeValueChangeEvent(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ResourceAttributeValueChangeEvent - a model defined in OpenAPI

        event_id: The event_id of this ResourceAttributeValueChangeEvent [Optional].
        event_time: The event_time of this ResourceAttributeValueChangeEvent [Optional].
        event_type: The event_type of this ResourceAttributeValueChangeEvent [Optional].
        correlation_id: The correlation_id of this ResourceAttributeValueChangeEvent [Optional].
        domain: The domain of this ResourceAttributeValueChangeEvent [Optional].
        title: The title of this ResourceAttributeValueChangeEvent [Optional].
        description: The description of this ResourceAttributeValueChangeEvent [Optional].
        priority: The priority of this ResourceAttributeValueChangeEvent [Optional].
        time_ocurred: The time_ocurred of this ResourceAttributeValueChangeEvent [Optional].
        field_path: The field_path of this ResourceAttributeValueChangeEvent [Optional].
        event: The event of this ResourceAttributeValueChangeEvent [Optional].
    """

    event_id: Optional[str] = None
    event_time: Optional[datetime] = None
    event_type: Optional[str] = None
    correlation_id: Optional[str] = None
    domain: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    time_ocurred: Optional[datetime] = None
    field_path: Optional[str] = None
    event: Optional[ResourceAttributeValueChangeEventPayload] = None

ResourceAttributeValueChangeEvent.update_forward_refs()
