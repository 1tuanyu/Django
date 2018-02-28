import datetime
from django.http import Http404, HttpResponse

def hour_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><bdoy>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
