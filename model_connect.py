from halls.models import Hall, Hour, MealMenu, FoodCategory, FoodAttribute, FoodItem
import json
import calendar
from datetime import date

with open('items.json') as f:
    data = f.read()

read = json.loads(data)

# Map from hall name in JSON data to hall names in database. Use assoc list
hall_dict = { u'1835 Hinman Caf\xe9' : 4 }

# Map from month to month index
mmap = dict((v,k) for k,v in enumerate(calendar.month_abbr))

hours = Hour.objects


for line in read:
    hall_name = line[u'hall']
    day = line[u'name']
    brk = line[u'breakfast']
    lun = line[u'lunch']
    din = line[u'dinner']
    daylist = line[u'absoluteWeek'].split(' ')
    date_month = mmap[(daylist[0][:3])]
    date_day = int(daylist[1].strip(','))
    date_year = int(daylist[2])
    date_obj = date(date_year,date_month,date_day)
    try:
        print hall_dict[hall_name]
    except KeyError:
        pass
    
