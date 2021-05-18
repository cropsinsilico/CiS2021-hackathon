import os
import glob
import pickle
import inspect
import trimesh
import matplotlib.pyplot as plt


def display_last_timestep(with_light=False, with_masses=False):
    last_mesh = sorted(glob.glob('output/mesh_*.obj'))[-1]
    mesh = trimesh.load_mesh(last_mesh)
    if with_light:
        last_light = sorted(glob.glob('output/light_*.pkl'))[-1]
        with open(last_light, 'rb') as fd:
            light = pickle.load(fd)
        mesh.visual.vertex_colors = trimesh.visual.interpolate(
            light/max(light))
    if with_masses:
        plot_mass()
        return mesh.show()
    return mesh.show()


def plot_mass():
    from yggdrasil.communication.AsciiTableComm import AsciiTableComm
    fd = AsciiTableComm('mass', address='output/mass.txt', direction='recv',
                        as_array=True)
    flag, masses = fd.recv_dict()
    plt.plot(masses['time'], masses['root_mass'], label='root mass')
    plt.plot(masses['time'],
             masses['plant_mass'].to(masses['root_mass'].units),
             label='plant_mass')
    plt.plot(masses['time'],
             masses['total_mass'].to(masses['root_mass'].units),
             label='total_mass')
    plt.xlabel('time (%s)' % masses['time'].units)
    plt.ylabel('mass (%s)' % masses['root_mass'].units)
    plt.legend()
    return plt.show()
