# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)
WELL_DONE = 900000
MEDIUM = 600000
COOKED_CONSTANT = 0.05

def is_cookeding_criteria_satisfied(time, temperature, pressure, desired_state):
    is_well_done = desired_state == 'well-done'
    is_medium = desired_state == 'medium'
    
    cooking = time * temperature * pressure * COOKED_CONSTANT
    
    if is_well_done and cooking >= WELL_DONE: 
        return True
    if is_medium and cooking >= MEDIUM:
        return True
    
    return False
`1234567890p-[=]\
    `
print(is_cookeding_criteria_satisfied(3, 450, 10000, 'medium'))