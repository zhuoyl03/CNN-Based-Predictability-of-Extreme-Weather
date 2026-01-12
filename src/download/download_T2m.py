# src/download/download_t2m.py
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
    "reanalysis-era5-single-levels",
    {
        "product_type": "reanalysis",
        "format": "netcdf",
        "variable": "2m_temperature",
        "year": years,
        "month": months,
        "day": days,
        "time": times,
        "area": [80, -180, 20, 180],
        "grid": [2.5, 2.5],
    },
    str(OUT / "era5_t2m_2p5_2010_2019_DJF_6hour.nc"),
)
