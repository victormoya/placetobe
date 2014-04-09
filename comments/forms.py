from django import forms
from django.shortcuts import get_object_or_404

from comments.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control area-fixed', 'placeholder': 'Add a comment...',
                                             'rows': '3'}),
        }

    def save(self, user, event, parent, commit=True):

        comment = super(CommentForm, self).save(commit=False)
        comment.publisher = user
        comment.event = event
        if parent:
            comment.parent = get_object_or_404(Comment, pk=parent)
        if commit:
            comment.save()
        return comment