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


for element in read:
    hall_name = element[u'hall']
    day = element[u'name']
    brk = element[u'breakfast']
    lun = element[u'lunch']
    din = element[u'dinner']
    daylist = element[u'absoluteWeek'].split(' ')
    date_month = mmap[(daylist[0][:3])]
    date_day = int(daylist[1].strip(','))
    date_year = int(daylist[2])
    date_obj = date(date_year,date_month,date_day)
    try:
        print hall_dict[hall_name]
        print date_month
    except KeyError:
        pass
    
