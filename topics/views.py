from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
import topics.strings as topic_strings
import resources.strings as common_strings
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
            topics = Topics.objects.all()
            paginator = Paginator(topics, 10)
            page = request.GET.get('page')
            try:
                topics_list = paginator.page(page)
            except PageNotAnInteger:
                topics_list = paginator.page(1)
            except EmptyPage:
                topics_list = paginator.page(paginator.num_pages)
            data['html_list'] = render_to_string('topics/partial_topics_list.html',
                                                          {'topics_list': topics_list, 'topic_strings':topic_strings, 'common_strings':common_strings})
        else:
            data['form_is_valid'] = False
    context = {'form': form, 'topic_strings':topic_strings, 'common_strings':common_strings}
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
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(TopicsList, self).get_context_data(**kwargs)
        topics = Topics.objects.all()
        paginator = Paginator(topics, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            topics_list = paginator.page(page)
        except PageNotAnInteger:
            topics_list = paginator.page(1)
        except EmptyPage:
            topics_list = paginator.page(paginator.num_pages)

        context['topics_list'] = topics_list
        context['common_strings'] = common_strings
        context['topic_strings'] = topic_strings
        return context



def topics_delete(request, pk):
    topics = get_object_or_404(Topics, pk=pk)
    data = dict()
    if request.method == 'POST':
        topics.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        topics = Topics.objects.all()
        paginator = Paginator(topics, 10)
        page = request.GET.get('page')
        try:
            topics_list = paginator.page(page)
        except PageNotAnInteger:
            topics_list = paginator.page(1)
        except EmptyPage:
            topics_list = paginator.page(paginator.num_pages)
        data['html_list'] = render_to_string('topics/partial_topics_list.html', {
            'topics_list': topics_list, 'topic_strings':topic_strings, 'common_strings':common_strings
        })
    else:
        context = {'topics': topics, 'topic_strings':topic_strings, 'common_strings':common_strings}
        data['html_form'] = render_to_string('topics/topics_confirm_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)

def pagination(request):
    data = dict()
    data['form_is_valid'] = True  # This is just to play along with the existing code
    topics = Topics.objects.all()
    paginator = Paginator(topics, 10)
    page = request.GET.get('page')
    try:
        topics_list = paginator.page(page)
    except PageNotAnInteger:
        topics_list = paginator.page(1)
    except EmptyPage:
        topics_list = paginator.page(paginator.num_pages)
    data['html_list'] = render_to_string('topics/partial_topics_list.html', {
        'topics_list': topics_list, 'topic_strings':topic_strings, 'common_strings':common_strings
    })
    return JsonResponse(data)
