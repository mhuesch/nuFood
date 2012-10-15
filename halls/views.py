from django.template import Context, loader
from django.http import HttpResponse
from halls.models import Hall
from datetime import datetime

def index(request):
    halls = Hall.objects.all()
    d = datetime.now()
    now_hour = d.hour
    now_minute = d.minute
    #open = Hour.objects.filter(day=now_day)
    #.extra(select={(start_hour*60+start_minute) > (now_hour*60+now_minute)}.distinct('host_hall')
    
    t = loader.get_template('index.html')
    c = Context({
                'Halls': halls,
                })
    return HttpResponse(t.render(c))
#return HttpResponse("Hello, world. You're at the nuFood index.")