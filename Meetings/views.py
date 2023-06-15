from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, DetailView
from .models import Meeting, Pick
from . import prepare_data as pData
from .prepare_data import prepareDataForShowingPicks
from .save_data import save_picks
# Create your views here.

# View for creating a Meeting
class MeetingCreateView(TemplateView):
    template_name = "meetings/create_meeting.html"
    def get(self, request):
        if request.GET:
            return redirect(reverse('meeting_submit', args=
                [request.GET["name"], request.GET['passCode'], request.GET['startDate'], request.GET['endDate']]))
        else:
            return super().get(request)


def newMeetingSubmit(request, name, passCode, startDate, endDate):
    meeting = Meeting(name=name, passCode=passCode, startDate=startDate, endDate=endDate)
    meeting.save()
    return redirect(reverse('meeting_details', args=[meeting.ID]))

class MeetingDetails(DetailView):
    model = Meeting
    template_name = "meetings/meeting_details.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["name"] = self.object.name
        context["before"] = pData.getOffset(self.object)
        context["after"] = pData.getTrailingDays(self.object)
        context["data"] = prepareDataForShowingPicks(self.object)
        context['days'] = pData.weekDays()
        return context
    
    def get(self, request, pk):
        if request.GET:
            save_picks(request, pk)
            return redirect(reverse('meeting_details', args=[pk]))
        else:
            return super().get(request)
