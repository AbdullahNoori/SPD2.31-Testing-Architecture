
import math, pytest

T_HALF = 5730
DECAY_CONSTANT = -0.693

def is_correct_type_carbon_14_dating(arg):
    return (not isinstance(arg, float) or not isinstance(arg, int))

def is_zero_carbon_14_dating(arg):
    return arg == 0

def is_negative_carbon_14_dating(arg):
    return arg < 0

def get_age_carbon_14_dating(carbon_14_ratio):
    """Returns the estimated age of the sample in year.
    carbon_14_ratio: the percent (0 < percent < 1) of carbon-14 
    in the sample conpared to the amount in living 
    tissue (unitless). 
    """

    if is_zero_carbon_14_dating(carbon_14_ratio):
        raise TypeError('carbon_14_ratio cannot be 0')
    elif is_correct_type_carbon_14_dating(carbon_14_ratio):
        raise TypeError('carbon_14_ratio can only be a float or int')
    elif is_negative_carbon_14_dating(carbon_14_ratio):
        raise TypeError('carbon_14_ratio cannot be negative')
    
    result = math.log(carbon_14_ratio) / DECAY_CONSTANT * T_HALF
    return (math.floor(result*100)/100) # round the number to 2 decimal places


def test_carbon_14_dating():
    with pytest.raises(TypeError):
        assert get_age_carbon_14_dating(0.35) == 8680.34

def test_negative_carbon_14_dating():
    with pytest.raises(TypeError):
        assert get_age_carbon_14_dating(-0.23) == 8680.34

def test_str_carbon_14_dating():
    with pytest.raises(TypeError):
        assert get_age_carbon_14_dating("-0.23") == 8680.34

def test_zero_carbon_14_dating():
    with pytest.raises(TypeError):
        assert get_age_carbon_14_dating(0) == 8680.34



        # TODO: Write a unit test which feed 0.35 to the function. 
# The result should be '8680.34'. Does the function handles 
# every possible input correctly? What if the input is zero
# or negative?
# Add the necessary logic to make sure the function handle 
# every possible input properly. Then write a unit test againt 
# this special case.

# get_age_carbon_14_dating("0.23")
# get_age_carbon_14_dating(0)
# get_age_carbon_14_dating(-0.23)