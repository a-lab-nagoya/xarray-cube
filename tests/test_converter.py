from pathlib import Path

from astropy.io import fits
import spectral_cube as sc

from xarray_cube import Cube, converter

DATA_DIR = Path("data")

hdu = fits.open(DATA_DIR / "GMC-8.spw16.12CO.7m.cube.pbcor.fits")[0]
expected_data_array = Cube.new(hdu.data, hdu.header.tostring())
expected_sc_cube = sc.SpectralCube.read(hdu)


def test_spectralcube2xarray():
    actual_data_array = converter.spectralcube2xarray(expected_sc_cube)
    assert (expected_data_array == actual_data_array).all()


def test_xarray2spectralcube():
    actual_sc_cube = converter.xarray2spectralcube(expected_data_array)
    assert (expected_sc_cube == actual_sc_cube).all()


def test_loop_conversion():
    tmp_data_array = converter.spectralcube2xarray(expected_sc_cube)
    actual_sc_cube = converter.xarray2spectralcube(tmp_data_array)
    assert (expected_sc_cube == actual_sc_cube).all()

    tmp_sc_cube = converter.xarray2spectralcube(expected_data_array)
    actual_data_array = converter.spectralcube2xarray(tmp_sc_cube)
    assert (expected_data_array == actual_data_array).all()
