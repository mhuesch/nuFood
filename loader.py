from halls.models import Hall, Hour, MealMenu, FoodAttribute, FoodItem
import json
import calendar
from datetime import date, timedelta

with open('items.json') as f:
    data = f.read()

read = json.loads(data)

# Dictionary mapping from hall name in JSON data to hall ids.
hall_dict = { u'1835 Hinman Caf\xe9' : 4
            , u'Sargent Caf\u00e9' : 7
            , u'Elder Caf\u00e9' : 6
            , u'Foster Walker West Caf\u00e9' : 2
            , u'Foster Walker East Side' : 1
            , u'Willard Caf\u00e9' : 3
            , u'Allison Caf\u00e9' : 5
            }

# Dictionary mappying from day strings to day ids
day_dict = { "monday" : 0
            ,"tuesday" : 1
            ,"wednesday" : 2
            ,"thursday" : 3
            ,"friday" : 4
            ,"saturday" : 5
            ,"sunday" : 6
            }


# Dictionary mapping from month to month index.
month_dict = dict((v,k) for k,v in enumerate(calendar.month_abbr))

# Meal choices
meal_choices = ["BRK","BRU","LUN","DIN","LAT"]

for element in read:
    hall_name = element[u'hall']
    hall_id = hall_dict[hall_name]

    day = element[u'name']
    weekday_index = day_dict[day]

    # FoodItem lists
    food_dict = dict()
    food_dict["BRK"] = element[u'breakfast']
    food_dict["BRU"] = element[u'brunch']
    food_dict["LUN"] = element[u'lunch']
    food_dict["DIN"] = element[u'dinner']
    food_dict["LAT"] = element[u'lateNight']

    # Date
    daylist = element[u'absoluteWeek'].split(' ')
    date_month = month_dict[(daylist[0][:3])]
    date_day = int(daylist[1].strip(','))
    date_year = int(daylist[2])
    date_obj = date(date_year,date_month,date_day)

    # Adjust according to day of week
    date_obj += timedelta(weekday_index)

    for meal in meal_choices:
        food_items = food_dict[meal]


        h = Hour.objects.filter(host_hall_id=hall_id,day=weekday_index,meal_type=meal)

        if h:
            # Create MealMenu object and save
            m = MealMenu(meal_time=h[0],date=date_obj)
            m.save()

            for item in food_items:
                fiList = FoodItem.objects.filter(name=item)

                if fiList:
                    # Get food item from list
                    fi = fiList[0]
                else:
                    # Create new food item
                    fi = FoodItem(name=item)
                    fi.save()

                # Create relation between food item and mealmenu
                fi.meal_menu.add(m)
        
        else:
            # If no meal found, print helpful message
            print "No meal type " + meal + " on day " + weekday_index


    









