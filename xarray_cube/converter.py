import spectral_cube as sc
import xarray as xr
from .cube import Cube


def spectralcube2xarray(cube: sc.SpectralCube) -> xr.DataArray:
    """Convert a SpectralCube to a DataArray object."""

    DataCube = Cube.new(
        data=cube.hdu.data,
        header=cube.hdu.header,
        Name=cube.hdu.header["BTYPE"],
        units=cube.hdu.header["BUNIT"],
    )
    return DataCube


def xarray2spectralcube(data: xr.DataArray) -> sc.SpectralCube:
    """Convert a DataArray object to a SpectralCube."""
    pass
