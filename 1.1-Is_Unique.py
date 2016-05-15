def is_Unique(string):

    """Implement an algorithm to determine if a string has all
    unique characters. (This solution assumes that a string with 1 
    character or an empty string is valid and thus contains unique characters.)"""
    
    if len(string) <= 1:
        return True
    identifier = string[0]
    for i in string[1:]:
        if identifier != i:
            return False
        else:
            continue
    return True

