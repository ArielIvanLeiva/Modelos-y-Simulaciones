from statutils import analysis

# TODO: Complete this test suite

# Frecuencies analysis tests
def test_get_frecuencies_all_values():
    sample = [1, 1, 1, 3, 3, 4, 2, 1, 0, 1, 6]

    frecuencies = analysis.get_frecuencies(sample, keys=range(0,6+1))

    assert frecuencies == {0: 1, 1: 5, 2: 1, 3: 2, 4: 1, 5: 0, 6: 1}, (
        "Error calculating frecuencies values."
    )


def test_get_frecuencies_some_values():
    sample = [1, 1, 1, 3, 3, 4, 2, 1, 0, 1, 6]

    frecuencies = analysis.get_frecuencies(sample, keys=range(2,7+1))

    assert frecuencies == {2: 1, 3: 2, 4: 1, 5: 0, 6: 1, 7: 0}, (
        "Error calculating frecuencies values."
    )


def test_get_relative_frecuencies_all_values():
    sample = [1, 1, 1, 3, 3, 4, 2, 1, 0, 1, 6]

    frecuencies = analysis.get_rel_frecuencies(sample, keys=range(0,6+1))

    assert frecuencies == {0: 1/11, 1: 5/11, 2: 1/11, 3: 2/11, 4: 1/11, 5: 0, 6: 1/11}, (
        "Error calculating frecuencies values."
    )


def test_get_relative_frecuencies_some_values():
    sample = [1, 1, 1, 3, 3, 4, 2, 1, 0, 1, 6]

    frecuencies = analysis.get_rel_frecuencies(sample, keys=range(2,7+1))

    assert frecuencies == {2: 1/11, 3: 2/11, 4: 1/11, 5: 0, 6: 1/11, 7: 0}, (
        "Error calculating frecuencies values."
    )


# Probability analysis tests
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