import os
from yggdrasil import tools
from yggdrasil.runner import run
if not os.path.isdir('output'):
    os.mkdir('output')

# Part 1: add copies to isolated light model
tools.display_source_diff('../../yamls/shoot_v1.yml',
                          'yamls/shoot_copies.yml',
                          number_lines=True)

# Part 2: run it & check output
run(['yamls/shoot_copies.yml'], production_run=True)
tools.display_source('output/height.txt')
