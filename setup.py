from skbuild import setup

setup(
    name="climate_network",
    version="0.1",
    description="Library to construct Climate networks from geospatial time series data",
    author=["Niccolò Zanotti", "Francesco Baiocchi"],
    packages=["climate_network"],
    cmake_install_dir=".",
    python_requires=">=3.12",
    install_requires=["numpy>=2.0"],
    extras_require={
        "dev": [
            "cmakelang>=0.6.13",
            "fortitude-lint>=0.7.3",
            "ruff>=0.11.9",
            "zizmor>=1.7.0",
        ]
    },
)
