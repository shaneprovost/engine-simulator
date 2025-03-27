import numpy as np
import matplotlib.pyplot as plt

def otto_cycle_efficiency(compression_ratio, gamma=1.4):
    """
    Calculate the ideal thermal efficiency of an Otto cycle
    
    Parameters:
    compression_ratio (float): Ratio of maximum to minimum cylinder volume
    gamma (float): Ratio of specific heats (default 1.4 for air)
    
    Returns:
    float: Thermal efficiency (0-1)
    """
    efficiency = 1 - (1 / (compression_ratio ** (gamma - 1)))
    return efficiency

def diesel_cycle_efficiency(compression_ratio, cutoff_ratio, gamma=1.4):
    """
    Calculate the ideal thermal efficiency of a Diesel cycle
    
    Parameters:
    compression_ratio (float): Ratio of maximum to minimum cylinder volume
    cutoff_ratio (float): Ratio of volumes after combustion to before combustion
    gamma (float): Ratio of specific heats (default 1.4 for air)
    
    Returns:
    float: Thermal efficiency (0-1)
    """
    term1 = 1 / (compression_ratio ** (gamma - 1))
    term2 = (cutoff_ratio ** gamma - 1) / (gamma * (cutoff_ratio - 1))
    efficiency = 1 - (term1 * term2)
    return efficiency

def plot_otto_cycle(displacement, compression_ratio, heat_added, gamma=1.4, points=100):
    """
    Plot a P-V diagram for an ideal Otto cycle
    
    Parameters:
    displacement (float): Engine displacement volume (m³)
    compression_ratio (float): Compression ratio
    heat_added (float): Heat added during combustion (J)
    gamma (float): Ratio of specific heats
    points (int): Number of points to plot per stroke
    
    Returns:
    tuple: (figure, axes)
    """
    # Calculate volumes
    max_volume = displacement
    min_volume = displacement / compression_ratio
    
    # Generate array of volumes for each process
    v1 = min_volume  # Bottom of compression
    v2 = max_volume  # Top of intake
    
    # Create arrays for plotting
    volumes = []
    pressures = []
    
    # Starting conditions (reference values)
    p1 = 101325  # Atmospheric pressure (Pa)
    T1 = 298     # Initial temperature (K)
    
    # Process 1-2: Isentropic compression
    v_compression = np.linspace(v2, v1, points)
    p_compression = p1 * (v2 / v_compression) ** gamma
    volumes.extend(v_compression)
    pressures.extend(p_compression)
    
    # Process 2-3: Isochoric heat addition
    p2 = p_compression[-1]
    p3 = p2 * (1 + heat_added / (p2 * v1))  # Simplified approximation
    volumes.append(v1)
    pressures.append(p3)
    
    # Process 3-4: Isentropic expansion
    v_expansion = np.linspace(v1, v2, points)
    p_expansion = p3 * (v1 / v_expansion) ** gamma
    volumes.extend(v_expansion)
    pressures.extend(p_expansion)
    
    # Process 4-1: Isochoric heat rejection (close the cycle)
    volumes.append(v2)
    pressures.append(p1)
    
    # Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(volumes, pressures)
    ax.set_title('P-V Diagram of Otto Cycle')
    ax.set_xlabel('Volume (m³)')
    ax.set_ylabel('Pressure (Pa)')
    ax.grid(True)
    
    # Calculate and display the efficiency
    eff = otto_cycle_efficiency(compression_ratio, gamma)
    ax.text(0.05, 0.95, f'Thermal Efficiency: {eff*100:.1f}%', 
            transform=ax.transAxes, fontsize=12, 
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.5))
    
    plt.show()
    return fig, ax

# Compare efficiencies of Otto and Diesel cycles
def plot_efficiency_comparison(compression_ratios, cutoff_ratios, gamma=1.4):
    """
    Plot efficiency comparison between Otto and Diesel cycles
    
    Parameters:
    compression_ratios (list): Range of compression ratios to compare
    cutoff_ratios (list): List of cutoff ratios for Diesel cycle
    gamma (float): Ratio of specific heats
    """
    plt.figure(figsize=(12, 8))
    
    # Plot Otto cycle efficiency
    otto_efficiencies = [otto_cycle_efficiency(r, gamma) for r in compression_ratios]
    plt.plot(compression_ratios, otto_efficiencies, 'b-', linewidth=2, label='Otto Cycle')
    
    # Plot Diesel cycle efficiencies for different cutoff ratios
    colors = ['r', 'g', 'c', 'm']
    for i, cutoff in enumerate(cutoff_ratios):
        diesel_efficiencies = [diesel_cycle_efficiency(r, cutoff, gamma) for r in compression_ratios]
        plt.plot(compression_ratios, diesel_efficiencies, 
                f'{colors[i%len(colors)]}-', linewidth=2, 
                label=f'Diesel Cycle (cutoff={cutoff})')
    
    plt.xlabel('Compression Ratio')
    plt.ylabel('Thermal Efficiency')
    plt.title('Thermal Efficiency vs. Compression Ratio')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
compression_ratios = np.linspace(4, 20, 50)
cutoff_ratios = [1.5, 2.0, 2.5]
plot_efficiency_comparison(compression_ratios, cutoff_ratios)

# Plot an example Otto cycle
plot_otto_cycle(0.002, 9.5, 1000)