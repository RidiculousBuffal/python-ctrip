from .approval import ApprovalClient
from .ctrip_base_model import CtripBaseModel
from .details import CarOrderDetailsQuery, FlightOrderDetailsQuery, HotelOrderDetailQuery, TrainOrderDetailsQuery
from .basedata import BaseDataClient
from .people import PeopleClient
from .sso import SSOClient

__all__ = [
    "ApprovalClient",
    "CtripBaseModel",
    "CarOrderDetailsQuery",
    "FlightOrderDetailsQuery",
    "HotelOrderDetailQuery",
    "TrainOrderDetailsQuery",
    "BaseDataClient",
    "PeopleClient",
    "SSOClient",
]
