"""Downloading data from ERA5 post-processed monthly averaged dataset https://doi.org/10.24381/cds.f17050d7."""

from pathlib import Path

import cdsapi
import xarray as xr

if __name__ == "__main__":
    dataset_name = "reanalysis-era5-single-levels-monthly-means"
    request = {
        "product_type": ["monthly_averaged_reanalysis"],
        "variable": ["skin_temperature"],
        "year": [str(year) for year in range(1981, 2011)],
        "month": [f"{month:02d}" for month in range(1, 13)],
        "day": [f"{day:02d}" for day in range(1, 32)],
        "time": ["00:00"],
        "area": "global",
        "data_format": "grib",
        "download_format": "unarchived",
    }

    dataset_path = Path(__file__).parent / f"{dataset_name}.grib"

    # dataset hasn't been donwloaded yet
    if not dataset_path.exists():
        client = cdsapi.Client()

        raw_dataset = client.retrieve(dataset_name, request, f"{dataset_name}.grib")

