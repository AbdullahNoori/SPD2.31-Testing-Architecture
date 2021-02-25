# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math


def get_distance(xc1=5, xc2=7.25, yc1=22, yc2=-4.84):
    # Calculate the distance between the two circle
    return math.sqrt((xc1-xc2)**2 + (yc1 - yc2)**2)


print('distance', get_distance())


# *** somewhere else in your program ***
def get_length(xa=-50, ya=99, xb=.67, yb=.26):
    # calcualte the length of vector AB vector which is a vector between A and B points.
    return math.sqrt((xa-xb)*(xa-xb) + (ya-yb)*(ya-yb))


print('length', get_length())
