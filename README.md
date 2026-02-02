# GAIA DR3 Earth-Centric Star Mapper

The following project uses GAIA DR3 data to create an Earth-centric map of nearby stars (given a distance in parsecs), and simulate the time evolution of the selected system in 5000 years per frame.

## Features
- **Static 3D star map** in parsecs using `(ra, dec, parallax)`
- Color modes:
  - `by_distance` (pc)
  - `by_mag` (Gaia `phot_g_mean_mag`)
- Auto marker sizing + **star count** overlay
- **Animated mode** builds full 6D phase space using:
  - proper motion (`pmra`, `pmdec`) + radial velocity (`radial_velocity`)
  - optional uncertainty sampling (`*_error` columns, if present)
- Embeds a **JS animation** directly in the notebook output

## Quick start

```bash
uv venv
uv pip install -e .
```

Open `nbs/main_file.ipynb` to run the simulator.

To use the built-in functions to create a plot or simulation, pass in a distance limit with units (parsecs recommended; add `u.pc` after the number) followed by the output design (whether or not you want the stars to be colored by distance or by birghtness; "by_distance" and "by_mag" are the appropriate inputs respectively). If using the animation function, beware of long runtime for large distances. Each frame is hardcoded to 5000 years.


## NOTES:
- The animation is a toy model (smooth Plummer potential; not a full Galactic orbit model or N-body simulation).
- A UV file is included but just in case, the required packages are:
  NumPy,
  AstroPy,
  Matplotlib,
  Agama,
  SciPy,
  Pandas.
  IPython
