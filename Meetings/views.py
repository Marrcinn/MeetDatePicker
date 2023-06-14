from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView
from .models import Meeting

# Create your views here.

# View for creating a Meeting
class MeetingCreateView(CreateView):
    template_name = "meetings/create_meeting.html"
    model = Meeting
    fields = ["name", "passCode"]
    def get(self, request):
        if request.GET:
            print("SUIII")
            return redirect(reverse('meeting_submit', args=[request.GET["name"], request.GET['passCode'] ]))

def newMeetingSubmit(request, name, passCode):
    print("HEEEE")
    meeting = Meeting(name=name, passCode=passCode)
    meeting.save()
    return redirect(reverse('meeting_details', args=[meeting.ID]))

class MeetingDetails(DetailView):
    model = Meeting
    template_name = "meetings/meeting_details.html"
