from django.urls import path
from .views import MeetingCreateView, MeetingDetails, AccessMeetingView

from .views import newMeetingSubmit

urlpatterns = [
        path('create', MeetingCreateView.as_view(), name='create_meeting'),
        path('access', AccessMeetingView.as_view(), name='meeting_access'),
        path('create/<str:name>/<str:passCode>/<str:startDate>/<str:endDate>', newMeetingSubmit, name='meeting_submit'),        
        path('details/<int:pk>', MeetingDetails.as_view(), name="meeting_details"),
        ]
