from django.db import models


class Stories(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=2083)
    selfpost = models.BooleanField(default=False)
    selfpost_text = models.TextField(default="", null=True)
    poll = models.BooleanField(default=False)
    dead = models.BooleanField(default=False)
    username = models.CharField(max_length=150, null=True)
    score = models.PositiveIntegerField(max_length=5)
    comments = models.PositiveIntegerField(max_length=5)
    story_type = models.CharField(max_length=30, default='news')
    time = models.DateTimeField()
    cache = models.DateTimeField(null=True)


class HNComments(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    story_id = models.PositiveIntegerField(max_length=10, default=0, null=True)
    username = models.CharField(max_length=150)
    text = models.TextField(default="")
    hiddenpercent = models.PositiveIntegerField(max_length=10, default=0)
    hiddencolor = models.CharField(max_length=7, default="#000000")
    time = models.DateTimeField(null=True)
    cache = models.DateTimeField(null=True)
    parent = models.ForeignKey('self', related_name='children', null=True, db_index=True)
    dead = models.BooleanField(default=False)

    class Meta:
        ordering = ['dead', 'cache']


class StoryCache(models.Model):
    name = models.CharField(max_length=30)
    time = models.DateTimeField(null=True)
    over = models.IntegerField(null=True)


# Not really used anymore
class HNCommentsCache(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    time = models.DateTimeField(null=True, auto_now=True)


class UserInfo(models.Model):
    username = models.CharField(max_length=150, primary_key=True)
    created = models.DateTimeField()
    karma = models.IntegerField(null=True, default=1)
    avg = models.DecimalField(null=True, default=None, max_digits=20, decimal_places=2)
    about = models.TextField(default="", null=True)
    cache = models.DateTimeField(auto_now_add=True, null=True)


class Poll(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=1000)
    score = models.PositiveIntegerField(max_length=5)
    story_id = models.PositiveIntegerField(max_length=10, default=0, null=True)
