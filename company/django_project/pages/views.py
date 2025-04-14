from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def home_page_view(request):
    context = {
        "inventory_list": ["Widget 1", "Widget 2", "Widget 3"],
        "greeting": "THAnk you FOR vistING",
    }
    return render(request, "home.html", context)

class AboutPageView(TemplateView):
    template_name = "about.html"
    
    def get_context_data(self, **kwargs): # recommended approach for updating  the template context
        context = super().get_context_data(**kwargs)
        context['contact_address'] = "B2461/4 Tsatsu Street"
        context['phone_number'] = "555-555-555"
        return context