import numpy as np
import matplotlib.pyplot as plt

def calculate_internal_energy_change(heat_added, work_done):
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

def ideal_gas_pressure(volume, moles, temperature, R=8.314):
    """
    Calculate pressure using the ideal gas law
    
    Parameters:
    volume (float): Volume (m³)
    moles (float): Number of moles of gas
    temperature (float): Temperature (K)
    R (float): Universal gas constant (J/(mol·K))
    
    Returns:
    float: Pressure (Pa)
    """
    pressure = (moles * R * temperature) / volume
    return pressure

# Example: Calculate pressure at different volumes (simple P-V diagram)
def plot_pv_diagram_isothermal(initial_volume, final_volume, moles, temperature, points=100):
    """
    Plot a P-V diagram for an isothermal process
    """
    volumes = np.linspace(initial_volume, final_volume, points)
    pressures = [ideal_gas_pressure(v, moles, temperature) for v in volumes]
    
    plt.figure(figsize=(10, 6))
    plt.plot(volumes, pressures)
    plt.title('P-V Diagram for Isothermal Process')
    plt.xlabel('Volume (m³)')
    plt.ylabel('Pressure (Pa)')
    plt.grid(True)
    plt.show()
    
    # Calculate work done (area under the curve)
    work = moles * 8.314 * temperature * np.log(final_volume / initial_volume)
    print(f"Work done by the gas: {work:.2f} J")
    
    return work

# Example usage
plot_pv_diagram_isothermal(0.001, 0.002, 0.1, 500)