def swap(array, loc1, loc2):
    tmp = array[loc2]
    array[loc2] = array[loc1]
    array[loc1] = tmp