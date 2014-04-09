from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.db import models

UserModel = get_user_model()


class Category(models.Model):

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name


class Event(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    location = models.CharField(max_length=175)
    date = models.DateTimeField()
    category = models.ForeignKey(Category, related_name='events', default='General')
    image = models.ImageField(upload_to='images/event', null=True)
    website = models.CharField(max_length=250, null=True, blank=True)
    publisher = models.ForeignKey(UserModel, related_name='events', null=True)
    confirmed = models.BooleanField(default=False)

    def set_assistant(self, user):
        try:
            instance = Assistant.objects.get(user=user, event=self)
            instance.confirmed = Assistant.YES
            instance.save()
        except ObjectDoesNotExist:
            Assistant.objects.create(event=self, user=user)

    def delete_assistant(self, user):
        try:
            instance = Assistant.objects.get(user=user, event=self)
            instance.confirmed = Assistant.NO
            instance.save()
        except ObjectDoesNotExist:
            Assistant.objects.create(event=self, user=user, confirmed=Assistant.NO)

    @property
    def count_assistant(self):
        return self.assistants.filter(confirmed=Assistant.YES).count()

    @property
    def count_comments(self):
        return self.comments.count()

    def __unicode__(self):
        return self.title


class Assistant(models.Model):

    YES, NO = 1, 0

    OPTIONS = ((YES, 'Yes'),
               (NO, 'No'))

    user = models.ForeignKey(UserModel, related_name='assists')
    event = models.ForeignKey(Event, related_name='assistants')
    confirmed = models.IntegerField(default=YES, choices=OPTIONS)

    class Meta:
        unique_together = ('user', 'event')

    def __unicode__(self):
        return "{}{}".format(self.user.__unicode__(), self.event.__unicode__())

