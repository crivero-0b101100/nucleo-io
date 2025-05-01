def reverse_list(input_list):
    """
    Reverses a list and returns a new list with the reversed elements.
    
    Args:
        input_list: The list to be reversed
        
    Returns:
        A new list with elements in reverse order
        
    Raises:
        TypeError: If input is not a list
    """
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")
    return input_list[::-1]