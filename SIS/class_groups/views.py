from django.views.generic import ListView, TemplateView
from sis_users.mixins import LoginRequiredMessageMixin

class SchoolView(LoginRequiredMessageMixin, TemplateView):
    template_name = 'class_groups/school_class_page.html'

class YearView(LoginRequiredMessageMixin, TemplateView):
    template_name = 'class_groups/year_class_page.html'

class BandView(LoginRequiredMessageMixin, TemplateView):
    template_name = 'class_groups/band_class_page.html'

class SetView(LoginRequiredMessageMixin, ListView):
    template_name = 'class_groups/base_class_page.html'

