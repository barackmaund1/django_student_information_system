from django.views.generic import ListView, TemplateView
from sis_users.mixins import LoginRequiredMessageMixin
from class_groups.models import ClassGroup
from class_groups.choices import YEAR_CHOICES, BAND_CHOICES, SET_CHOICES

class SchoolView(LoginRequiredMessageMixin, TemplateView):
    template_name = 'class_groups/school_class_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['years'] = YEAR_CHOICES
        context['bands'] = BAND_CHOICES
        context['sets'] = SET_CHOICES
        return context

class YearView(LoginRequiredMessageMixin, ListView):
    template_name = 'class_groups/school_class_page.html.html'

    def get_queryset(self):
        year = self.kwargs['year']
        return ClassGroup.objects.filter(year=year)

class BandView(LoginRequiredMessageMixin, ListView):
    template_name = 'class_groups/base_class_page.html'

    def get_queryset(self):
        year = self.kwargs['year']
        band = self.kwargs['band']
        return ClassGroup.objects.filter(
            year=year,
            band=band
        )

class SetView(LoginRequiredMessageMixin, ListView):
    template_name = 'class_groups/base_class_page.html'

    def get_queryset(self):
        year = self.kwargs['year']
        band = self.kwargs['band']
        set = self.kwargs['set']
        return ClassGroup.objects.filter(
            year=year,
            band=band,
            set=set
        )
