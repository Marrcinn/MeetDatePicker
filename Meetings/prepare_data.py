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

# Quick function to get number of gray squares to put before
# the startDate
def getOffset(meeting):
    return meeting.startDate.weekday()
# Function to get the number of gray squares after the
# endDate of a given Meeting
def getTrailingDays(meeting):
    return 6-meeting.startDate.weekday()

# Function that returns a list of weekdays
def weekDays():
    return ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def getStartDate(obj):
    return obj.startDate

def getBoxes(obj):
    return int((obj.endDate-obj.startDate).days) + 1