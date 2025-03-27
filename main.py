from therm.index import calculate_internal_energy_change, ideal_gas_pressure

d_u = calculate_internal_energy_change(500, 300)

print(d_u)

volume_high = ideal_gas_pressure(5, 2, 300)
volume_low = ideal_gas_pressure(2, 2, 300)

print(volume_high, volume_low)
