# Complex network

A library to efficiently reconstruct climate-related networks from geospatial time series data.

> [!NOTE]
> This project is currently in early-development stage.


## Build from source

Many of the computationally-intensive routines are implemented in Fortran and are called from Python via
[F2PY](https://numpy.org/doc/stable/f2py/index.html). 
The package is built using [ scikit-build ](https://scikit-build.readthedocs.io/en/latest/index.html) backend (using `setuptools`) which 
uses CMake to generate the C/Fortran extensions modules.

After making sure the following requirements are satisfied on your system:

* A Fortran/C compiler (e.g. `gcc`)
* CMake >= 3.18
* Ninja >= 1.10

you can build the package in a virtual environment (pip/uv)
```shell
(.venv) pip install . -v
```
or by preprending `uv` if using uv.

### Tests

To test the Fortran extended modules can be correctly imported run
```shell
(.venv) python tests/test_routines.py
```
