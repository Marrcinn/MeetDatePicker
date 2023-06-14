from django.db import models

# Create your models here.

# Model for meeting
class Meeting(models.Model):
    ID = models.AutoField(primary_key=True)
    passCode = models.CharField(max_length=32)
    name = models.TextField()

# Model representin user's pick - note that user should not be able
# To make two picks with overlaping Hours on one meeting.
class Pick(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    user = models.TextField()
    date = models.DateTimeField()
