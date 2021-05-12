from django.urls import path

from . import views

#here are our app-connections.(these connection just affect to our app, not at entire system)
#each connection going us to a view functionality
#these connections needs to be connect with url root, because that's where the requests come from


app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/result/', views.ResultView.as_view(), name='result'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    
] 