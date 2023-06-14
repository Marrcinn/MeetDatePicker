from .models import Pick, Meeting
from datetime import timedelta

# This file is for scripts to help prepare data.
# Those scripts are not in places they are going to be used
# i.e. views.py to preserve readability of those files
# and have only necessary code in them 
# (because I feel they are cluttered otherwise :))


# We are returning range of dates from startDate to endDate EXCLUSIVELY
def dateRange(startDate, endDate):
    for n in range(int((endDate-startDate).days)):
        yield startDate+timedelta(n)

def prepareDataForShowingPicks(meeting):
    res = {}
    for date in dateRange(meeting.startDate, meeting.endDate+timedelta(1)):
        res[date] = Pick.objects.filter(date__date=date).filter(meeting=meeting).count()
    return res
