#from django.http import HttpResponse,Http404
#from django.template.loader import get_template
#from django.template import Context 用render_to_response节省了导入模版的麻烦
from django.shortcuts import render_to_response
import datetime

def hello(request):
    return HttpResponse('hello world!')

def current_datetime(request):
    now = datetime.datetime.now()
    #t = get_template('current_datetime.html')
    #html = t.render(Context({'current_date':now}))
    return render_to_response('current_datetime.html', {'current_date':now})

def hour_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><bdoy>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
