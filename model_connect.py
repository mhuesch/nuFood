from halls.models import Hall, Hour, MealMenu, FoodCategory, FoodAttribute, FoodItem
import json
import calendar
from datetime import date

with open('items.json') as f:
    data = f.read()

read = json.loads(data)

# Dictionary mapping from hall name in JSON data to hall ids.
hall_dict = { u'1835 Hinman Caf\xe9' : 4
            , u'Sargent Caf\u00e9' : 7
            , u'Elder Caf\u00e9' : 6
            , u'Foster Walker West Caf\u00e9' : 2
            , u'Foster Walker East Caf\u00e9' : 1
            , u'Willard Caf\u00e9' : 3
            , u'Allison Caf\u00e9' : 5
            }

# Dictionary mapping from month to month index.
month_dict = dict((v,k) for k,v in enumerate(calendar.month_abbr))



hours = Hour.objects


for element in read:
    hall_name = element[u'hall']
    day = element[u'name']
    brk = element[u'breakfast']
    lun = element[u'lunch']
    din = element[u'dinner']
    daylist = element[u'absoluteWeek'].split(' ')
    date_month = month_dict[(daylist[0][:3])]
    date_day = int(daylist[1].strip(','))
    date_year = int(daylist[2])
    date_obj = date(date_year,date_month,date_day)
    try:
        print hall_dict[hall_name]
        print date_month
    except KeyError:
        pass
    
