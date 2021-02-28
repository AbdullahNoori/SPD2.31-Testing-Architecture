# by Kami Bigdely
# Extract class
WELL_DONE = 3000
MEDIUM = 2500
COOKED_CONSTANT = 0.05

cooking_criteria = "time","temp", "pressure", "desired_state"

def is_cookeding_criteria_satisfied(cooking_criteria):
    return is_well_done(cooking_criteria) or \
           is_medium(cooking_criteria)


def is_well_done(cooking_criteria):    
    return desired_state == 'well-done' and  \
           get_cooking_progress(time, temp, pressure) >= WELL_DONE


def is_medium(cooking_criteria):
    return desired_state == 'medium' and  \
           get_cooking_progress(time, temp, pressure) >= MEDIUM

def get_cooking_progress(time, temp, pressure):
    return time * temp * pressure * COOKED_CONSTANT


time = 30 # [min]
temp = 103 # [celcius]
pressure = 20 # [psi]
desired_state = 'well-done'

if is_cookeding_criteria_satisfied(cooking_criteria):
    print('cooking is done.')
else:
    print('ongoing cooking.')