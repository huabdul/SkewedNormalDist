import numpy as np
from scipy.special import erf

class SkewedNormalDist():
    def __init__(self, mode=0, std=1, alpha=0):
        self.mode = mode
        self.std = std
        self.alpha = alpha
        
        delta = alpha / np.sqrt(1 + alpha**2) 
        gamma1 = ((4 - np.pi) / 2) * (delta * np.sqrt(2/np.pi))**3 / (1 - 2*delta**2 / np.pi)**(3/2)
        
        muz = np.sqrt(2/np.pi) * delta
        sigmaz = np.sqrt(1 - muz**2)
        
        mo = muz - gamma1*sigmaz/2 - np.sign(alpha)*0.5*np.exp(-2*np.pi/np.abs(alpha)) if alpha != 0 else muz
        
        self.offset = std*mo
        
    def normpdf(self, x):
        return (1/np.sqrt(2*np.pi)) * np.exp(-0.5*x**2)
    def normcdf(self, x):
        return 0.5*(1 + erf(x / np.sqrt(2)))
        
    def pdf(self, x):
        mode = self.mode
        std = self.std
        alpha = self.alpha
        offset = self.offset
        
        y = 0.5*std * self.normpdf((x - mode + offset)/std) * self.normcdf(alpha*(x - mode + offset)/std)
        
        return y