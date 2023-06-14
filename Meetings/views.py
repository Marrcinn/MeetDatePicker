from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, DetailView
from .models import Meeting
# Create your views here.

# View for creating a Meeting
class MeetingCreateView(TemplateView):
    template_name = "meetings/create_meeting.html"
    def get(self, request):
        if request.GET:
            print("SUIII")
            return redirect(reverse('meeting_submit', args=
                [request.GET["name"], request.GET['passCode'], request.GET['startDate'], request.GET['endDate']]))
        else:
            return super().get(request)


def newMeetingSubmit(request, name, passCode, startDate, endDate):
    print("HEEEE")
    meeting = Meeting(name=name, passCode=passCode, startDate=startDate, endDate=endDate)
    meeting.save()
    return redirect(reverse('meeting_details', args=[meeting.ID]))

class MeetingDetails(DetailView):
    model = Meeting
    template_name = "meetings/meeting_details.html"
