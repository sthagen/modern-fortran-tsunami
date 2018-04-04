"""
plot_1d_time_steps.py

Reads output of tsunami and plots the results in an image file,
one image file per time step.
"""
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='text file output by tsunami simulator')
args = parser.parse_args()

input_file = args.input_file

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

dt = 0.02

# read data into a list
data = [line.rstrip().split() for line in open(input_file).readlines()]

time = [float(line[0]) for line in data[::2]]
u1 = [[float(x) for x in line[2:]] for line in data[::2]]
u2 = [[float(x) for x in line[2:]] for line in data[1::2]]

x1 = np.arange(1, len(u1[0])+1).tolist()
x2 = np.arange(x1[-1]+1, x1[-1]+len(u1[0])+1).tolist()

for n in range(len(time)):
    print('plotting time step ', n)
    fig = plt.figure(figsize=(8,3))
    ax = fig.add_axes((0.12, 0.2, 0.8, 0.7))
    ax.tick_params(axis='both', which='major', labelsize=16)
    plt.ylim(-0.2,1.2)
    plt.xlim(1,100)
    plt.xticks(range(25,125,25))
    plt.yticks(np.arange(-0.2, 1.4, 0.2))
    #x = np.arange(1,101)
    plt.plot(x1+x2, u1[n]+u2[n], 'b-')
    #plt.fill_between(x, -0.5, u[n], color='b', alpha=0.4)
    plt.grid(True)
    plt.xlabel('Distance [m]',fontsize=16)
    plt.ylabel('Height [m]',fontsize=16)
    plt.title(r'Water elevation [m], time = '+'%5.1f' % (n*dt)+' s', fontsize=16)
    plt.savefig('h_'+'%4.4i' % n+'.png',dpi=100)
    plt.close(fig)
