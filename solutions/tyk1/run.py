import os
from yggdrasil import tools
from yggdrasil.runner import run
if not os.path.isdir('output'):
    os.mkdir('output')

# Part 1: YAML
tools.display_source('yamls/weather.yml', number_lines=True)

# Part 2: Run
run(['yamls/weather.yml'], production_run=True)
