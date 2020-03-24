import sys
import time

import numpy as np


def z_plot(x_values, y_values):
    """ Description: Method for plotting a list of values
        Inputs:
            x_values - list_of_values_in_X
            y_values - list_of_values_in_Y
        Outputs:
            - None
    """
    import tkinter
    from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
    from matplotlib.backend_bases import key_press_handler
    from matplotlib.figure import Figure
    root = tkinter.Tk()
    root.wm_title("Embedding in Tk")
    fig = Figure(figsize=(5, 4), dpi=100)
    fig.add_subplot(111).plot(x_values, y_values)
    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    def on_key_press(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, canvas, toolbar)

    canvas.mpl_connect("key_press_event", on_key_press)

    def _quit():
        root.quit()     # stops mainloop
        root.destroy()  # this is necessary on Windows to prevent
        # Fatal Python Error: PyEval_RestoreThread: NULL tstate
    button = tkinter.Button(master=root, text="Quit", command=_quit)
    button.pack(side=tkinter.BOTTOM)
    tkinter.mainloop()
    # If you put root.destroy() here, it will cause an error if the window is
    # closed with the window manager.


# number of x values
nx = 41

# span between the x values
dx = 2/(nx-1)
#print("dx={}".format(dx))

# number of time steps
nt = 25

# amount of time between each step
dt = 0.025

# speed of the wave without changing its shape
c = 1

# creating a vector with all members equal to 1
u = np.ones(nx)
#print("u={}".format(u))

# changing the values of u-vector
wave_start_x = 0.5/dx
#print("wave_start_x={}".format(wave_start_x))
wave_end_x = 1/dx+1
#print("wave_end_x={}".format(wave_end_x))
#
u[int(0.5/dx):int(1/dx+1)] = 2
print("new_u={}".format(u))

# plotting doesn't seem to work without Jupyter
#z_plot(np.linspace(0, 2, nx), u)

# applying the advance in time (1-D Linear Convection equation)
un = np.ones(nx)
#print("un={}".format(un))

for n in range(nt):  # for each time step
    un = u.copy()  # create a duplicate of u
    for i in range(1, nx):  # for each x-value in the current time step
        u[i] = un[i] - c * dt / dx * (un[i] - un[i-1])  # calculate the change of that x value compared to the previous x value at the next time step

print("un={}".format(un))
z_plot(np.linspace(0, 2, nx), un)
#
#print(np.linspace(0, 2, nx))
#print(nx)
#print(help(z_plot))
