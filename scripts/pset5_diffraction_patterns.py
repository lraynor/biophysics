# -*- coding: utf-8 -*-
"""
Author:     Lynne Raynor
Created:    Tue Oct 29 17:10:09 2019

Description:    Investigation of single slit diffraction in the wide, narrow,
                and intermediate cases. PDF found using probability amplitude
                derived in from "From Photon to Neuron" by Philip Nelson, 
                equations 4.18 to 4.20
-----------
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sci

plt.close('all')

#part a
def square(x): 
    return x*x

re, im = sci.quad(square, 0, 1)
print(re)

#part b
plt.figure('part b')
def find_diffraction_pattern(m_value): 
    x_vals = np.linspace(0, 4000, 100)
    psi2 = np.zeros(len(x_vals))
    M = m_value
    ctr = 0
    for x in x_vals: 
        #split the integrand into real and imaginary parts using the Euler formula
        def single_slit_re(u): 
            return np.cos((M**2)*(u - x)**2)
        def single_slit_im(u): 
            return np.sin((M**2)*(u - x)**2)
        #integrate each part
        re_value, error = sci.quad(single_slit_re, -0.5, 0.5, limit=100)
        im_value, error = sci.quad(single_slit_im, -0.5, 0.5, limit=100)
        #take the modulus of the full complex answer
        psi2[ctr] = np.abs(complex(re_value, im_value))**2
        ctr += 1
    

    PDF = psi2 / (np.sum(psi2) * (x_vals[1] - x_vals[0]) * 2)
    plt.plot(x_vals, PDF)
    axes = plt.gca()
    axes.set_title('PDF for single slit  with M = {:.3f}'.format(m_value))
    #axes are unitless
    axes.set_xlabel('x/W')
    axes.set_ylabel('probability density')
    
find_diffraction_pattern(12)

#part c
plt.figure('part c, M = 2')
find_diffraction_pattern(2)
plt.figure('part c, M = 0.5')
find_diffraction_pattern(0.5)
axes = plt.gca()
axes.set_ylim(0, 1)
#plt.close('all')

plt.figure('part d')
#part d
def find_M(W, d, lamda): 
    return W / (d * lamda / np.pi)**0.5

M = find_M(0.1E-3, 5, 600E-9)
print('M = {}'.format(M))
find_diffraction_pattern(M)
axes = plt.gca()
print('range = {}'.format(20E-2 / .05E-3))
axes.set_xlim(0, (250))
axes.set_ylim(0, (.01))