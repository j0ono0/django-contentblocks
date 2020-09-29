from django.shortcuts import render
from django.views import View
from .models import ContentBlock

class IndexView(View):
    def get(self, request):
        context = {}
        return render(request, "contentblocks/index.html", context)