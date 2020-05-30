import numpy

def arrays(arr):
    # complete this function
    np = numpy.array(arr, float)
    return (np[::-1])

arr = input().strip().split(' ')