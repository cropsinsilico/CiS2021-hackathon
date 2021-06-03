import os
import pickle
import numpy as np
from yggdrasil import tools, units
from yggdrasil.runner import run as run
import matplotlib.pyplot as plt
if not os.path.isdir('output'):
    os.mkdir('output')

if __name__ == '__main__':
    # Part 1: integrate microbe w/ root model
    tools.display_source_diff('../../models/microbe.py',
                              'models/microbe.py', number_lines=True)
    tools.display_source('yamls/microbe.yml', number_lines=True)
    run(['yamls/roots_v1.yml', 'yamls/microbe.yml', 'yamls/timesync.yml'],
        production_run=True)

    # Part 2: integrate microbe w/ root & shoot model
    run(['yamls/roots_v1.yml', 'yamls/microbe.yml', 'yamls/timesync.yml',
         'yamls/shoot_v3.yml', 'yamls/light_v1_python.yml'],
        production_run=True)
    

    # Part 3: plot
    filename_root_masses = 'output/masses.pkl'
    with open(filename_root_masses, 'rb') as fd:
        root_masses = pickle.load(fd)
        root_masses['times'] = units.add_units(
            np.array(root_masses['times']), 'days')
        root_masses['masses'] = units.add_units(
            np.array(root_masses['masses']), 'kg')
        root_masses['times'].convert_to_mks()
        root_masses['masses'].convert_to_mks()
    filename_microbe_masses = 'output/microbe_masses.pkl'
    with open(filename_microbe_masses, 'rb') as fd:
        microbe_masses = pickle.load(fd)
        microbe_masses['times'] = units.add_units(
            np.array(microbe_masses['times']), 'min')
        microbe_masses['masses'] = units.add_units(
            np.array(microbe_masses['masses']), 'g')
        microbe_masses['times'].convert_to_mks()
        microbe_masses['masses'].convert_to_mks()
    plt.plot(root_masses['times'], root_masses['masses'])
    plt.plot(microbe_masses['times'], microbe_masses['masses'])
    plt.show()
