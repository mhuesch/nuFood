from django.template import Context, loader
from django.http import HttpResponse
from django.db.models import Q
from halls.models import Hall, Hour
from datetime import datetime

def index(request):
    halls = Hall.objects.all()
    d = datetime.now()
    Day = d.weekday()
    now_hour = d.hour       # put test hour here 7 45
    now_minute = d.minute   # put test minute here

    
    Open = Hour.objects.filter(day=Day).filter(Q(end_hour__gt=now_hour) | (Q(end_hour=now_hour) & Q(end_minute__gt=now_minute))).filter(Q(start_hour__lt=now_hour) | (Q(start_hour=now_hour) & Q(start_minute__lt=now_minute)))
    
    # values list returns list of tuples of selected values
    # flat makes it a list instead of tuples
    open_halls = Open.values_list('host_hall', flat=True)
    
    ##This query block will return the next time that a hall opens on a day.
    #---------
    #filter for blocks of time that haven't ended yet
    Closed = Hour.objects.filter(Q(end_hour__gt=now_hour) | (Q(end_hour=now_hour) & Q(end_minute__gt=now_minute)))
    #filter for blocks of time that also haven't started yet
    Closed = Closed.exclude(Q(start_hour__lt=now_hour) | (Q(start_hour=now_hour) & Q(start_minute__lt=now_minute))).filter(day=Day)
    ##order by when it starts
    Closed = Closed.order_by('host_hall','start_hour','start_minute')
    #choose the first time for each hall
    Closed = Closed.distinct('host_hall')
   
    # exclude halls that are currently open 
    Closed = Closed.exclude(host_hall__in=list(open_halls))
    #---------
    


    
    t = loader.get_template('index.html')
    c = Context({
                'Halls': halls,
                'date': d,
                'openHalls': Open,
                'closedHalls': Closed,
                'day': Day,
                'nowMin': now_minute,
                'nowHr': now_hour,
                })
    return HttpResponse(t.render(c))

#return HttpResponse("Hello, world. You're at the nuFood index.")