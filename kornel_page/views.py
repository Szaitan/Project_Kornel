from django.shortcuts import render
from django.views import View

# Create your views here.


class CoverPageView(View):
    def get(self, request):
        return render(request, "kornel_page/cover.html")

