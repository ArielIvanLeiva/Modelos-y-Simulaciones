from statutils import analysis

# TODO: Complete this test suite
def test_probability_of():
    p = analysis.probability_of([1, 2, 2, 3, 3, 4, 5, 3], lambda x: x == 3)
    assert p == 3 / 8, (
        f"Error calculating probability. Expected {3/8}, received: {p}"
    )
