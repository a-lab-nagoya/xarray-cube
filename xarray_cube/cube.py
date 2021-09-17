__all__ = ["Cube"]


# standard library
from dataclasses import dataclass
from typing import Any, Tuple


# dependencies
import numpy as np
from astropy.io.fits import Header, ImageHDU
from typing_extensions import Literal
from xarray_dataclasses import AsDataArray, Attr, Coord, Coordof, Data, Name


# constants
CUBE_NDIM = 3
DEFAULT_INT = 0
DEFAULT_STR = ""
TYPE_KEYWORD = "BTYPE"
UNIT_KEYWORD = "BUNIT"


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
    short_name: Attr[str] = "S axis"
    units: Attr[str] = "pixel"


@dataclass
class YAxis:
    """Pixel coordinate of the latitude axis."""

    data: Data[Y, int] = DEFAULT_INT
    long_name: Attr[str] = "Latitude axis"
    short_name: Attr[str] = "Y axis"
    units: Attr[str] = "pixel"


@dataclass
class XAxis:
    """Pixel coordinate of the longitude axis."""

    data: Data[X, int] = DEFAULT_INT
    long_name: Attr[str] = "Longitude axis"
    short_name: Attr[str] = "X axis"
    units: Attr[str] = "pixel"


@dataclass
class Cube(AsDataArray):
    """Spectral cube in astronomy."""

    data: Data[Tuple[S, Y, X], Any]
    """Cube data as a three-dimensional array."""

    header: Coord[Tuple[()], str] = DEFAULT_STR
    """Cube header. Defaults to an empty FITS header."""

    type: Name[str] = DEFAULT_STR
    """Cube type. Defaults to BTYPE in the header."""

    units: Attr[str] = DEFAULT_STR
    """Cube units. Defaults to BUNIT in the header."""

    s: Coordof[SAxis] = DEFAULT_INT
    """Pixel coordinate of the spectral axis."""

    y: Coordof[YAxis] = DEFAULT_INT
    """Pixel coordinate of the latitude axis."""

    x: Coordof[XAxis] = DEFAULT_INT
    """Pixel coordinate of the longitude axis."""

    def __post_init__(self):
        """Initialize coordinates if default values are given."""
        shape = np.shape(self.data)  # type: ignore

        if len(shape) != CUBE_NDIM:
            raise ValueError("Data must have three dimensions.")

        if self.header == DEFAULT_STR:
            self.header = ImageHDU(self.data).header.tostring()

        header = Header.fromstring(self.header)

        if self.type == DEFAULT_STR:
            self.type = str(header.get(TYPE_KEYWORD, DEFAULT_STR))

        if self.units == DEFAULT_STR:
            self.units = str(header.get(UNIT_KEYWORD, DEFAULT_STR))

        if self.s == self.y == self.x == DEFAULT_INT:
            self.s, self.y, self.x = map(np.arange, shape)
