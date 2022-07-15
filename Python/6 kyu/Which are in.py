def in_array(array1, array2):
    return sorted(set(elem1 for elem1 in array1 if any(elem1 in elem2 for elem2 in array2)))