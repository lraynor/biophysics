# -*- coding: utf-8 -*-
"""
Author:     Lynne Raynor
Created:    Tue Nov 19 20:49:17 2019

Description:    Using the method described in "From Photon to Neuron" 
                by Philip Nelson, we show how diffraction patterns
                can be used to reconstruct physical structures. Using
                DNA as the scattering object, we first project the helix
                onto the uv-plane and use the resulting sine curve as 
                a set of scattering points. We then show the 
                probability amplitude on a far detection screen can 
                be used to infer the structure of DNA.
-----------
"""
import numpy as np
import matplotlib.pyplot as plt

plt.close('all')

helical_pitch = 10.5
base_length = .34E-9
Nobject = int(14 * helical_pitch)

def find_v (u): 
    return np.sin (2*np.pi*u/(10.5 * .34E-9)) * 1E-9

us = np.arange(0, Nobject * base_length, base_length)
vs = find_v(us)
plt.figure('part a')
plt.plot(us, vs)
axes_a = plt.gca()
axes_a.set_xlabel('u [m]')
axes_a.set_ylabel('v [m]')
axes_a.set_title('part a: scattering points in the uv-plane')

plt.figure('part a points')
plt.plot(us, vs, 'bo')
axes_a = plt.gca()
axes_a.set_xlabel('u [m]')
axes_a.set_ylabel('v [m]')
axes_a.set_title('part a: scattering points in the uv-plane')


#part b
lamba = .05E-9
scale = lamba / base_length

screen = np.linspace(-scale, scale, 200) # x/d values to consider
xs, ys = np.meshgrid(screen, screen)
xs = xs.reshape([200, 200, 1])
ys = ys.reshape([200, 200, 1])
us = us.reshape([1, 1, Nobject])
vs = vs.reshape([1,1,Nobject])
phases = np.exp(-2j*np.pi*(xs*us + ys*vs)/lamba)
prob_ampl = np.sum(phases, axis=2)


#part c
psi_2 = (abs(prob_ampl))**2
plt.figure('part c')
im = plt.imshow(psi_2.transpose(), origin = 'lower', cmap='hot', extent = [-.147, .147, -.147, .147])
axes_c = plt.gca()
axes_c.set_xlabel('x/d')
axes_c.set_ylabel('y/d')
axes_c.set_title('part c: heatmap of psi^2 as a function of x/d, y/d')
