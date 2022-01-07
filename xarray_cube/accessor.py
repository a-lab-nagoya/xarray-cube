import xarray as xr
from astropy.io import fits


@xr.register_dataarray_accessor("cube")
class CubeAccessor:
    def __init__(self, xarray_obj: xr.DataArray) -> None:
        self._obj = xarray_obj

    @property
    def header(self) -> fits.header.Header:
        """Return header object of Astropy."""
        return fits.Header.fromstring(self._obj.header.item())