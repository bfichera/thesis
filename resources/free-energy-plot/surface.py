import matplotlib.pyplot as plt
import numpy as np

# Create the mesh in polar coordinates and compute corresponding Z.
T = [0.0, 0.2, 0.4]
u = 1
r = np.linspace(0, 0.6, 50)
p = np.linspace(0, 2*np.pi, 50)
R, P = np.meshgrid(r, p)
fig, axd = plt.subplot_mosaic([T], subplot_kw=dict(projection='3d'))
bottoms = []
tops = []
for t in T:
    ax = axd[t]
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
    ax.plot_wireframe(bigX, bigY, Zero, color='black', rstride=2, cstride=2, linewidth=0.3)
for ax in axd.values():
    ax.set_zlim(min(bottoms), max(tops))
plt.show()
