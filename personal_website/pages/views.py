from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page_view(request):
    return HttpResponse("Homepage")

def about_page_view(request):
    context = {"name": "Joshua Ampofo Yentumi",
               "age": 33,
               "hobbies": ["coding", "reading", "gaming"],
               "is_student": True,
               "profile_picture": "https://example.com/profile.jpg",
               "bio": "A passionate developer and lifelong learner."}
    return render(request, "pages/about.html", context)