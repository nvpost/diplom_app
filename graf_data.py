from datetime import datetime, timedelta

import x_graf_data as x
import y_graf_data as y

# Собираем ось X
start_date ="2019-10-01"
end_date = "2019-11-01"
start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
end_date = datetime.strptime(end_date, '%Y-%m-%d').date()


# Собираем ось Y
#
#
# print(x_arr)
# print(y_arr)
d_format = "%Y-%m-%d"

def get_data(start_date, end_date, step):
    graf_data =[]
    x_arr = x.delta_date(start_date, end_date, step)

    bars=['users', 'views', 'page', 'buy']
    for i in bars:
        y_arr = y.do_y_arr(len(x_arr))
        row = {'x': x_arr, 'y': y_arr, 'type': 'bar', 'name': i}
        graf_data.append(row)


    return graf_data