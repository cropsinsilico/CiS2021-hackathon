import os
from yggdrasil import tools
from yggdrasil.runner import run
tyk_dir = 'tyk1'

try:
    # Change to the solution directory
    old_dir = os.getcwd()
    if not old_dir.endswith(tyk_dir):
        os.chdir(os.path.join('solutions', tyk_dir))
    if not os.path.isdir('output'):
        os.mkdir('output')

    # Part 1: YAML
    tools.display_source('yamls/weather.yml', number_lines=True)

    # Part 2: Run
    run(['yamls/weather.yml'], production_run=True)

    # Part 3: Open ended...

finally:
    os.chdir(old_dir)
