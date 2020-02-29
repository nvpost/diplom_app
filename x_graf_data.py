from datetime import datetime, timedelta

start_date = datetime.strptime("2019-10-01", '%Y-%m-%d').date()
end_date = datetime.strptime("2019-11-01", '%Y-%m-%d').date()
d_format = "%Y-%m-%d"

delta_date_ar=[]
def delta_date(start_date, end_date, step=1):
    deltadays = round((end_date - start_date).days/step)
    nd = start_date
    for i in range(deltadays):
        delta_date_ar.append(nd.strftime(d_format))
        nd = nd + timedelta(days=1)
    return(delta_date_ar)


