import time
from swap import swap

def insertion_sort(array, draw_array):
    sorted_loc = 0
    unsorted_loc = 1
    while unsorted_loc < len(array):
        div = unsorted_loc
        
        draw_array(array, ['white' if x == unsorted_loc else 'red' for x in range(len(array))])
        time.sleep(0.1)
        draw_array(array, ['yellow' if x == unsorted_loc else 'red' for x in range(len(array))])
        time.sleep(0.1)
        draw_array(array, ['white' if x == unsorted_loc else 'red' for x in range(len(array))])
        time.sleep(0.1)
        draw_array(array, ['yellow' if x == unsorted_loc else 'red' for x in range(len(array))])
        time.sleep(0.1)
        
        if array[unsorted_loc] >= array[sorted_loc]:
            draw_array(array, ['orange' if x <= div else 'red' for x in range(len(array))])
            time.sleep(0.8)

        while sorted_loc >= 0 and array[unsorted_loc] < array[sorted_loc]:
            draw_array(array, ['white' if x == unsorted_loc else 'red' for x in range(len(array))])
            time.sleep(0.1)
            draw_array(array, ['yellow' if x == unsorted_loc else 'red' for x in range(len(array))])
            time.sleep(0.1)
            draw_array(array, ['white' if x == unsorted_loc else 'red' for x in range(len(array))])
            time.sleep(0.1)
            draw_array(array, ['yellow' if x == unsorted_loc else 'red' for x in range(len(array))])
            time.sleep(0.1)
            draw_array(array, ['white' if x == unsorted_loc else 'red' for x in range(len(array))])
            time.sleep(0.1)
            draw_array(array, ['yellow' if x == unsorted_loc else 'red' for x in range(len(array))])
            time.sleep(0.1)
            draw_array(array, ['white' if x == unsorted_loc else 'red' for x in range(len(array))])
            time.sleep(0.1)
            draw_array(array, ['yellow' if x == unsorted_loc else 'red' for x in range(len(array))])
            time.sleep(0.1)
            
            swap(array, unsorted_loc, sorted_loc)
            sorted_loc -= 1
            unsorted_loc -= 1

            draw_array(array, ['white' if x == unsorted_loc else 'red' for x in range(len(array))])
            time.sleep(0.1)
            draw_array(array, ['yellow' if x == unsorted_loc else 'red' for x in range(len(array))])
            time.sleep(0.1)
            draw_array(array, ['white' if x == unsorted_loc else 'red' for x in range(len(array))])
            time.sleep(0.1)
            draw_array(array, ['yellow' if x == unsorted_loc else 'red' for x in range(len(array))])
            time.sleep(0.1)
            draw_array(array, ['white' if x == unsorted_loc else 'red' for x in range(len(array))])
            time.sleep(0.1)
            draw_array(array, ['yellow' if x == unsorted_loc else 'red' for x in range(len(array))])
            time.sleep(0.1)
            draw_array(array, ['white' if x == unsorted_loc else 'red' for x in range(len(array))])
            time.sleep(0.1)
            draw_array(array, ['yellow' if x == unsorted_loc else 'red' for x in range(len(array))])
            time.sleep(0.1)

            draw_array(array, ['orange' if x <= div else 'red' for x in range(len(array))])
            time.sleep(0.8)
        
        unsorted_loc = div+1
        sorted_loc = unsorted_loc-1

    draw_array(array, ['blue' for x in range(len(array))])