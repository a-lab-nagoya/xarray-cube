import spectral_cube as sc
import xarray as xr
from astropy.io import fits

from .cube import Cube


def spectralcube2xarray(cube: sc.SpectralCube) -> xr.DataArray:
    """Convert a SpectralCube to a DataArray object."""

    return Cube.new(
        data=cube.hdu.data,
        header=cube.hdu.header.tostring(),
    )


def xarray2spectralcube(da: xr.DataArray) -> sc.SpectralCube:
    """Convert a DataArray object to a SpectralCube."""
    header = fits.Header.fromstring(da.header.item())
    data = da.values

    return sc.SpectralCube.read(fits.ImageHDU(data, header))
