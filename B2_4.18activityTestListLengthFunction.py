# implementing a function to test list_length()

def list_length(a_list):
    """Retur the length of a list."""
    length = 0
    for item in a_list:
        length = length + 1
    return length

def test_list_length():
    """Test the list_length() function"""
    assert list_length([]) == 0
    assert list_length([1]) == 1
    assert list_length([1, 1]) == 2
    assert list_length([1, 1, 3]) == 3

test_list_length()
    
