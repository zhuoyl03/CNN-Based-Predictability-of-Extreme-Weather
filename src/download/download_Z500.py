# src/download/download_z500.py
import cdsapi
from pathlib import Path

OUT = Path("data/raw")
OUT.mkdir(parents=True, exist_ok=True)

c = cdsapi.Client()

years = [str(y) for y in range(2010, 2020)]
months = ["12", "01", "02"]
days = [f"{d:02d}" for d in range(1, 32)]
times = ["00:00", "06:00", "12:00", "18:00"]

c.retrieve(
    "reanalysis-era5-pressure-levels",
    {
        "product_type": "reanalysis",
        "format": "netcdf",
        "variable": "geopotential",
        "pressure_level": "500",
        "year": years,
        "month": months,
        "day": days,
        "time": times,
        # area = [North, West, South, East]
        "area": [80, -180, 20, 180],
        # grid = [lat, lon] in degrees
        "grid": [2.5, 2.5],
    },
    str(OUT / "era5_z500_2p5_2010_2019_DJF_6hour.nc"),
)


