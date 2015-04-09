from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models import Sum

from communityfund.apps.home.templatetags.custom_tags import currency_filter


class DatedModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(DatedModel):
    creator = models.ForeignKey(User, related_name="categories_created")
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=1000)
    subscribers = models.ManyToManyField(User, related_name="subscriptions")

    def get_absolute_url(self):
        return reverse('category', args=[str(self.id)])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Idea(DatedModel):
    initiator = models.ForeignKey(User, related_name="ideas_created")
    category = models.ForeignKey(Category, related_name="ideas")
    name = models.TextField(max_length=100)
    summary = models.TextField(max_length=250)
    description = models.TextField(max_length=20000)

    @property
    def likes(self):
        return self.ratings.filter(positive=True).count()

    @property
    def dislikes(self):
        return self.ratings.filter(positive=False).count()

    def get_absolute_url(self):
        return reverse('idea', args=[str(self.id)])

    def __str__(self):
        return self.name

class IdeaRating(models.Model):
    idea = models.ForeignKey(Idea, related_name="ratings")
    user = models.ForeignKey(User, related_name="idea_ratings")
    positive = models.BooleanField(default=True)

    def __str__(self):
        return '{} {} {}'.format(self.user.username, 'likes' if self.positive else 'dislikes', self.idea.name)
