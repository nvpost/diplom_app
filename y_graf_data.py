import random
import sql_data

#Для теста

def do_y_arr(x, bar):
    # sql_data.y_sql_row()
    # print(x)
    # print(bar)
    y_arr_local=[]
    # y_arr_local = ['5', '7']
    for i in range(len(x)):
        y_arr_local.append(random.randint(2, 10))
        # y_data = sql_data.y_sql_row(x, bar)
        # y_arr_local.append(y_data)

    return y_arr_local

