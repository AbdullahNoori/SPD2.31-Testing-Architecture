def calculate_kinetic_energy(mass, velocity): 
    """Returns kinetic energy of mass [kg] with velocity [ms]."""
    return 0.5 * mass * velocity ** 2

    def test_calculate_kinetic_energy():
        mass = 10 # [kg]
    velocity = 4 # [m/s]
    assert calculate_kinetic_energy(mass, velocity) == 80

    def calculate_kinetic_energy(mass, velocity): 
    """Returns kinetic energy of mass [kg] with velocity [ms]."""
    return mass * velocity ** 2


# test 
    def get_average(li):
        sum = 0
    for num in li:
        sum += num
    mean = sum / len(li)
    return mean