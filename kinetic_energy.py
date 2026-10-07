def kinetic_energy(mass,velocity):
  mass = float(input("Enter mass in kilograms:"))
  velocity = float(input("Enter velocity in meters per second:"))
  KE = 0.5 * mass * velocity ** 2

total_energy = kinetic_energy(mass,velocity)
print(f" The objects kinetic energy is {total_energy) joules.")
