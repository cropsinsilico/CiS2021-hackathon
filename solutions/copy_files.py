r"""Script to copy models from the root of the repo"""
import os
import shutil

solutions_dir = os.path.abspath(os.path.dirname(__file__))
files = {
    'tyk1': [
        'models/weather.py',
        'input/intensity.txt',
    ],
    'tyk2': [
        'yamls/co2.yml',
        'models/humidity.py',
        'input/height.txt',
        'input/co2.txt',
        'input/temp.txt',
    ],
    'tyk3': [
        'models/light_v0.py',
        'yamls/light_v0_python.yml',
        'models/weather.py',
        'models/shoot_v1.py',
        'yamls/shoot_v1.yml',
        'yamls/co2.yml',
        'input/height.txt',
        (os.path.join(solutions_dir, 'tyk2/models/co2.py'),
         os.path.join(solutions_dir, 'tyk3/models/co2.py')),
        'meshes/plants-2.obj'
        ],
    'tyk4': [
        'models/light_v0.py',
        'models/weather.py',
        'input/height.txt',
        'meshes/plants-2.obj',
    ],
    'tyk5': [
        'models/shoot_v1.py',
        'meshes/plants-2.obj',
    ],
    'tyk6': [
        'yamls/roots_v1.yml',
        'models/roots_v1.py',
        'yamls/shoot_v3.yml',
        'models/shoot_v3.py',
        'yamls/light_v1_python.yml',
        'models/light_v0.py',
        'yamls/timesync.yml',
        'meshes/plants-2.obj',
    ],
    'tyk7': [
        'models/weather.py',
        'yamls/co2.yml',
        (os.path.join(solutions_dir, 'tyk2/models/co2.py'),
         os.path.join(solutions_dir, 'tyk7/models/co2.py')),
    ],
    'tyk8': [
        'models/light_v0.py',
        'yamls/light_v0_python.yml',
        'input/light_v0.txt',
    ],
}


for k, kset in files.items():
    input_dir = os.path.join(solutions_dir, k, 'input')
    if not os.path.isdir(input_dir):
        os.mkdir(input_dir)
    for f in kset:
        if isinstance(f, tuple):
            src = f[0]
            dst = f[1]
        else:
            src = os.path.join(solutions_dir, '..', f)
            dst = os.path.join(solutions_dir, k, f)
        # print(src, dst)
        assert(os.path.isfile(src))
        dst_dir = os.path.dirname(dst)
        if not os.path.isdir(dst_dir):
            os.mkdir(dst_dir)
        shutil.copy2(src, dst)
