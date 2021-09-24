from django.conf.urls import url, include
from django.contrib import admin
from predictor.views import PlayersView

urlpatterns = [
    url(r'', include('predictor.urls', namespace="predictor")),
    url(r'^api/players/$', PlayersView.as_view(), name='players'),
    url(r'^admin/', admin.site.urls)
]
