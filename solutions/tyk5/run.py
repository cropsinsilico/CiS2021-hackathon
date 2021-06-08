import os
from yggdrasil import tools
from yggdrasil.runner import run
tyk_dir = 'tyk5'

try:
    # Change to the solution directory
    old_dir = os.getcwd()
    if not old_dir.endswith(tyk_dir):
        os.chdir(os.path.join('solutions', tyk_dir))
    if not os.path.isdir('output'):
        os.mkdir('output')

    # Part 1: add copies to isolated light model
    tools.display_source_diff('../../yamls/shoot_v1.yml',
                              'yamls/shoot_copies.yml',
                              number_lines=True)

    # Part 2: run it & check output
    run(['yamls/shoot_copies.yml'], production_run=True)
    tools.display_source('output/height.txt')

finally:
    os.chdir(old_dir)
