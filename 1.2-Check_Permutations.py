def check_permutations_sort(str1, str2):

    """ Given 2 strings, check if one string is a permutation of the other."""
    if len(str1) != len(str2):
        return False

    a = ''.join(sorted(str1))
    b = ''.join(sorted(str2))

    if a != b:
        return False
    else:
        return True


def check_permutations_dict(str1, str2):

    """ Given 2 strings, check if one string is a permutation of the other."""

    if len(str1) != len(str2):
        return False

    #Not optimal but correct...first checks if both strings have same length ^^^
  
    str1_dict = {}
    
    for letter in str1:
        str1_dict[letter] = str1_dict.get(letter, 0) + 1
    
    #If both strings have same length, a hashmap is created from the first string
    #where the keys are the letters in the string and the values are the number of
    #times the letter appears in the word

    for letter in str2:
        if letter in str1_dict.keys():
            continue
        if letter not in str1_dict.keys():
            return False

    #Then code checks that each letter in str2 is in str1, if not, breaks out of loop/returns False
            
    str2_dict = {}
       
    for letter in str2:
        str2_dict[letter] = str2_dict.get(letter, 0) + 1
        print str2_dict

    #If str1 and str2 have the same letters another hashmap is created mapping the
    #letters in str2 to the number occurences in the string

    for i in str2_dict.keys():
        if str1_dict[i] != str2_dict[i]:
            return False
        if str1_dict[i] == str2_dict[i]:
            continue

    #By now we know both strings have the same letters and both hashmaps have
    # the same key values. This last part of the code checks that each string
    #has the same number of letters, and thus if str1 is a permutation of str2.
     
            
    return True


