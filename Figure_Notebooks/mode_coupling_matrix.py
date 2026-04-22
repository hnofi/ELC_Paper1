# Script by Graeme Addison

import numpy as np
import scipy as sp
import healpy as hp

# This file computes the mode-coupling matrix used to correct for
# mask-induced mode coupling in pseudo-Cl power spectrum estimates,
# following Hivon et al. (2002).

def approx_log_factorial(n):
    # This is a 'beyond Stirling' approximation for large n
    # NB does not include factor of sqrt(2*pi)
    
    # Coefficients for high order correction beyond Stirling
    C = np.array([1., 1./24, 3./80., 18029./45360., 6272051./14869008.])
    
    # Shifted variable
    N = n + 0.5
    
    # Approximation to improve accuracy
    A = N**2 / (N + C[1] / (N + C[2] / (N + C[3] / N)))
    return N * (np.log(A) - 1)

def vec_wigner3j_zeros(j1, j2, j3):
    # Compute Wigner 3j symbols
    J = j1 + j2 + j3
    n = np.array([J-2*j1, J-2*j2, J-2*j3, J/2, J+1, J/2-j1, J/2-j2, J/2-j3]).astype(int)
    #print(n)
    # Weights for combining log-factorials
    w = np.array([1, 1, 1, 2, -1, -2, -2, -2])
    return np.exp(np.sum(w[:,None] * log_fact_arr[n], axis=0))

def compute_mode_coupling_matrix_from_mask(mask):
    # Compute mode-coupling matrix from sky mask
    # Based on MASTER method (Hivon et al. 2002).
    global log_fact_arr
    
    nside = hp.npix2nside(len(mask))
    lmax = 3*nside-1
    
    # Maximum factorial needed for Wigner 3j 
    factorial_max = 4*lmax+1
    
    # Threshold for computation
    calc_factorial_max = 170  # maximum we can hold as float / max you can calculate with sp.misc.factorial
    
    log_fact_arr = np.empty(factorial_max+1, dtype='float64')
    log_fact_arr[:calc_factorial_max+1] = np.log(sp.special.factorial(np.arange(calc_factorial_max+1)))
    log_fact_arr[calc_factorial_max+1:factorial_max+1] = approx_log_factorial(np.arange(calc_factorial_max+1, factorial_max+1)) + 0.5 * np.log(2*np.pi)
    
    # Power spectrum of the mask
    cl_mask_pad = np.zeros(2*lmax+1)
    cl_mask_pad[:3*nside] = hp.anafast(mask)  #, use_pixel_weights=True, datapath=WEIGHTS_PATH)
    
    # Mode-coupling matrix
    mode_matrix = np.zeros([lmax+1, lmax+1])
    
    # Loop over multipoles 1 & 2
    for l_1 in range(lmax+1):
        for l_2 in range(l_1, lmax+1):
            l_3_min = abs(l_1 - l_2)
            l_3_max = l_1 + l_2
            l_3 = np.arange(l_3_min, l_3_max+1, 2)
            
            # MASTER formula
            mode_matrix[l_1, l_2] = (2 * l_2 + 1) * 0.25 * np.sum((2 * l_3 + 1) * cl_mask_pad[l_3] * vec_wigner3j_zeros(l_1, l_2, l_3)) /np.pi
            if l_1 != l_2:
                mode_matrix[l_2, l_1] = (2. * l_1 + 1.)*mode_matrix[l_1, l_2]/(2. * l_2 + 1.)
    
    return mode_matrix
    