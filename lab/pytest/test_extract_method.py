import pytest, math
from extract_method import calculate_stat

def test_calculate_stats():
    grades = [10, 20, 5, 0, 15]
    result = (10.0, 7.071)
    
    mean, sd = calculate_stat(grades)
    
    assert (mean, round(sd, 3)) == result
    
def test_negative_grades():
    grades = [-10, 20, -5, 0, 15]
    result = (10.0, 7.071)
    
    with pytest.raises(TypeError):
        mean, sd = calculate_stat(grades)
        assert (mean, round(sd, 3)) == result
        
def test_wrong_type_grades():
    grades = ["-10", "20", "-5", "0", "15"]
    result = (10.0, 7.071)
    
    with pytest.raises(TypeError):
        mean, sd = calculate_stat(grades)
        assert (mean, round(sd, 3)) == result