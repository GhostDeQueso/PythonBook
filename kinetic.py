def main():
    mass = int(input("Mass in kg: "))
    velocity = int(input("Velocity m per s: "))
    result = kinetic_energy(mass, velocity)
    print(f" KE is {result}")



def kinetic_energy(mass, velocity):
    v = velocity ** 2
    ke = 0.5 * mass * v
    return ke


main()