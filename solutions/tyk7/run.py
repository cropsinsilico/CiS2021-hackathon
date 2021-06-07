import os
from yggdrasil import import_as_function
from yggdrasil import tools, units
if not os.path.isdir('output'):
    os.mkdir('output')

# Part 1: import the weather model
x = import_as_function('yamls/weather_alone.yml')
x.model_info()
print(x(123.0))
x.stop()

# Part 2: import the co2 model
x = import_as_function('yamls/co2.yml')
x.model_info()
print(x(units.add_units(24.0, 'hrs'), units.add_units(2.9, 'cm')))
x.stop()
