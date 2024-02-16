#!/bin/bash

# Run a specific cell in a Jupyter notebook
jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=-1 --ExecutePreprocessor.allow_errors=True --ExecutePreprocessor.kernel_name=python --execute weekly_pulls.ipynb --ExecutePreprocessor.cell_indices=1-64