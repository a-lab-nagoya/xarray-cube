import spectral_cube as sc
import xarray as xr
from .cube import Cube


def spectralcube2xarray(cube: sc.SpectralCube) -> xr.DataArray:
    """Convert a SpectralCube to a DataArray object."""

    data_cube = Cube.new(
        data=cube.hdu.data,
        header=cube.hdu.header,
        type=cube.hdu.header["BTYPE"],
        units=cube.hdu.header["BUNIT"],
    )
    return data_cube


def xarray2spectralcube(da: xr.DataArray) -> sc.SpectralCube:
    """Convert a DataArray object to a SpectralCube."""
    pass
