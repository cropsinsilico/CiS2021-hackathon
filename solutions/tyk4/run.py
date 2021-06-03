import os
from yggdrasil import tools
from yggdrasil.runner import run
if not os.path.isdir('output'):
    os.mkdir('output')

# Part 1: shoot calling light and weather
tools.display_source_diff('../../models/shoot_v2.py',
                          'models/shoot_calling_light_and_weather.py',
                          number_lines=True)
tools.display_source('yamls/shoot_calling_light_and_weather.yml', number_lines=True)
run(['yamls/shoot_calling_light_and_weather.yml'], production_run=True)

# Part 2: light-calling-weather
tools.display_source_diff('../../models/light_v0.py',
                          'models/light_calling_weather.py', number_lines=True)
tools.display_source('yamls/light_calling_weather.yml', number_lines=True)
run(['yamls/light_calling_weather.yml'], production_run=True)

# Part 3: shoot calling light calling weather
tools.display_source_diff('../../models/shoot_v2.py',
                          'models/shoot_calling_light_calling_weather.py',
                          number_lines=True)
tools.display_source('yamls/shoot_calling_light_calling_weather.yml',
                     number_lines=True)
run(['yamls/shoot_calling_light_calling_weather.yml'],
    production_run=True)


