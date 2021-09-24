from django.conf.urls import url, include
from . import views

app_name = 'predictor'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^homepage/$', views.home, name='home'),
    url(r'^league/$', views.create_league_form_submit, name='league'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'registration/logout.html'}, name='logout'),
]
