from django.urls import path

from . import views

#here are our app-connections.(these connection just affect to our app, not at entire system)
#each connection going us to a view functionality
#these connections needs to be connect with url root, because that's where the requests come from

urlpatterns = [
    path('', views.index, name='index')
]