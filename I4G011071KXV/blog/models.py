from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


# Title : A string of maxlength 200, use Django’s models.CharField
# Text : Any amount of text, use Django’s TextField
# Author : A Foreign Key to the current user model. Make use of Django’s get_user_model function.
# Created_date : A date-time column, use Django’s models.DateTimeField.
# Published_date : A date-time column, use Django’s models.DateTimeField.

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title
