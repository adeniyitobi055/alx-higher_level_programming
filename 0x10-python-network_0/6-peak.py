#!/usr/bin/python3
""" 6-peak module """


def find_peak(list_of_integers):
    """ Finds a peak in list_of_integers """

    size = len(list_of_integers)
    middle = size // 2
    mid = size

    if size == 0:
        return None

    while True:
        mid = mid // 2
        if (middle < size - 1 and
                list_of_integers[middle] < list_of_integers[middle + 1]):
            if mid // 2 == 0:
                mid = 2
            middle = middle + mid // 2
        elif (mid > 0 and
                list_of_integers[middle] < list_of_integers[middle - 1]):
            if mid // 2 == 0:
                mid = 2
            middle = middle - mid // 2
        else:
            return list_of_integers[middle]
