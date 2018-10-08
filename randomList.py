
import random
import time


def new_list():
    temp = []
    for i in range(random.randint(1, 1000)):
        temp.append(random.randint(0, 1000))

    return temp


# I don't use sort and then [-1] because that edits the actual list
def find_max(arg_list=[]):
    temp = arg_list[0]
    pos = 0

    for i in range(len(arg_list)):
        if arg_list[i] > temp:
            temp = arg_list[i]
            pos = i

#   return temp  # Not as important
    return pos


def my_sort(arg_list=[]):

    result = []
    while len(arg_list) > 0:
        pos = find_max(arg_list)
        result.insert(0, arg_list.pop(pos))

    return result


def insert(arg_list=[]):

    for i in range(len(arg_list)):
        for j in range(i):
            if arg_list[i] < arg_list[j]:
                temp = arg_list[i]
                arg_list[i] = arg_list[j]
                arg_list[j] = temp

    return arg_list


def selection(arg_list=[]):

    for i in range(len(arg_list)):
        k = i

        for j in range(i+1, len(arg_list)):
            if arg_list[j]<arg_list[k]:
                k = j

        arg_list[i], arg_list[k] = arg_list[k], arg_list[i]

    return arg_list


def bubble(arg_list=[]):

    for i in range(len(arg_list)):
        swapped = False
        for j in range(len(arg_list) -1, i, -1):
            if arg_list[j] < arg_list[j-1]:
                arg_list[j], arg_list[j-1] = arg_list[j-1], arg_list[j]
                swapped = True

        if not swapped:
            break

    return arg_list


def partition(arg_list, first, pivot):

    q = j = first

    while j < pivot:
        if arg_list[j] <= arg_list[pivot]:
            arg_list[q], arg_list[j] = arg_list[j], arg_list[q]
            q += 1
        j += 1

    arg_list[q], arg_list[pivot] = arg_list[pivot], arg_list[q]
    return q


def quick(arg_list, first, pivot):

    if pivot <= first:
        return

    q = partition(arg_list, first, pivot)
    quick(arg_list, first, q-1)
    quick(arg_list, q+1, pivot)

    return arg_list


my_list = new_list()
# my_list = [360, 433, 720, 840, 126, 380]  # For testing purposes
print(my_list)
# I tried to measure the time elapsed as well as possible
# surprisingly when I measure the time elapsed twice the answer is different (always faster second time)
# slightly better if i change the result variable
# the longer the array, the more consistent the times

start_time = time.clock()
result = my_sort(my_list.copy())
total_time = time.clock() - start_time
print(result, "-", total_time, "seconds - my_sort")

start_time = time.clock()
result1 = insert(my_list.copy())
total_time = time.clock() - start_time
print(result1, "-", total_time, "seconds - insert")

start_time = time.clock()
result2 = insert(my_list.copy())
total_time = time.clock() - start_time
print(result2, "-", total_time, "seconds - insert")

start_time = time.clock()
result2 = selection(my_list.copy())
total_time = time.clock() - start_time
print(result2, "-", total_time, "seconds - selection")

start_time = time.clock()
result3 = bubble(my_list.copy())
total_time = time.clock() - start_time
print(result3, "-", total_time, "seconds - bubble")

start_time = time.clock()
result3 = quick(my_list.copy(), 0, len(my_list)-1)
total_time = time.clock() - start_time
print(result3, "-", total_time, "seconds - quick")
