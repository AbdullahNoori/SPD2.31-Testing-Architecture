def calculate_kinetic_energy(mass, velocity): 
    """Returns kinetic energy of mass [kg] with velocity [ms]."""
    return 0.5 * mass * velocity ** 2

    def test_calculate_kinetic_energy():
        mass = 10 # [kg]
    velocity = 4 # [m/s]
    assert calculate_kinetic_energy(mass, velocity) == 80

def test_calculate_kinetic_energy():
    mass = 10 # [kg]
    velocity = 4 # [m/s]
    assert calculate_kinetic_energy(mass, velocity) == 80

# Failing Test below
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


def test_get_average():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # list of numbers
    assert get_average(nums) == 5.5