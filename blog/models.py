from __future__ import unicode_literals

from django.db import models

class blogPost(models.Model):

    title = models.CharField(max_length=150)
    post = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    date_modfied = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return self.title