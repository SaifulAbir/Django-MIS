from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse, JsonResponse
from .models import Division_name


# Create your views here.

def division_list(request):
    division = Division_name.objects.all()
    context = {
        'division': division
    }
    return render(request, 'division_list.html', context)

def create(request):
    print(request.POST)
    Division = request.GET['Division']

    Division_name_details = Division_name(Division=Division)
    Division_name_details.save()
    return redirect("/division/division_list")


def division_add(request):
    return render(request, 'division_add.html')

# def delete_divison_ajax(request):
#     division_id = request.GET.get('id')
#     division = Division_name.objects.get(pk=division_id)
#     context = {
#         'division': division
#     }
#     return HttpResponse(division.Division)



def delete(request, id):
    division = Division_name.objects.get(pk=id)
    division.delete()
    return redirect('/division/division_list')


def edit(request, id):
    division = Division_name.objects.get(pk=id)
    context = {
        'division': division
    }
    return render(request, 'edit.html', context)


def update_divison_ajax(request):
    division_id = request.GET.get('id')
    division = Division_name.objects.get(pk=division_id)
    context = {
        'division': division
    }
    return HttpResponse(division.Division)
    return render(request, 'ajax-edit.html', context)

def update(request, id):
    division = Division_name.objects.get(pk=id)
    division.Division = request.GET['Division']
    division.save()
    return redirect('/division/division_list')
