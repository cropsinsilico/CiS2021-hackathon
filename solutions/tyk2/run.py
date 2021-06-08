import os
from yggdrasil import tools
from yggdrasil.runner import run
tyk_dir = 'tyk2'

try:
    # Change to the solution directory
    old_dir = os.getcwd()
    if not old_dir.endswith(tyk_dir):
        os.chdir(os.path.join('solutions', tyk_dir))
    if not os.path.isdir('output'):
        os.mkdir('output')

    # Part 1: Add interface calls
    tools.display_source_diff('../../models/co2.py', 'models/co2.py', number_lines=True)
    run(['yamls/co2.yml'], production_run=True)

    # Part 2: Write a YAML
    tools.display_source('yamls/humidity.yml', number_lines=True)
    run(['yamls/humidity.yml'], production_run=True)

    # Part 3: Add interface calls and write a YAML
    tools.display_source_diff('../../models/reflectance.py', 'models/reflectance.py', number_lines=True)
    tools.display_source('yamls/reflectance.yml', number_lines=True)
    run(['yamls/reflectance.yml'], production_run=True)

finally:
    os.chdir(old_dir)
