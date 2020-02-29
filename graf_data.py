from datetime import datetime, timedelta

import x_graf_data as x
import y_graf_data as y


import sql_data

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

def get_data(start_date, end_date, step, bars):
    graf_data =[]
    x_arr = x.delta_date(start_date, end_date, step)
    x_dotted = list(map(lambda d: d.replace('-', '.'), x_arr))
# Рабочая схема
    y_bars={'y':[], 'b':[]}
    data_row = []
    for b in bars:
        # print("get data for: "+ b)
        bar_row = []
        for d in x_arr:
            br = sql_data.get_y_bar(d, b)
            bar_row.append(br)
            # print('Значение '+str(br)+' за '+d)
        data_row.append(bar_row)
    print(data_row)

    for i in range(len(bars)):
        y_bars = {'x':x_dotted, 'y': data_row[i], 'type': 'bar', 'name': bars[i]}
        # print(y_bars)
        graf_data.append(y_bars)



# не рабочая, для теста
#     for i in bars:
#         # row=x_y_set
#         y_arr = y.do_y_arr(x_arr, bars)
#         x_dotted=list(map(lambda d: d.replace('-', '.'), x_arr))
#         print(x_dotted)
#         row = {'x': x_dotted, 'y': y_arr, 'type': 'bar', 'name': i}
#         # row['name'] = i
#         # print(x_y_set)
#         graf_data.append(row)


    return graf_data