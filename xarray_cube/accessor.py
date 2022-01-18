import xarray as xr
import astropy
from astropy.io import fits

from . import converter


@xr.register_dataarray_accessor("cube")
class CubeAccessor:
    def __init__(self, xarray_obj: xr.DataArray) -> None:
        self._obj = xarray_obj

    @property
    def header(self) -> fits.header.Header:
        """Convert the header string to a header object."""
        return fits.Header.fromstring(self._obj.header.item())

    @property
    def wcs(self) -> astropy.wcs.wcs.WCS:
        """Extract header"""
        return converter.xarray2spectralcube(self._obj).wcs
