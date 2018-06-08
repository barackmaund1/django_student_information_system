from django.views.generic import ListView
from sis_users.mixins import LoginRequiredMessageMixin
from class_groups.models import ClassGroup

class YearView(LoginRequiredMessageMixin, ListView):
    def get_queryset(self):
        year = self.kwargs['year']
        return ClassGroup.objects.filter(year=year)

class BandView(LoginRequiredMessageMixin, ListView):
    def get_queryset(self):
        year = self.kwargs['year']
        band = self.kwargs['band']
        return ClassGroup.objects.filter(
            year=year,
            band=band
        )

class SetView(LoginRequiredMessageMixin, ListView):
    def get_queryset(self):
        year = self.kwargs['year']
        band = self.kwargs['band']
        set = self.kwargs['set']
        return ClassGroup.objects.filter(
            year=year,
            band=band,
            set=set
        )
