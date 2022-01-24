import xarray as xr
from astropy.wcs import WCS
from astropy.io import fits


@xr.register_dataarray_accessor("cube")
class CubeAccessor:
    def __init__(self, xarray_obj: xr.DataArray) -> None:
        self._obj = xarray_obj

    @property
    def header(self) -> fits.Header:
        """Convert the header string to a header object."""
        return fits.Header.fromstring(self._obj.header.item())

    @property
    def wcs(self) -> WCS:
        """Extract wcs"""
        return WCS(self._obj.cube.header)
