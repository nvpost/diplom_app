
import sql
# import secret as secret
# bars = ['users', 'visits', 'buyers']
# def y_sql_row(x, bar):
#     # print(x)
#     # print(bar)
#     query = "select "+', '.join(bars)+" from data where date in('"+"', '".join(x)+"') limit 1"
#     sql.cursor.execute(query)
#     rows = sql.cursor.fetchall()
# def y_set(x, bars):
#     query = "select " + ', '.join(bars) + " from data where date in('" + "', '".join(x) + "')"
#     sql.cursor.execute(query)
#     rows = sql.cursor.fetchall()
#     # print(rows)
#     y_data = []
#     for i in rows:
#         y_data.append(list(i.values()))
#     return y_data
#
# def get_y(d, bars):
#     query = "select " + ', '.join(bars) + " from data where date='"+d+"' limit 1"
#     sql.cursor.execute(query)
#     rows = sql.cursor.fetchall()
#     return(list(rows[0].values()))

def get_y_bar(d, b):
    query = "select " + b + " from data where date='" + d + "' limit 1"
    sql.cursor.execute(query)
    rows = sql.cursor.fetchall()
    # print(list(rows[0].values())[0])
    return (list(rows[0].values())[0])

