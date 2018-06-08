from django.urls import path
from class_groups.views import SchoolView, YearView, BandView, SetView

app_name = 'class_groups'

urlpatterns = [
    path('', SchoolView.as_view(), name='school-view'),
    path('<year>/', YearView.as_view(), name='year-view'),
    path('<year>/<band>/', BandView.as_view(), name='band-view'),
    path('<year>/<band>/<set>', SetView.as_view(), name='set-view')
]