from django.urls import path
from .import views
from .views import export_notices_csv

urlpatterns = [
    path('', views.index, name='index'),
    path('noticeboard/', views.noticeboard, name='noticeboard'),
    path('export/csv/', export_notices_csv, name='export_notices_csv'),
]
