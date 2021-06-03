import numpy as np


temp = np.array([400.0, 410.0, 420.0, 430.0, 440.0, 450.0])  # Temp in K
theta_i = np.linspace(0.0, np.pi / 2, 10)  # radians
n1 = 1.0
n2 = 1.5


for i in range(len(temp)):
    in1 = n1 - 0.0001 * (400.0 - temp[i])
    in2 = n2 - 0.05 * (400.0 - temp[i])
    theta_t = np.arcsin(in1 * np.sin(theta_i) / in2)
    R = np.abs((in1 * np.cos(theta_i) - in2 * np.cos(theta_t))
               / (in1 * np.cos(theta_i) + in2 * np.cos(theta_t)))**2
    print("Reflectance at %s K: %s" % (temp[i], R))
