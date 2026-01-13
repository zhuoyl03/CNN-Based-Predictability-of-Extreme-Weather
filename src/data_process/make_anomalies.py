import xarray as xr
from pathlib import Path

RAW = Path("data/raw")
OUTPUT = Path("data/interim")
OUTPUT.mkdir(parents=True, exist_ok=True)


def load_data(path: str | Path) -> xr.Dataset:
    """Load the dataset from a NetCDF file.
    Args:
        file_path (str): The path to the NetCDF file.
    Returns:
        xr.Dataset: The loaded dataset.
    """
    file_path = Path(path)
    ds = xr.open_dataset(file_path)
    return ds

# -------- Z500 --------
ds_z500 = load_data(RAW / "era5_z500_2p5_2010_2019_DJF_6hour.nc")

# daily mean  
z500_daily = (
ds_z500["z"]
.sel(pressure_level=500)
.resample(valid_time="1D")
.mean()
/ 9.81
)

# climatology
clim = z500_daily.groupby("valid_time.dayofyear").mean("valid_time")

# anomaly
z500_anom = z500_daily.groupby("valid_time.dayofyear") - clim

z500_anom.to_netcdf(OUTPUT / "z500_anom_daily.nc")



# -------- T2m --------
ds_t2m = load_data(RAW / "era5_t2m_2p5_2010_2019_DJF_6hour.nc")

# daily mean
t2m_daily = (
    ds_t2m["t2m"]
    .resample(valid_time="1D")
    .mean()
    - 273.15
)

# climatology
clim = t2m_daily.groupby("valid_time.dayofyear").mean("valid_time")

# anomaly
t2m_anom = t2m_daily.groupby("valid_time.dayofyear") - clim

da = t2m_anom.isel(valid_time=0)
t2m_anom.to_netcdf(OUTPUT / "t2m_anom_daily.nc")