from halls.models import FoodAttribute, FoodItem
import json
import calendar
from datetime import date, timedelta

with open('menuitem.json') as f:
    data = f.read()

read = json.loads(data)


attr_dict = { u'w':'Well-Balanced'
            , u'g':'Vegan'
            , u'v':'Vegetarian'
            }

for element in read:
    itemname = element[u'name']

    try:
        fi = FoodItem.objects.filter(name=itemname)[0]

        for key, value in attr_dict.items():
            if element[key]:
                if fi.attributes.filter(name=value):
                    pass
                else:
                    food_attribute = FoodAttribute.objects.get(name=value)
                    fi.attributes.add(food_attribute)

    except IndexError:
        pass

    
