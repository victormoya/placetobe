from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic import View
from comments.forms import CommentForm
from comments.models import Comment
from events.models import Event


class PostCommentView(View):

    template_name = 'events/detail.html'
    form_class = CommentForm

    def post(self, request, event_id, comment_id=None):
        if not request.user.is_authenticated():
            messages.error(request, 'Need to be logged')
            return redirect(reverse('profiles:login'))
        form = self.form_class(request.POST)
        event = get_object_or_404(Event, pk=event_id)
        comments = event.comments.filter(parent__isnull=True)
        data = {
            'event': event,
            'form_comments': form,
            'list_comments': comments,
        }
        if form.is_valid():
            form.save(user=request.user, event=event, parent=comment_id)
            messages.success(request, 'Comment has been posted')
            return redirect(reverse('events:detail', args=(event_id,)))
        messages.error(request, 'Ops! Some errors detected')
        return render(request, self.template_name, data)


class VotePositiveView(View):

    @staticmethod
    def get(request, comment_id):
        if not request.user.is_authenticated():
            messages.error(request, 'Need to be logged')
            return redirect(reverse('profiles:login'))
        user = request.user
        comment = Comment.objects.get(pk=comment_id)
        event = comment.event_id
        if comment:
            comment.vote_like(user)
        return redirect(reverse('events:detail', args=(event,)))


class VoteNegativeView(View):

    @staticmethod
    def get(request, comment_id):
        if not request.user.is_authenticated():
            messages.error(request, 'Need to be logged')
            return redirect(reverse('profiles:login'))
        user = request.user
        comment = Comment.objects.get(pk=comment_id)
        event = comment.event_id
        if comment:
            comment.vote_dislike(user)
        return redirect(reverse('events:detail', args=(event,)))


class SortByLikesView(View):

    template_name = 'events/detail.html'
    form_class = CommentForm

    def get(self, request, event_id):
        event = get_object_or_404(Event, pk=event_id)
        form = self.form_class()
        comments = event.comments.all().filter(parent__isnull=True)
        sorted_comments = sorted(comments, key=lambda x: x.count_like, reverse=True)

        data = {
            'event': event,
            'form_comments': form,
            'list_comments': sorted_comments,
        }
        return render(request, self.template_name, data)