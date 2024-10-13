from django.shortcuts import render
from .models import Event

def event_list(request):
    events = Event.objects.all()
    print("Events fetched from database:", events)  # Debug statement
    return render(request, 'event/event_list.html', {'events': events})
