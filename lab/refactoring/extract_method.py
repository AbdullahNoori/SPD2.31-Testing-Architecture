"""Written by Kamran Bigdely.
Example for Compose Methods: Extract Method."""
import math 


def user_input(n_students):
    """Prompt the user to input the grades for n students.

    Args:
        n_students: int. Number of grades to input.

    Returns: a list of floating point values
    """
    gradeList = []
    total = 0
    # Get the inputs from the user
    for _ in range(0, n_students):
        user_input = int(input('Enter a number: '))
        gradeList.append(user_input)
        total += user_input
    
    return gradeList, total


def compute_stats(gradeList, mean):
    """Compute and return the mean and standard deviation of the grades.

    Args:
        grade_list: List[float]. A list of numerical grade values.
    
    Returns: a Tuple[float] of the mean and standard deviation.
    """
    # Calculate the mean and standard deviation of the grades
    # mean = sum(gradeList) / len(gradeList, mean)
    # sd = 0 # standard deviation
    sum_of_sqrs = 0
    for grade in gradeList:
        sum_of_sqrs += (grade - mean) ** 2
 
    return math.sqrt(sum_of_sqrs / len(gradeList))


def print_stat():
    """Display the mean and standard deviation for the class.
    
    Args:
        n_students: int. The number of students in the class.

    Returns: None.
    """
    # get the grades
    gradeList, total = user_input(3)
    # compute mean and standard deviation
    mean = total / len(gradeList)
    # return the calculated sd 
    sd = compute_stats(gradeList, mean)
    # print out the mean and standard deviation in a nice format.
    print("****** Grade Statistics ******")
    print(f"The grades's mean is: {mean}")
    print('The population standard deviation of grades is: ', round(sd, 3))
    print("****** END ******")


if __name__ == "__name__":
    n_students = 7
print_stat()


