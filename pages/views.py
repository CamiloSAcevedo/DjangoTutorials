from django.shortcuts import render #here by default
from django.views.generic import TemplateView


# Create your views here.

class HomePageView(TemplateView):
    template_name='pages/home.html'

class AboutPageView(TemplateView):
    template_name='pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title" : "About us - Online Store",
            "subtitle" : "About us",
            "description" : "This is an About page...",
            "author" : "Developed by: Camilo Salazar",
        })
        return context
    
class ContactPageView(TemplateView):
    template_name='pages/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title" : "Contact - Online Store",
            "subtitle" : "Contact",
            "description" : "Contact information: email: cas@OnlineStore.com, phone number: 555 0021365",
            "author" : "Developed by: Camilo Salazar",
        })
        return context
