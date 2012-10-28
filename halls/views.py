from django.template import Context, loader
from django.http import HttpResponse
from django.db.models import Q
from halls.models import Hall, Hour, FoodItem, MealMenu
from datetime import datetime, timedelta


#
# Display the index page, the list of halls and their open/closed status
#
def index(request):
    d = datetime.now()
    weekday = d.weekday()
    now_hour = d.hour       # put test hour here    example test times: 745, 1249
    now_minute = d.minute   # put test minute here
    #now_hour = 23
    #now_minute = 30
    halls = Hall.objects.all()
    
    # Select hour objects from halls previous day which might still be open
    now_hour_for_yesterday = now_hour + 24
    weekday_for_yesterday = (weekday - 1) % 7
    openFromYesterday = Hour.objects.filter(
        day=weekday_for_yesterday
    ).filter(
        Q(end_hour__gt=now_hour_for_yesterday) | (Q(end_hour=now_hour_for_yesterday) & Q(end_minute__gt=now_minute))
    ).filter(
        Q(start_hour__lt=now_hour_for_yesterday) | (Q(start_hour=now_hour_for_yesterday) & Q(start_minute__lt=now_minute))
    )

    # Select hour objects from current day which are open
    Open = Hour.objects.filter(
        day=weekday
    ).filter(
        Q(end_hour__gt=now_hour) | (Q(end_hour=now_hour) & Q(end_minute__gt=now_minute))
    ).filter(
        Q(start_hour__lt=now_hour) | (Q(start_hour=now_hour) & Q(start_minute__lt=now_minute))
    )
    
    open_from_yesterday_halls = openFromYesterday.values_list('host_hall', flat=True)
    
    Open = openFromYesterday | Open.exclude(host_hall__in=list(open_from_yesterday_halls))
    
    Open = Open.order_by('end_hour','end_minute', 'host_hall__name')
    # values list returns list of tuples of selected values
    # flat makes it a list instead of tuples
    open_halls = Open.values_list('host_hall', flat=True)
    
    #
    # This query block will return the next time that a hall opens on a day.
    #---------
    #filter for blocks of time that haven't ended yet
    Closed = Hour.objects.filter(
        Q(end_hour__gt=now_hour) | (Q(end_hour=now_hour) & Q(end_minute__gt=now_minute))
    ).exclude(
        Q(start_hour__lt=now_hour) | (Q(start_hour=now_hour) & Q(start_minute__lt=now_minute))
    ).filter(
        day=weekday
    ).order_by(
        'host_hall','start_hour','start_minute'
    ).distinct(
        'host_hall'
    ).exclude(
        host_hall__in=list(open_halls)
    )
    
    closed_halls = Closed.values_list('host_hall', flat=True)
    
    closed_for_day = Hall.objects.exclude(id__in=list(closed_halls)).exclude(id__in=list(open_halls))


    
    t = loader.get_template('index.html')
    c = Context({
                'Halls': halls,
                'date': d,
                'day': weekday,
                'nowHr': now_hour,
                'nowMin': now_minute,
                'openHalls': Open,
                'closedHalls': Closed,
                'closedForDay': closed_for_day
                })
    return HttpResponse(t.render(c))


#
# Display the menu for a meal at a hall page
#
def hallmenu(request,hall_name,meal_name,day_num):
    d = datetime.now()
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    meal_dict = { 'BRK': 'Breakfast'
                    , 'BRU': 'Brunch'
                    , 'LUN': 'Lunch'
                    , 'DIN': 'Dinner'
                    , 'LAT': 'Late Night'
                    , 'RET': 'Retail'
    }
    weekday = days[int(day_num)]
    meal_type = meal_dict[meal_name]
    today = datetime.today()

    #get time period from hall+meal+day
    hour_id = Hour.objects.get(host_hall__name=hall_name,meal_type=meal_name,day=day_num).id

    #get distinct food items from this day, assuming the day is now or in the near future
    food_items = FoodItem.objects.filter(
            meal_menu__meal_time__id=hour_id #time matches
    ).filter( 
            meal_menu__date=(today+timedelta((int(day_num)-d.weekday()) % 7)) #date matching
    ).distinct('name')

    meal_type = meal_dict[meal_name]

    t = loader.get_template('hall-menu.html')
    c = Context({
                # lizz: I want the name of the hall... hall with hall_id --> name?? i dont know :(
                # Andrew: added here + template
                'hallName': hall_name,
                'date': d,
                'day': weekday,
                'mealType': meal_type,
                'foodItems': food_items,
                })
    return HttpResponse(t.render(c))