import datetime

def timef(datep):
    date = datetime.datetime.strftime(datep, '%B-%Y')
    return date

d = timef(datetime.datetime.now())

print(d)