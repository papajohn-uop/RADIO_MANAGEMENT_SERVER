# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from openapi_server.models.time_period import TimePeriod


class FeatureRelationship(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    FeatureRelationship - a model defined in OpenAPI

        id: The id of this FeatureRelationship [Optional].
        name: The name of this FeatureRelationship.
        relationship_type: The relationship_type of this FeatureRelationship.
        valid_for: The valid_for of this FeatureRelationship [Optional].
    """

    id: Optional[str] = None
    name: str
    relationship_type: str
    valid_for: Optional[TimePeriod] = None

FeatureRelationship.update_forward_refs()
