# uncomment the next line if running in a notebook
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

# mass, spring constant, initial position and velocity
G = 6.673e-11
M = 6.42e23
pos = np.array([4e6, 0.0, 0.0])
vel = np.array([0.0, -3272.638844, 0.0])

# simulation time, timestep and time
t_max = 8000
dt = 10e-2
t_array = np.arange(0, t_max, dt)

# initialise empty lists to record trajectories
# Euler integration
def euler(x, v):
    x_list = []
    v_list = []
    
    for i in range(len(t_array)):
        #create empty list
        xz = []
        vz = []
        #append initial value
        if i == 0:
            for j in range(len(x)):
                xz.append(x[j])
                vz.append(v[j]) 
            
            x_list.append(xz)
            v_list.append(vz)
            xz = []
            vz = []
            
        x_magnitude = np.sqrt(x.dot(x))
        # calculate new position and velocity
        for k in range(len(x)):
            a = -(G*M/((x_magnitude)**3))*(x[k])
            x[k] = x[k] + dt*v[k]
            v[k] = v[k] + dt*a
            xz.append(x[k])
            vz.append(v[k])
        
        #to ignore final list
        if i == len(t_array)-1:
            continue
        else:
            x_list.append(xz)
            v_list.append(vz)
            
    return [x_list, v_list]

# convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
result_e = euler(pos, vel)
pos_array_e = np.array(result_e[0])

def plott(array, label):
    plt.figure(1)
    plt.clf()
    plt.grid()
    plt.plot(array[:, 0], array[:, 1], label=label)
    plt.legend()
    plt.show()   

#plot euler results   
plott(pos_array_e, "euler")

pos = np.array([4e6, 0.0, 0.0])
vel = np.array([0.0, -3272.638844, 0.0])
#Verlet integration
def verlet(x, v):
    x_list = []
    v_list = []
    
    for i in range(len(t_array)):
        xz = []
        vz = []
        
        if i == 0:
            for j in range(len(x)):
                xz.append(x[j])
                vz.append(v[j])
                
            x_list.append(xz)
            v_list.append(vz)     
            xz = []
            vz = []
            
        x_magnitude = np.sqrt(x.dot(x))
        if i == 0:
            for k in range(len(x)):
                a = -(G*M/((x_magnitude)**3))*(x[k])
                x[k] = x[k] + dt * v[k]
                v[k] = v[k] + dt * a
                xz.append(x[k])
                vz.append(v[k])      
        else:
            for k in range(len(x)):
                a = -(G*M/((x_magnitude)**3))*(x[k])
                x[k] = 2*x_list[-1][k] - x_list[-2][k] + (dt**2)*a
                v[k] = (x[k] - x_list[-2][k])/(2*dt)
                xz.append(x[k])
                vz.append(v[k])
                
        if i == len(t_array)-1:
            continue
        else:
            x_list.append(xz)
            v_list.append(vz)
            
    return [x_list, v_list]

result_v = verlet(pos, vel)
pos_array_v = np.array(result_v[0])

# plot verlet results
plott(pos_array_v, "verlet")
