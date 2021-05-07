from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='main'),
    path('query1', views.query1, name='query1'),
    path('query2', views.query2, name='query2'),
    path('query3', views.query3, name='query3'),
    path('query4', views.query4, name='query4'),
    path('query5', views.query5, name='query5'),
    path('app_history', views.app_history, name='app_history'),
    path('treat_history', views.treat_history, name='treat_history'),
    path('report1', views.report1, name='report1'),
    path('report2', views.report2, name='report2'),
]
