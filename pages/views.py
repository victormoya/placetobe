from django.shortcuts import render
from django.views.generic import View


class LandingView(View):
    template_name = 'landing.html'

    def get(self, request):
        return render (request, self.template_name)