# uncomment the next line if running in a notebook
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

import time
start_time = time.time()



# mass, spring constant, initial position and velocity
m = 1
k = 1
x = 0
v = 1

# simulation time, timestep and time
t_max = 100
dt = 0.0001
t_array = np.arange(0, t_max, dt)

# initialise empty lists to record trajectories
# Euler integration
def euler(x, v, m, k):
    x_list = []
    v_list = []
    
    for t in t_array:

    # append current state to trajectories
        x_list.append(x)
        v_list.append(v)
    
        # calculate new position and velocity
        a = -k * x / m
        x = x + dt * v
        v = v + dt * a
    
    return [x_list, v_list]


# convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
x_array_e = np.array(euler(x, v, m, k)[0])
v_array_e = np.array(euler(x, v, m, k)[1])

print("--- %s seconds ---" % (time.time() - start_time))

# plot the position-time graph
plt.figure(1)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
plt.plot(t_array, x_array_e, label='x (m)')
plt.plot(t_array, v_array_e, label='v (m/s)')
plt.legend()
plt.show()

#Verlet integration
def verlet(x, v, m, k):
    x_list = []
    v_list = []
    
    for i in range(len(t_array)):
        
        x_list.append(x)
        v_list.append(v)
        
        if i == 0:
            a = -k * x / m
            x = dt
            v = v + dt * a
        else:
            a = -k * x_list[-1] / m
            x = 2*x_list[-1] - x_list[-2] + (dt**2)*a
            v = (x - x_list[-2])/(2*dt)
        
    return [x_list, v_list]

x_array_v = np.array(verlet(x, v, m, k)[0])
v_array_v = np.array(verlet(x, v, m, k)[1])

# plot the position-time graph
plt.figure(1)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
plt.plot(t_array, x_array_v, label='x (m)')
plt.plot(t_array, v_array_v, label='v (m/s)')
plt.legend()
plt.show()