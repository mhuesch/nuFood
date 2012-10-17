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
    #Open = Hour.objects.filter(day=Day).filter(end_hour__gt=now_hour).filter(start_hour__lt=now_hour) | Hour.objects.filter(day=Day).filter(end_hour=now_hour).filter(end_minute__gt=now_minute)
    
    
    
    Open = Hour.objects.filter(Q(end_hour__gt=now_hour) | (Q(end_hour=now_hour) & Q(end_minute__gt=now_minute))).filter(Q(start_hour__lt=now_hour) | (Q(start_hour=now_hour) & Q(start_minute__lt=now_minute))).filter(day=Day)
    
    #lizz's attempt to try to see closed places...
    #Closed = Hour.objects.filter(Q(end_hour__lt=now_hour) | (Q(end_hour=now_hour) & Q(end_minute__lt=now_minute))).filter(Q(start_hour__gt=now_hour) & Q(start_minute__gt=now_minute)).filter(day=Day)
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