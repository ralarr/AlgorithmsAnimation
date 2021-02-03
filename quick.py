import time
from swap import swap

def quick_sort(array, start, end, draw_array):
    if start < end:
        draw_array(array, ['white' if x == start else 'red' for x in range(len(array))])
        time.sleep(0.1)
        draw_array(array, ['yellow' if x == start else 'red' for x in range(len(array))])
        time.sleep(0.1)
        draw_array(array, ['white' if x == start else 'red' for x in range(len(array))])
        time.sleep(0.1)
        draw_array(array, ['yellow' if x == start else 'red' for x in range(len(array))])
        time.sleep(0.1)

        j = end+1
        for i in range(end, start, -1):
            draw_array(array, ['purple' if x == start else 'white' for x in range(len(array))])
            time.sleep(0.8)
            draw_array(array, ['green' if x == i else 'white' for x in range(len(array))])
            time.sleep(0.8)
            if array[i] > array[start]:
                draw_array(array, ['white' if x == i else 'white' for x in range(len(array))])
                time.sleep(0.1)
                draw_array(array, ['yellow' if x == i else 'white' for x in range(len(array))])
                time.sleep(0.1)
                draw_array(array, ['white' if x == i else 'white' for x in range(len(array))])
                time.sleep(0.1)
                draw_array(array, ['yellow' if x == i else 'white' for x in range(len(array))])
                time.sleep(0.1)
                j -= 1
                swap(array, i, j)

        j -= 1
        swap(array, start, j)
        quick_sort(array, start, j-1, draw_array)
        quick_sort(array, j+1, end, draw_array)

    draw_array(array, ['blue' for x in range(len(array))])
