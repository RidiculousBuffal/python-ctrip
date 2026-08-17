"""Shared Pydantic model behavior for the Ctrip SDK."""

from pydantic import BaseModel, ConfigDict


class CtripBaseModel(BaseModel):
    """Base model compatible with additional fields returned by Ctrip APIs."""

    model_config = ConfigDict(extra="ignore")

    def model_dump(self, **kwargs):
        kwargs.setdefault("exclude_none", True)
        return super().model_dump(**kwargs)

    def model_dump_json(self, **kwargs):
        kwargs.setdefault("exclude_none", True)
        return super().model_dump_json(**kwargs)
