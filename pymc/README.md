Simple pymc notebook based on https://www.pymc.io/projects/docs/en/latest/learn/core_notebooks/pymc_overview.html#a-motivating-example-linear-regression

Setup and install pymc with 

uv init pymc_start
cd pymc_start/
uv add pymc

For some reason (MCMC sampling throws some weird error) we cannot run the stuff in a "normal" python script (which we would run using uv run main.py) but need a notebook instead. This we run using

uv run --with jupyter jupyter lab
