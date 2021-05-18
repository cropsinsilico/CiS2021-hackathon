import os
import trimesh
import argparse
import numpy as np
from yggdrasil import units
from yggdrasil.languages.Python.YggInterface import YggRpcClient, YggOutput


def run(mesh, tmin, tmax, tstep):
    mass = 2000.0
    mesh_out = YggOutput('mesh')
    mass = units.add_units(mass, 'g')
    tmin = units.add_units(tmin, 'hrs')
    tmax = units.add_units(tmax, 'hrs')
    tstep = units.add_units(tstep, 'hrs')
    t = tmin

    while t <= tmax:

        # Grow mesh
        # (pretend this is a biologically complex calculation)
        scale = units.get_data(mass * t / units.add_units(1.5e6, 'g*hrs'))
        mesh.vertices[:, 2] += mesh.vertices[:, 2] * scale

        # Send mesh to output for this timestep
        flag = mesh_out.send(mesh)
        if not flag:
            raise Exception("Error sending mesh to output")

        # Advance time step
        t += tstep

    return mesh


# Parse command-line arguments
if __name__ == "__main__":
    parser = argparse.ArgumentParser("Simulate plant growth over time.")
    parser.add_argument('tmin', help='Starting time (in hours)', type=float)
    parser.add_argument('tmax', help='Ending time (in hours)', type=float)
    parser.add_argument('tstep', help='Time step (in hours)', type=float)
    parser.add_argument('--meshfile', help='Path to file where mesh is stored.',
                        default='../meshes/plants-2.obj')
    args = parser.parse_args()
    mesh = trimesh.load_mesh(args.meshfile)
    run(mesh, args.tmin, args.tmax, args.tstep)
