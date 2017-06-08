# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class BiographyPageView(TemplateView):
	template_name ="biography.html"

class ContactPageView(TemplateView):
	template_name ="contact.html"

class PaintingsPageView(TemplateView):
	template_name ="paintings.html"