# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class AttachmentRef(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    AttachmentRef - a model defined in OpenAPI

        id: The id of this AttachmentRef.
        href: The href of this AttachmentRef [Optional].
        description: The description of this AttachmentRef [Optional].
        name: The name of this AttachmentRef [Optional].
        url: The url of this AttachmentRef [Optional].
        base_type: The base_type of this AttachmentRef [Optional].
        schema_location: The schema_location of this AttachmentRef [Optional].
        type: The type of this AttachmentRef [Optional].
        referred_type: The referred_type of this AttachmentRef [Optional].
    """

    id: str
    href: Optional[AnyUrl] = None
    description: Optional[str] = None
    name: Optional[str] = None
    url: Optional[AnyUrl] = None
    base_type: Optional[str] = None
    schema_location: Optional[AnyUrl] = None
    type: Optional[str] = None
    referred_type: Optional[str] = None

AttachmentRef.update_forward_refs()
