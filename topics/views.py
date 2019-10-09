from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from accounts.decorators import admin_login_required
from topics.models import Topics
from .forms import TopicsForm
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from . import models


def save_topics_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            topics_list = Topics.objects.all()
            data['html_topics_list'] = render_to_string('topics/partial_topics_list.html',
                                                          {'topics_list': topics_list})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def topics_create(request):
    data = dict()

    if request.method == 'POST':
        form = TopicsForm(request.POST)
    else:
        form = TopicsForm()
    return save_topics_form(request, form, 'topics/topics_form.html')

def topics_update(request, pk):
    topics = get_object_or_404(Topics, pk=pk)
    if request.method == 'POST':
        form = TopicsForm(request.POST, instance=topics)
    else:
        form = TopicsForm(instance=topics)
    return save_topics_form(request, form, 'topics/topics_update_form.html')

@method_decorator(admin_login_required, name='dispatch')
class TopicsList(LoginRequiredMixin, generic.ListView):
    login_url = '/'
    model = models.Topics



def topics_delete(request, pk):
    topics = get_object_or_404(Topics, pk=pk)
    data = dict()
    if request.method == 'POST':
        topics.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        topics_list = Topics.objects.all()
        data['html_topics_list'] = render_to_string('topics/partial_topics_list.html', {
            'topics_list': topics_list
        })
    else:
        context = {'topics': topics}
        data['html_form'] = render_to_string('topics/topics_confirm_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)
