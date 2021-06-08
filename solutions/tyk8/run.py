import os
from yggdrasil.runner import run
from yggdrasil import tools
tyk_dir = 'tyk8'

try:
    # Change to the solution directory
    old_dir = os.getcwd()
    if not old_dir.endswith(tyk_dir):
        os.chdir(os.path.join('solutions', tyk_dir))
    if not os.path.isdir('output'):
        os.mkdir('output')

    # Part 1: Sort intensities
    tools.display_source_diff('../../yamls/connections_v0.yml',
                              'yamls/connections_sort_intensity.yml',
                              number_lines=True)
    run(['yamls/light_v0_python.yml', 'yamls/connections_sort_intensity.yml'],
        production_run=True)
    tools.display_source('output/light_filter_lt400.txt', number_lines=True)
    tools.display_source('output/light_filter_ge400.txt', number_lines=True)

    # Part 2: New light model
    tools.display_source_diff('models/light_v0.py', 'models/light_new.py',
                              number_lines=True)
    tools.display_source_diff('yamls/light_v0_python.yml',
                              'yamls/light_new_python.yml', number_lines=True)
    tools.display_source_diff('../../yamls/connections_v0.yml',
                              'yamls/connections_sort_height.yml',
                              number_lines=True)
    run(['yamls/light_v0_python.yml', 'yamls/light_new_python.yml',
         'yamls/connections_sort_height.yml'],
        production_run=True)
    tools.display_source('output/light_multi_model.txt', number_lines=True)

    # Part 3: Transformation
    tools.display_source_diff('yamls/connections_sort_height.yml',
                              'yamls/connections_sort_height_transform.yml',
                              number_lines=True)
    run(['yamls/light_v0_python.yml', 'yamls/light_new_python.yml',
         'yamls/connections_sort_height_transform.yml'],
        production_run=True)
    tools.display_source('output/light_multi_model_transform.txt',
                         number_lines=True)

finally:
    os.chdir(old_dir)
