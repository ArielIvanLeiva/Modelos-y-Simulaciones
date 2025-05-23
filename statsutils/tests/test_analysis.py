from statutils import analysis

# TODO: Complete this test suite
def test_probability_of():
    p = analysis.probability_of([1, 2, 2, 3, 3, 4, 5, 3], lambda x: x == 3)
    expected_value = 3/8
    
    assert p == expected_value, (
        f"Error calculating probability. Expected {expected_value}, received: {p}"
    )


def test_get_ic_confidence():
    ics = [(0,1), (0.2, 1.2), (-0.2, 0.8), (-0.1, 1.1)]
    real_value = 0.9
    
    confidence = analysis.get_ic_confidence(ics, real_value)
    expected_value = 3/4

    assert confidence == expected_value, (
        f"Error estimating confidence. Expected {expected_value}, received: {confidence}"
    )
    
