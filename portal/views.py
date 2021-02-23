from django.shortcuts import render
from django.views import View
from django.conf import settings


class Dashboard(View):
    template_name = 'portal/dashboard.html'

    def get(self, request):
        return render(request, self.template_name, context={'VGS_URL': settings.VGS_URL})
