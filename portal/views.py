from django.shortcuts import render
from django.views import View
from django.conf import settings


class Dashboard(View):
    template_name = 'portal/dashboard.html'

    def get(self, request):
        url = settings.ENDPOINT_URL
        return render(request, self.template_name, context={'url': url})

class Reveal(View):
    template_name = 'portal/reveal.html'

    def get(self, request):
        return render(request, self.template_name, context={})


class TokenizeImage(View):
    template_name = 'portal/tokenize-image.html'

    def get(self, request):
        return render(request, self.template_name, context={})

class Temp(View):
    template_name = 'portal/temp.html'

    def get(self, request):
        return render(request, self.template_name, context={})
