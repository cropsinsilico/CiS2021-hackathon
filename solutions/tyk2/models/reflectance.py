import os
import numpy as np


temp = np.array([400.0, 410.0, 420.0, 430.0, 440.0, 450.0])  # Temp in K
theta_i = np.linspace(0.0, np.pi / 2, 10)  # radians
n1 = 1.0
n2 = 1.5

# Check if model is running as a part of an yggdrasil integration
with_yggdrasil = os.environ.get('YGG_SUBPROCESS', False)

# If the model is running as part of an yggdrasil integration, import
# the relevant yggdrasil routines and use the interface routine to
# complete the connection defined in the YAML
if with_yggdrasil:
    from yggdrasil import units
    from yggdrasil.languages.Python.YggInterface import YggInput, YggOutput
    temp_in = YggInput('temperature')
    refl_out = YggOutput('reflectance')

    # Receive the temperatures
    flag, temp = temp_in.recv()
    if not flag:
        raise Exception("Error receiving temperature.")

    # Ensure correct units
    temp = units.convert_to(temp[0], 'K')  # list of one table column
    temp = units.get_data(temp)


for i in range(len(temp)):
    in1 = n1 - 0.0001 * (400.0 - temp[i])
    in2 = n2 - 0.05 * (400.0 - temp[i])
    theta_t = np.arcsin(in1 * np.sin(theta_i) / in2)
    R = np.abs((in1 * np.cos(theta_i) - in2 * np.cos(theta_t))
               / (in1 * np.cos(theta_i) + in2 * np.cos(theta_t)))**2
    print("Reflectance at %s K: %s" % (temp[i], R))
    if with_yggdrasil:
        flag = refl_out.send(temp[i], *R)  # expand array elements
        if not flag:
            raise Exception("Error sending reflectance")
