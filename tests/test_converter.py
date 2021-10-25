from pathlib import Path

from astropy.io import fits
import spectral_cube as sc

from xarray_cube import Cube  # , converter

DATA_DIR = Path("data")

hdu = fits.open(DATA_DIR / "GMC-8.spw16.12CO.7m.cube.pbcor.fits")
expected_data_array = Cube(hdu.data, hdu.header.tostring())
expected_sc_cube = sc.SpectralCube(hdu)


def test_header():
    assert True


def test_data():
    assert True
