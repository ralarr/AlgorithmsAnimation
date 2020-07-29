import time
from swap import swap

def selection_sort(array, draw_array):
    curr_loc = 0
    min_loc = 0
    i = 1
    while curr_loc < len(array):
        while i < len(array):
            draw_array(array, ['orange' if x == min_loc else 'red' for x in range(len(array))])
            time.sleep(0.5)
            draw_array(array, ['black' if x == i or x == min_loc else 'red' for x in range(len(array))])
            time.sleep(0.3)

            if array[i] < array[min_loc]:
                draw_array(array, ['white' if x == i else 'red' for x in range(len(array))])
                time.sleep(0.1)
                draw_array(array, ['yellow' if x == i else 'red' for x in range(len(array))])
                time.sleep(0.1)
                draw_array(array, ['white' if x == i else 'red' for x in range(len(array))])
                time.sleep(0.1)
                draw_array(array, ['yellow' if x == i else 'red' for x in range(len(array))])
                time.sleep(0.1)
                draw_array(array, ['white' if x == i else 'red' for x in range(len(array))])
                time.sleep(0.1)
                draw_array(array, ['yellow' if x == i else 'red' for x in range(len(array))])
                time.sleep(0.1)
                draw_array(array, ['white' if x == i else 'red' for x in range(len(array))])
                time.sleep(0.1)
                draw_array(array, ['yellow' if x == i else 'red' for x in range(len(array))])
                time.sleep(0.1)

                min_loc = i
            i += 1

        if min_loc != curr_loc:
            draw_array(array, ['purple' if x == min_loc or x == curr_loc else 'red' for x in range(len(array))])
            time.sleep(1.5)
            swap(array, curr_loc, min_loc)
            draw_array(array, ['purple' if x == min_loc or x == curr_loc else 'red' for x in range(len(array))])
            time.sleep(1.5)

        curr_loc += 1
        i = curr_loc+1
        min_loc = curr_loc
        
    draw_array(array, ['blue' for x in range(len(array))])