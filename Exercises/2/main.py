import os
import numpy as np
import matplotlib.pyplot as plt

file_path = "data/input.txt"
file = open(file_path)
data = file.readlines()
for i in range(len(data)):
    line = data[i]
    line = line.replace(" ", "")
    line = line.replace("\n", "")
    line = line.split(",")
    data[i] = line

try: 
    nDay = int(data[0][0])
    P_start = [[float(y) for y in x] for x in data[1:3]]
    P_start = np.array(P_start)
    P = [[float(y) for y in x] for x in data[3:]]
    P = np.array(P)    
except:
    print("\n [Error:] Wrong input in \"" + file_path + "\" file !!!")
    exit()

print("\nAfter reading \"" + file_path + "\" file: ")
print("Number of days: ", nDay)
print("P start:\n", P_start)
print("P:\n", P)

P_happyDays = np.zeros((2, nDay))
P_sadDays = np.zeros((2, nDay))
P_happyDays[:,0]= P_start[:,0]
P_sadDays[:,0] = P_start[:,1]

P_happy = np.array([P_start[:,0]])
P_sad = np.array([P_start[:,1]])

for day in range(1, nDay):
    P_start = np.dot(P_start, P)
    P_happyDays[:,day] = np.dot(P_happy, P_start)
    P_sadDays[:,day] = np.dot(P_sad, P_start)

fig, axes = plt.subplots(1,2,figsize=(9, 4.5))  
axes[0].plot(range(nDay), P_happyDays[0,:], label="Happy")
axes[0].plot(range(nDay), P_happyDays[1,:], label="Sad")
axes[0].set_title("P(0)="+str(P_happy)+"^T")
axes[0].legend()

axes[1].plot(range(nDay), P_sadDays[0,:], label="Happy")
axes[1].plot(range(nDay), P_sadDays[1,:], label="Sad")
axes[1].set_title("P(0)="+str(P_sad)+"^T")
axes[1].legend()

for ax in axes.flat:
    ax.set(xlabel='Days', ylabel='P')
    ax.label_outer()

plt.tight_layout()
plt.show()

