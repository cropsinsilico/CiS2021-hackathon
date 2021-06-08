import os
from yggdrasil import tools
from yggdrasil.runner import run
tyk_dir = 'tyk3'

try:
    # Change to the solution directory
    old_dir = os.getcwd()
    if not old_dir.endswith(tyk_dir):
        os.chdir(os.path.join('solutions', tyk_dir))
    if not os.path.isdir('output'):
        os.mkdir('output')

    # Part 1: light-to-weather
    tools.display_source('yamls/light_to_weather.yml', number_lines=True)
    run(['yamls/light_to_weather.yml', 'yamls/light_v0_python.yml'],
        production_run=True)

    # Part 2: shoot-to-co2
    tools.display_source('yamls/shoot_to_co2.yml', number_lines=True)
    run(['yamls/shoot_to_co2.yml', 'yamls/shoot_v1.yml', 'yamls/co2.yml'],
        production_run=True)

    # Part 3: shoot-to-light&co2
    tools.display_source('yamls/shoot_to_light_and_co2.yml', number_lines=True)
    run(['yamls/shoot_to_light_and_co2.yml', 'yamls/shoot_v1.yml',
         'yamls/co2.yml', 'yamls/light_v0_python.yml'], production_run=True)

finally:
    os.chdir(old_dir)
