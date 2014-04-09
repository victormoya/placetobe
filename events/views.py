import datetime
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Event
from .forms import EventForm
from comments.forms import CommentForm
from profiles.models import MyUser
from search.engine import SearchEngine


class EventList(View):
    template_name = "events/list.html"

    def get(self, request):
        event_list = Event.objects.filter(confirmed=True).filter(date__gt=datetime.datetime.now()).order_by('date')
        paginator = Paginator(event_list, 4)

        page = request.GET.get('page')
        try:
            events = paginator.page(page)
        except PageNotAnInteger:
            events = paginator.page(1)
        except EmptyPage:
            events = paginator.page(paginator.num_pages)

        data = {
            'events': events
        }
        return render(request, self.template_name, data)


class EventSuggestedView(View):
    template_name = "events/suggested_list.html"

    def get(self, request):

        user = MyUser.objects.get(username=request.user)
        interest_list = user.get_interest_list()
        event_list = Event.objects.filter(category__name__in=interest_list)
        paginator = Paginator(event_list, 4)

        page = request.GET.get('page')
        try:
            event_list = paginator.page(page)
        except PageNotAnInteger:
            event_list = paginator.page(1)
        except EmptyPage:
            event_list = paginator.page(paginator.num_pages)

        data = {
            'events': event_list,
            'interest_list': interest_list,
        }
        return render(request, self.template_name, data)


class EventDetailView(View):
    template_name = 'events/detail.html'
    form_class = CommentForm

    def get(self, request, event_id):
        event = get_object_or_404(Event, pk=event_id)
        form = self.form_class()
        comments = event.comments.filter(parent__isnull=True)

        data = {
            'event': event,
            'form_comments': form,
            'list_comments': comments,
        }
        return render(request, self.template_name, data)


class PublishEventView(View):
    template_name = 'events/form.html'
    form_class = EventForm

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            messages.error(request, 'You need to be logged in to publish a new event')
            return redirect(reverse('profiles:login'))
        return super(PublishEventView, self).dispatch(request, *args, **kwargs)

    @method_decorator(login_required)
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'event_form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save(user=request.user)
            messages.success(request, 'Event has been sent')
            return redirect(reverse('events:list'))
        messages.error(request, 'Ops! Some errors detected')
        return render(request, self.template_name, {'event_form': form})


class AddAssistantView(View):
    @staticmethod
    def get(request, event_id):
        user = request.user
        event = Event.objects.get(pk=event_id)
        if event:
            event.set_assistant(user)
            messages.success(request, 'Attend to the event confirmed')
            return redirect(reverse('events:detail', args=(event_id,)))
        messages.error(request, "Attend don't confirmed")
        return redirect(reverse('events:detail', args=(event_id,)))


class RemoveAssistantView(View):
    @staticmethod
    def get(request, event_id):
        user = request.user
        event = Event.objects.get(pk=event_id)
        if event:
            event.delete_assistant(user)
            messages.info(request, 'You will not go to the event')
            return redirect(reverse('events:detail', args=(event_id,)))
        messages.error(request, "Ops")
        return redirect(reverse('events:detail', args=(event_id,)))



