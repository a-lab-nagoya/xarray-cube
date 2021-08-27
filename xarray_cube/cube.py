# standard library
from dataclasses import dataclass
from typing import Any, Tuple


# dependencies
from typing_extensions import Literal
from xarray_dataclasses import Attr, Data


# type hints
X = Literal["x"]
Y = Literal["y"]
S = Literal["s"]


# dataclasses
@dataclass
class XAxis:
    """DataArray specs of longitude axis."""

    data: Data[X, int] = 0
    long_name: Attr[str] = "Longitude axis"
    standard_name: Attr[str] = "X axis"
    units: Attr[str] = "pixel"


@dataclass
class YAxis:
    """DataArray specs of latitude axis."""

    data: Data[Y, int] = 0
    long_name: Attr[str] = "Latitude axis"
    standard_name: Attr[str] = "Y axis"
    units: Attr[str] = "pixel"


@dataclass
class SAxis:
    """DataArray specs of spectral axis."""

    data: Data[S, int] = 0
    long_name: Attr[str] = "Spectral axis"
    standard_name: Attr[str] = "S axis"
    units: Attr[str] = "pixel"
