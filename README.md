The main jupyter notebook file is titled "main_file" in the "nbs" folder

To use the built-in functions to create a plot or simulation, pass in a distance limit with units (parsecs recommended; add [u.pc] after the number) followed by the output design (whether or not you want the stars to be colored by distance or by birghtness; "by_distance" and "by_mag" are the appropriate inputs respectively). If using the animation function, beware of long runtime for large distances. Each frame is hardcoded to 5000 years. 

QUICK START
```bash
uv venv
uv pip install -e .
```

A UV file is included but just in case, the required packages are:
  NumPy
  AstroPy
  Matplotlib
  Agama
  SciPy
  Pandas
  IPython
