#!/bin/bash
set -e
source /opt/conda/etc/profile.d/conda.sh
conda activate CiS2021-hackathon-environment
jupyter notebook --no-browser --ip=0.0.0.0 --NotebookApp.token='' --NotebookApp.password='' --allow-root
