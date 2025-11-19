# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 11:14:36 2025

@author: iruch
"""
# nbody_anim.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

def _extract_xy(bodies):
    #Extract (x,y) from your Body objects
    xs, ys = [], []
    for b in bodies:
        if hasattr(b, "rx") and hasattr(b, "ry"):
            xs.append(b.rx); ys.append(b.ry)
        elif hasattr(b, "x") and hasattr(b, "y"):
            xs.append(b.x); ys.append(b.y)
        elif hasattr(b, "pos"):
            xs.append(b.pos[0]); ys.append(b.pos[1])
        else:
            raise ValueError("Body object has no positional attributes.")
    return np.array(xs), np.array(ys)


def animate_simulation(
        bodies,
        step_function,
        frames,
        dt,
        figsize=(6,6),
        interval=30,
        limits=None,
        point_color="white",
        bg="black",
        markersize=4,
        save=None   # "filename.gif" or None
        ):
    

    # Generic animation function for both Direct-Sum and Barnes-Hut simulations.

    # Parameters
    # bodies : list of Body objects
    # step_function : function(bodies, dt) → integrates one timestep
    # frames : # of animation frames
    # dt : timestep forwarded to step_function
    # save : filename.gif (uses PillowWriter)

    fig, ax = plt.subplots(figsize=figsize, facecolor=bg)
    ax.set_facecolor(bg)

    # store energies here
    energy_arr = []

    # Initial positions
    xs, ys = _extract_xy(bodies)
    scat = ax.scatter(xs, ys, s=markersize, c=point_color)

    # Axis limits
    if limits is None:
        m = max(np.max(np.abs(xs)), np.max(np.abs(ys))) * 1.2
        limits = (-m, m, -m, m)

    ax.set_xlim(limits[0], limits[1])
    ax.set_ylim(limits[2], limits[3])

    def update(frame):
        # added the energy return to each animation step
        E = step_function(bodies, dt)
        xs, ys = _extract_xy(bodies)
        
        # adding the energy at this timestep to the total array
        energy_arr.append(E)
        
        #print(xs, ys)
        
        scat.set_offsets(np.column_stack([xs, ys]))
        ax.set_title(f"Timestep {frame}", color = 'white')
        return scat,

    anim = FuncAnimation(
        fig,
        update,
        frames=frames,
        interval=interval,
        blit=True
    )

    if save is not None:
        print(f"Saving GIF → {save}")
        writer = PillowWriter(fps=20)
        anim.save(save, writer=writer)
        print("Saved.")
        plt.close(fig)
    return anim, np.array(energy_arr)
