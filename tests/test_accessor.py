from pathlib import Path

from astropy.io import fits

import xarray_cube

DATA_DIR = Path("data")

hdu = fits.open(DATA_DIR / "GMC-8.spw16.12CO.7m.cube.pbcor.fits")[0]


def test_header():
    assert (
        xarray_cube.Cube.new(hdu.data, hdu.header.tostring()).cube.header == hdu.header
    )
