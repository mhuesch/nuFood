from django.template import Context, loader
from django.http import HttpResponse
from django.db.models import Q
from halls.models import Hall, Hour
from datetime import datetime

def index(request):
    halls = Hall.objects.all()
    d = datetime.now()
    Day = d.weekday()
    now_hour = d.hour       # put test hour here
    now_minute = d.minute   # put test minute here

    
    Open = Hour.objects.filter(
                Q(end_hour__gt=now_hour) | (Q(end_hour=now_hour) & Q(end_minute__gt=now_minute))).filter(
                Q(start_hour__lt=now_hour) | (Q(start_hour=now_hour) & Q(start_minute__lt=now_minute))).filter(
                day=Day)
    
    #lizz's attempt to try to see closed places...
    #Closed = Hour.objects.filter(Q(end_hour__lt=now_hour) | (Q(end_hour=now_hour) & Q(end_minute__lt=now_minute))).filter(Q(start_hour__gt=now_hour) & Q(start_minute__gt=now_minute)).filter(day=Day)
    ##This won't return anything, I don't think. You would be filtering down to time blocks that have already ended, then filtering those to blocks that haven't started yet. This would mean the end time is earlier than the start time for anything that's returned.
    
    
    ##This query block will return the next time that a hall opens on a day.
    #---------
    ##filter for blocks of time that haven't ended yet
    #Closed = Hour.objects.filter(Q(end_hour__gt=now_hour) | (Q(end_hour=now_hour) & Q(end_minute__gt=now_minute)))
    ##filter for blocks of time that also haven't started yet
    #Closed = Closed.exclude(Q(start_hour__lt=now_hour) | (Q(start_hour=now_hour) & Q(start_minute__lt=now_minute))).filter(day=Day)
    ##order by when it starts
    #Closed = Closed.order_by('host_hall','start_hour','start_minute')
    ##choose the first time for each hall
    #Closed = Closed.distinct('host_hall')
    #---------
    
    #Closed = Hall.objects.all()
    
    #.extra(select={(start_hour*60+start_minute) > (now_hour*60+now_minute)}.distinct('host_hall')

    
    t = loader.get_template('index.html')
    c = Context({
                'Halls': halls,
                'date': d,
                'open': Open,
                # 'closed': Closed,
                'day': Day,
                })
    return HttpResponse(t.render(c))
#return HttpResponse("Hello, world. You're at the nuFood index.")