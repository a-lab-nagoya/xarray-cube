from xarray_cube import __author__, __version__


def test_author():
    assert __author__ == "xarray-cube developers"


def test_version():
    assert __version__ == "0.3.1"
