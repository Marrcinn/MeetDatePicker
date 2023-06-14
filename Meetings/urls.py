from django.urls import path
from .views import MeetingCreateView, MeetingDetails

from .views import newMeetingSubmit

urlpatterns = [
        path('create', MeetingCreateView.as_view(), name='create_meeting'),
        path('create/<str:name>/<str:passCode>/<str:startDate>/<str:endDate>', newMeetingSubmit, name='meeting_submit'),        
        path('details/<int:pk>', MeetingDetails.as_view(), name="meeting_details"),
        ]
