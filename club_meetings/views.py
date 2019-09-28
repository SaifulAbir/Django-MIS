from django.shortcuts import render
from .forms import ClubMeetingForms


# Create your views here.
def showform(request):
    form= ClubMeetingForms(request.POST)
    if form.is_valid():
        form.save()

    context={"form":form}

    return render(request,'club_meetings/create_meeeting.htm',context)
