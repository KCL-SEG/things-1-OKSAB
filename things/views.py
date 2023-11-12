from django.shortcuts import render

# Create your views here.

from .models import Thing

def home(request):
    # Query all Thing objects
    things = Thing.objects.all()
    # Pass them to the context
    context = {'things': things}
    return render(request, 'home.html', context)


