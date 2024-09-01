import datetime

def date_to_epoch(date, end=False):
    if date is None: return

    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:])

    if not end: return int(datetime.datetime(year, month, day, 0, 0, 0).timestamp())

    #return int(datetime.datetime(year, month, day+1, 0, 0, 0).timestamp()) -1
    return int(datetime.datetime(year, month, day, hour=23, minute=59, second=59).timestamp())


data = date_to_epoch("20240827")

print(data)