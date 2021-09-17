# standard library
from pathlib import Path


# dependencies
import xarray as xr


# submodules
from xarray_cube.cube import Cube


# constants
DATA_DIR = Path("data")


# test data
cube_netcdf = xr.open_dataarray(DATA_DIR / "cube-ones-5x4x3.nc")
cube_runtime = Cube.ones([5, 4, 3], type="Intensity", units="Jy/beam")


# test functions
def test_data():
    assert (cube_runtime.data == cube_netcdf.data).all()


def test_header():
    assert (cube_runtime.header == cube_netcdf.header).all()


def test_xaxis():
    assert (cube_runtime.x == cube_netcdf.x).all()
    assert cube_runtime.x.attrs == cube_netcdf.x.attrs


def test_yaxis():
    assert (cube_runtime.y == cube_netcdf.y).all()
    assert cube_runtime.y.attrs == cube_netcdf.y.attrs


def test_saxis():
    assert (cube_runtime.s == cube_netcdf.s).all()
    assert cube_runtime.s.attrs == cube_netcdf.s.attrs


def test_name():
    assert cube_runtime.name == cube_netcdf.name
