from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View


class IndexMain(View):
    def get(self, request):
        context = {
            'title': 'Main'
        }
        return render(request, 'index.html', context)
