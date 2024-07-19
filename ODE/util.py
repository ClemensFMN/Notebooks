import numpy as np
import matplotlib.pyplot as plt
import scipy as sci
import scipy.integrate as int
import scipy.linalg as lin
import matplotlib as mpl
mpl.rcParams['figure.figsize'] = (7,7)


def solveODE(dX_dt, y0, tstart, tstop):
    t  = np.linspace(tstart, tstop, 1000)
    X, infodict = int.odeint(dX_dt, y0, t, full_output=True)
    return(X, infodict)

def vField(xmin, xmax, ymin, ymax, dX_dt, Norm):
    x = np.linspace(xmin, xmax, 20)
    y = np.linspace(ymin, ymax, 20)

    X1 , Y1  = np.meshgrid(x, y)                    # create a grid
    DX1, DY1 = dX_dt([X1, Y1])                      # compute derivative on grid

    if Norm == True:
        M = (np.hypot(DX1, DY1))                           # Norm of the growth rate 
        M[ M == 0] = 1.                                 # Avoid zero division errors 
        DX1 /= M                                        # Normalize each arrows
        DY1 /= M

    
    #-------------------------------------------------------
    # Drow direction fields, using matplotlib 's quiver function
    plt.title('Trajectories and direction fields')
    Q = plt.quiver(X1, Y1, DX1, DY1, color="C0")
    plt.xlabel('y_1')
    plt.ylabel('y_2')
    plt.grid()

