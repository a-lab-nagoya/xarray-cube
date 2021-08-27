__all__ = ["Cube"]


# standard library
from dataclasses import dataclass
from typing import Any, Tuple


# dependencies
from typing_extensions import Literal
from xarray_dataclasses import AsDataArray, Attr, Coordof, Data


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


@dataclass
class Cube(AsDataArray):
    """DataArray specs of spectral cube."""

    data: Data[Tuple[X, Y, S], Any]
    x: Coordof[XAxis] = 0
    y: Coordof[YAxis] = 0
    s: Coordof[SAxis] = 0
