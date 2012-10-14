from django.template import Context, loader
from django.http import HttpResponse
from halls.models import Hall
from datetime import datetime

def index(request):
    halls = Hall.objects.all()
    d = datetime.now()
    t = loader.get_template('index.html')
    c = Context({
                'Halls': halls,
                'date': d
                })
    return HttpResponse(t.render(c))
#return HttpResponse("Hello, world. You're at the nuFood index.")