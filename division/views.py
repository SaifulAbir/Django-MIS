from django.shortcuts import render, redirect, HttpResponse

from .models import Division_name


# Create your views here.

def index(request):
    # division = Division_name.objects.all()
    # context = {
    #     'division': division
    # }
    return render(request, 'division_list.html')


def create(request):
    print(request.POST)
    Division = request.GET['Division']

    Division_name_details = Division_name(Division=Division)
    Division_name_details.save()
    return redirect('/division_add')


def division_add(request):
    return render(request, 'division_add.html')


def delete(request, id):
    division = Division_name.objects.get(pk=id)
    division.delete()
    return redirect('/division_add')


def edit(request,):
    # division = Division_name.objects.get(pk=id)
    # context = {
    #     'division': division
    # }
    return render(request, 'division_edit.html')


def update(request, id):
    division = Division_name.objects.get(pk=id)
    division.Division = request.GET['Division']

    division.save()
    return redirect('/division_add')