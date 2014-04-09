from django.db import models
from events.models import Event
from profiles.models import MyUser


class Comment(models.Model):

    DELETED, APPROVED, SPAM = 0, 1, 2

    OPTIONS = ((DELETED, 'Deleted'),
               (APPROVED, 'Approved'),
               (SPAM, 'Spam'))

    publisher = models.ForeignKey(MyUser)
    event = models.ForeignKey(Event, related_name='comments')
    parent = models.ForeignKey('Comment', blank=True, null=True, related_name='replies')
    content = models.TextField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=APPROVED, choices=OPTIONS)

    def is_approved(self):
        return self.status is self.APPROVED

    def vote_like(self, user):
        if Voter.objects.filter(user=user, comment=self).exists():
            # if self.votes.filter(user=user).exists():
            return False
        Voter.objects.create_positive(user=user, comment=self)
        return True

    def vote_dislike(self, user):
        if Voter.objects.filter(user=user, comment=self).exists():
            return False
        Voter.objects.create_negative(user=user, comment=self)
        return True

    @property
    def count_like(self):
        return self.voters.filter(vote=Voter.LIKE).count()

    @property
    def count_dislike(self):
        return self.voters.filter(vote=Voter.DISLIKE).count()

    def __unicode__(self):
        return "{0} post comment {1} on {2}".format(self.publisher.get_short_name(), self.pk, self.event)


class VoterManager(models.Manager):

    def create_positive(self, user, comment):
        return self.create(user=user, comment=comment, vote=Voter.LIKE)

    def create_negative(self, user, comment):
        return self.create(user=user, comment=comment, vote=Voter.DISLIKE)


class Voter(models.Model):

    LIKE, DISLIKE = 1, 0

    user = models.ForeignKey(MyUser, related_name='votes')
    comment = models.ForeignKey(Comment, related_name='voters')
    vote = models.IntegerField()

    objects = VoterManager()

    class Meta:
        unique_together = ('user', 'comment')

    def __unicode__(self):
        return "{0} vote {2} on {1}".format(self.user.get_short_name(), self.comment, self.vote)