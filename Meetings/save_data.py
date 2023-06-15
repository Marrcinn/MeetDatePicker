import datetime
from .models import Pick, Meeting
from . import prepare_data as pData

def save_picks(request, pk):
    try:
        obj = Meeting.objects.get(pk=pk)
        startDate = pData.getStartDate(obj)
        boxes= pData.getBoxes(obj)
        print(startDate)
        print(request.GET)

        for i in range(1, boxes+1):
            try:
                state = request.GET[f'chckBox{i}']
                if state == "on":
                    date = startDate + datetime.timedelta(i-1)
                    pick = Pick(meeting=obj, user=request.GET["userName"], date=date)
                    pick.save()
            except:
                pass
            finally:
                pass        
    # when for example, there is not object with that pk we want to igore that request
    except:
        pass

