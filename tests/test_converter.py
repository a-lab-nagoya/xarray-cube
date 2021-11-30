from pathlib import Path

import numpy as np
import spectral_cube as sc
from astropy.io import fits

from xarray_cube import Cube, converter

DATA_DIR = Path("data")

hdu = fits.open(DATA_DIR / "GMC-8.spw16.12CO.7m.cube.pbcor.fits")[0]
expected_data_array = Cube.new(hdu.data, hdu.header.tostring())
header_expected_data_array = fits.Header.fromstring(expected_data_array.header.item())
expected_sc_cube = sc.SpectralCube.read(hdu)

mask_expected_data_array = np.isnan(expected_data_array)
mask_expected_sc_cube = np.isnan(expected_sc_cube.hdu.data)


def test_spectralcube2xarray():
    actual_data_array = converter.spectralcube2xarray(expected_sc_cube)
    mask_actual_data_array = np.isnan(actual_data_array)
    header_actual_data_array = fits.Header.fromstring(actual_data_array.header.item())
    assert (
        expected_data_array.values[~mask_expected_data_array]
        == actual_data_array.values[~mask_actual_data_array]
    ).all()
    assert header_expected_data_array["NAXIS"] == header_actual_data_array["NAXIS"]


def test_xarray2spectralcube():
    actual_sc_cube = converter.xarray2spectralcube(expected_data_array)
    mask_actual_sc_cube = np.isnan(actual_sc_cube.hdu.data)
    assert (
        expected_sc_cube.hdu.data[~mask_expected_sc_cube]
        == actual_sc_cube.hdu.data[~mask_actual_sc_cube]
    ).all()
    assert expected_sc_cube.hdu.header["NAXIS"] == actual_sc_cube.hdu.header["NAXIS"]


def test_loop_conversion():
    tmp_data_array = converter.spectralcube2xarray(expected_sc_cube)
    actual_sc_cube = converter.xarray2spectralcube(tmp_data_array)
    mask_actual_sc_cube = np.isnan(actual_sc_cube.hdu.data)
    assert (
        expected_sc_cube.hdu.data[~mask_expected_sc_cube]
        == actual_sc_cube.hdu.data[~mask_actual_sc_cube]
    ).all()

    tmp_sc_cube = converter.xarray2spectralcube(expected_data_array)
    actual_data_array = converter.spectralcube2xarray(tmp_sc_cube)
    mask_actual_data_array = np.isnan(actual_data_array)
    assert (
        expected_data_array.values[~mask_expected_data_array]
        == actual_data_array.values[~mask_actual_data_array]
    ).all()
