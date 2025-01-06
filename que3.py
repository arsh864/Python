# Function to compute energy using E = mc^2
def compute_energy(mass, speed_of_light=300):
    energy = mass * speed_of_light**2
    return energy

# Taking user input for mass and speed of light
mass = float(input("Enter mass (m) in kg: "))
speed_of_light = float(input("Enter speed of light (c) in m/s (For simplicity, you can use 300): "))

# Compute energy
energy = compute_energy(mass, speed_of_light)
print(f"The energy (E) is: {energy} Joules.")
