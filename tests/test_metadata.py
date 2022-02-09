from xarray_cube import __author__, __version__


def test_author():
    assert __author__ == "Akio Taniguchi"


def test_version():
    assert __version__ == "0.3.0"
