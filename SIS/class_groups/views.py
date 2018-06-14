from django.views.generic import ListView, TemplateView, DetailView
from django.conf import settings
from sis_users.mixins import LoginRequiredMessageMixin
from class_groups.models import School, Year, Band, Set

class SchoolView(LoginRequiredMessageMixin, DetailView):
    template_name = 'class_groups/school_page.html'
    model = School

    def get_object(self, queryset=None):
        # get the name of the school defined in settings / environment variable
        return School.objects.get(name=settings.SCHOOL_NAME)

class YearView(LoginRequiredMessageMixin, DetailView):
    template_name = 'class_groups/year_page.html'
    model = Year

    def get_object(self, queryset=None):
        return Year.objects.get(
            value=self.kwargs['year']
        )

class BandView(LoginRequiredMessageMixin, DetailView):
    template_name = 'class_groups/band_page.html'
    model = Band

    def get_object(self, queryset=None):
        return Band.objects.get(
            value=self.kwargs['band'],
            year__value=self.kwargs['year']
        )

class SetView(LoginRequiredMessageMixin, DetailView):
    template_name = 'class_groups/set_page.html'
    model = Set

    def get_object(self, queryset=None):
        return Set.objects.get(
            value=self.kwargs['set'],
            band__value=self.kwargs['band'],
            band__year__value=self.kwargs['year']
        )

