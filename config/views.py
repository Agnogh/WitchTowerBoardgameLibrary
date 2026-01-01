# helper module
# render takes request + tempalte and combines. Then returns html in browser
from django.shortcuts import render

# defining function named 'home' with object 'request'
def home(request):
    return render(request, "base.html")
