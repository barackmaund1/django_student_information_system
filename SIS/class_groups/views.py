from django.views.generic import ListView, TemplateView, DetailView
from django.conf import settings
from sis_users.mixins import LoginRequiredMessageMixin
from class_groups.models import School, Year, Band, Set

class SchoolView(LoginRequiredMessageMixin, DetailView):
    template_name = 'class_groups/school_class_page.html'
    model = School

    def get_object(self, queryset=None):
        # get the name of the school defined in settings / environment variable
        return School.objects.get(name=settings.SCHOOL_NAME)

class YearView(LoginRequiredMessageMixin, DetailView):
    template_name = 'class_groups/year_class_page.html'
    model = Year

    def get_object(self, queryset=None):
        return Year.objects.get(
            value=self.kwargs['year']
        )

class BandView(LoginRequiredMessageMixin, TemplateView):
    template_name = 'class_groups/band_class_page.html'

class SetView(LoginRequiredMessageMixin, ListView):
    template_name = 'class_groups/base_class_page.html'

