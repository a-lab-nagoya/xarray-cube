__all__ = ["Cube"]


# standard library
from dataclasses import dataclass
from typing import Any, Tuple


# dependencies
import numpy as np
from astropy.io.fits import ImageHDU
from typing_extensions import Literal
from xarray_dataclasses import AsDataArray, Attr, Coord, Coordof, Data, Name


# constants
CUBE_NDIM = 3
DEFAULT_INT = 0
DEFAULT_STR = ""


# type hints
S = Literal["s"]
Y = Literal["y"]
X = Literal["x"]


# dataclasses
@dataclass
class SAxis:
    """Pixel coordinate of the spectral axis."""

    data: Data[S, int] = DEFAULT_INT
    long_name: Attr[str] = "Spectral axis"
    standard_name: Attr[str] = "S axis"
    units: Attr[str] = "pixel"


@dataclass
class YAxis:
    """Pixel coordinate of the latitude axis."""

    data: Data[Y, int] = DEFAULT_INT
    long_name: Attr[str] = "Latitude axis"
    standard_name: Attr[str] = "Y axis"
    units: Attr[str] = "pixel"


@dataclass
class XAxis:
    """Pixel coordinate of the longitude axis."""

    data: Data[X, int] = DEFAULT_INT
    long_name: Attr[str] = "Longitude axis"
    standard_name: Attr[str] = "X axis"
    units: Attr[str] = "pixel"


@dataclass
class Cube(AsDataArray):
    """Representation of spectral cubes in xarray."""

    data: Data[Tuple[S, Y, X], Any]
    """Data of an HDU as a three-dimensional array."""

    header: Coord[Tuple[()], str] = DEFAULT_STR
    """Header of an HDU as a string."""

    s: Coordof[SAxis] = DEFAULT_INT
    """Pixel coordinate of the spectral axis."""

    y: Coordof[YAxis] = DEFAULT_INT
    """Pixel coordinate of the latitude axis."""

    x: Coordof[XAxis] = DEFAULT_INT
    """Pixel coordinate of the longitude axis."""

    name: Name[str] = "Cube"
    """Name of a DataArray object."""

    def __post_init__(self):
        """Initialize coordinates if default values are given."""
        shape = np.shape(self.data)  # type: ignore

        if len(shape) != CUBE_NDIM:
            raise ValueError("Data must have three dimensions.")

        if self.header == DEFAULT_STR:
            self.header = ImageHDU(self.data).header.tostring()

        if self.s == self.y == self.x == DEFAULT_INT:
            self.s, self.y, self.x = map(np.arange, shape)
