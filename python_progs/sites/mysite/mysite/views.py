from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Template, Context
from django.http import HttpResponse


import datetime

def current_datetime(request):
    #now = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" % now

    #fp = open('./mysite/templates/mytemplate.html')
    #t = Template(fp.read())
    #fp.close()

    #t = get_template('mytemplate.html')
    #html = t.render(Context({'current_date': now}))
    #return HttpResponse(html)
    #return render_to_response('mytemplate.html', {'current_date': now})

    current_date = datetime.datetime.now()
    return render_to_response('current_datetime.html', locals())

def hours_ahead(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body> In %s hour(s), it will be %s.</body></html>" %(offset, dt)
    return HttpResponse(html)


#def admin_home(request):
#    site_title = 'My test site'
#    return render_to_response('admin/base_site.html', {'site_title': site_title})
