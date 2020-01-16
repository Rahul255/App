import uuid
from django.utils.translation import gettext as _

from django.conf import settings
from django.db import models

# Create your models here.
from django.urls import reverse

LIST_OF_GOD = (('Krishna', _('Krishna')), ('Ganapathi', _('Ganapathi')), ('Devi', _('Devi')), ('Ayyappa', _('Ayyappa')))


def _(param):
    pass


class Pooja(models.Model):
    pooja = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    # amount=models.CharField(max_length=255)
    god = models.CharField(_('God'), max_length=255, choices=LIST_OF_GOD, blank=False, )
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.pooja

    #def get_absolute_url(self):
       # return reverse('article_detail', args=[str(self.id)])


#def get_absolute_url():
    #return reverse('article_list')


class Comment(models.Model):
    pooja = models.ForeignKey(Pooja, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment


#def get_absolute_url():
    #return reverse('article_list')


class Print(models.Model):
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    poojano = models.CharField(max_length=200, null=True, blank=True, unique=True)
    pooja = models.CharField(max_length=200)
    amount = models.CharField(max_length=200)
    result = models.CharField(max_length=200)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        super(Print, self).__init__()
        self.poojano = str(uuid.uuid4())
