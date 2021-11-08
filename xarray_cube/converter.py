from astropy.io import fits
import spectral_cube as sc
import xarray as xr

from .cube import Cube


def spectralcube2xarray(cube: sc.SpectralCube) -> xr.DataArray:
    """Convert a SpectralCube to a DataArray object."""

    data_cube = Cube.new(
        data=cube.hdu.data,
        header=cube.hdu.header,
    )
    return data_cube


def xarray2spectralcube(da: xr.DataArray) -> sc.SpectralCube:
    """Convert a DataArray object to a SpectralCube."""
    header = fits.Header.fromstring(da.header.item())
    data = da.values

    cube = sc.SpectralCube(fits.imageHDU(data, header))
    return cube
