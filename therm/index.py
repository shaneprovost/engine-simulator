import numpy as np
import matplotlib.pyplot as plt

def calculate_internal_energy_change(heat_added, work_done) -> float:
    """
    Calculate change in internal energy using First Law of Thermodynamics
    
    Parameters:
    heat_added (float): Heat added to the system (J)
    work_done (float): Work done by the system (J)
    
    Returns:
    float: Change in internal energy (J)
    """
    delta_u = heat_added - work_done
    return delta_u

def ideal_gas_pressure(volume, moles, temperature, Z = 1.0) -> float:
    """
    Calculate pressure of an ideal gas using the ideal gas law
    
    Parameters:
    volume (float): Volume of the gas (L)
    moles (float): Amount of gas (mol)
    temperature (float): Temperature of the gas (K)
    Z (float): Compressibility factor (default 1.0)
    
    Returns:
    float: Pressure of the gas (Pa)
    """
    R = 8.314
    pressure = (Z * moles * R * temperature) / volume
    return pressure