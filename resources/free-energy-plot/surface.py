import matplotlib.pyplot as plt
from matplotlib import colormaps
import matplotlib
import numpy as np

font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 8.67}

matplotlib.rc('font', **font)

# Create the mesh in polar coordinates and compute corresponding Z.
T = [-0.2, 0.0, 0.4]
u = 1
r = np.linspace(0, 0.6, 50)
p = np.linspace(0, 2*np.pi, 50)
R, P = np.meshgrid(r, p)
axd = {}
figd = {}
bottoms = []
tops = []
for t in T:
    Z = -t*R**2+u*R**4

    # Express the mesh in the cartesian system.
    X, Y = R*np.cos(P), R*np.sin(P)
    bottoms.append(min(Z.flatten()))
    tops.append(max(Z.flatten()))

for t in T:
    fig, ax = plt.subplots(1, 1, subplot_kw=dict(projection='3d'), figsize=(2.4, 2.4))
    Z = -t*R**2+u*R**4

    # Express the mesh in the cartesian system.
    X, Y = R*np.cos(P), R*np.sin(P)


    # Plot the surface.
    ax.plot_surface(X, Y, Z, cmap=plt.cm.YlGnBu_r)

    # Tweak the limits and add latex math labels.
    bottoms.append(min(Z.flatten()))
    tops.append(max(Z.flatten()))
    ax.set_xlabel(r'$\mathrm{Re}\Psi$')
    ax.set_ylabel(r'$\mathrm{Im}\Psi$')
    ax.set_zlabel(r'$f$')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([0])
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_zticklabels([0.0])

    smallX = np.linspace(ax.get_xlim()[0], ax.get_xlim()[1], 50)
    smallY = np.linspace(ax.get_ylim()[0], ax.get_ylim()[1], 50)
    bigX, bigY = np.meshgrid(smallX, smallY)
    Zero = 0.0*bigX
    ax.set_zlim(min(bottoms), max(tops))
    fig.tight_layout()

    fig.savefig(f'surface_{t}.pdf')
