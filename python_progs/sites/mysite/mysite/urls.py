"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mysite.views import current_datetime, hours_ahead
import sviaz.views
import books.views


urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^time/$', current_datetime),
	url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^search/$', sviaz.views.search),
    url(r'^object/([\w\W]*)/$', sviaz.views.object_info),
    url(r'^contact/$', books.views.contact),
    url(r'^contact/thanks$', books.views.thanks),
    url(r'^platform/$', sviaz.views.platform_info),
    url(r'^platform/thanks$', sviaz.views.thanks),
]
