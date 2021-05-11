from django.urls import path

from . import views

#here are our app-connections.(these connection just affect to our app, not at entire system)
#each connection going us to a view functionality
#these connections needs to be connect with url root, because that's where the requests come from


app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('specifics/<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/result/', views.result, name='result'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    
] 