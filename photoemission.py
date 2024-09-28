import matplotlib.pyplot as plt
import scipy.constants as const
import numpy as np

# Constants
h = const.Planck                         # Planck's constant
c = const.c                              # Speed of light
electron_charge = const.electron_volt    # Charge of electron

def EnergyOfPhoton(frequency=None, wavelength=None):
    if frequency is not None:
        return h * frequency
    elif wavelength is not None:
        return h * c / wavelength
    else:
        raise ValueError("Either frequency (f) or wavelength (λ) must be provided.")

def Photoemission(frequency=None, thresholdf=None, workfunction=None):
    if frequency is None:
        raise ValueError("No frequency provided to compare with threshold frequency")
    
    E_photon = EnergyOfPhoton(frequency=frequency)
    
    if workfunction is None:
        raise ValueError("Work function must be provided.")

    if E_photon > workfunction:
        print("Photoemission will occur.")
    else:
        print("Photoemission will not occur.")

    if workfunction and frequency:
        return (h*frequency - workfunction)
    
# Parameters
ray_power = 8 # Watts
frequency = 6.80e14 # Hertz
workfunction = 3.70e-19 # Joules

E_photon = EnergyOfPhoton(frequency)
Ek = Photoemission(frequency=frequency, workfunction=workfunction)

n = ray_power/E_photon # no of emitted electrons per second (for current)

frequencies = np.linspace(0, frequency, 100)
energies = EnergyOfPhoton(frequency=frequencies)

# Energy vs Frequency
plt.subplot(1, 2, 1)
plt.plot(frequencies, energies)
plt.title('Energy vs Frequency')
plt.xlabel("Frequency (Hz)")
plt.ylabel("Energy (J)")
plt.grid()

# Maximum Kinetic Energy vs Frequency
if Ek > 0:
    Ek_values = np.array([Photoemission(f, workfunction=workfunction) for f in frequencies])
    plt.subplot(1, 2, 2)
    plt.plot(frequencies, Ek_values)
    plt.title('Kinetic Energy vs Frequency')
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Max Kinetic Energy (J)")
    plt.grid()

plt.tight_layout()
plt.show()
