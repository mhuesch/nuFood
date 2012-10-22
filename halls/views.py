from django.template import Context, loader
from django.http import HttpResponse
from django.db.models import Q
from halls.models import Hall, Hour, FoodItem, MealMenu
from datetime import datetime


def index(request):
    d = datetime.now()
    weekday = d.weekday()
    now_hour = d.hour       # put test hour here    example test times: 745, 1249
    now_minute = d.minute   # put test minute here

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
    
    # values list returns list of tuples of selected values
    # flat makes it a list instead of tuples
    open_halls = Open.values_list('host_hall', flat=True)
    
    ##This query block will return the next time that a hall opens on a day.
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
    


    
    t = loader.get_template('index.html')
    c = Context({
                'Halls': halls,
                'date': d,
                'openHalls': Open,
                'closedHalls': Closed,
                'day': weekday,
                'nowMin': now_minute,
                'nowHr': now_hour,
                })
    return HttpResponse(t.render(c))


#
# Display the menu for a meal at a hall page
#
def hallmenu(request,hall_id):
    d = datetime.now()
    weekday = d.weekday()
    today = d.today()
    
    meal_type = 'DIN'
    
    food_items = FoodItem.objects.filter(meal_menu__meal_time__day=weekday).filter(meal_menu__meal_time__host_hall__id=hall_id).filter(meal_menu__meal_time__meal_type=meal_type).filter(meal_menu__date=today)


    t = loader.get_template('hall-menu.html')
    c = Context({
                # lizz: I want the name of the hall... hall with hall_id --> name?? i dont know :(
                'foodItems': food_items,
                'mealType': meal_type,
                'date': d,
                'day': weekday,
                })
    return HttpResponse(t.render(c))