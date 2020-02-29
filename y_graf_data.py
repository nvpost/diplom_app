import random



def do_y_arr(l):
    y_arr_local = []
    for i in range(l):
        y_arr_local.append(random.randint(2, 10))
    return y_arr_local