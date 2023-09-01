from django.db import models


class Director(models.Model):
    first = models.CharField(max_length=128)
    last = models.CharField(max_length=128, blank=True, null=True)
    portrait = models.ImageField(upload_to='portraits/', blank=True, null=True)
    # films

    def __str__(self):
        return self.first + ' ' + self.last

    def actors(self):
        return Actor.objects.filter(films__director__exact=self).distinct().order_by('first')


class Film(models.Model):
    title = models.CharField(max_length=256)
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)
    director = models.ForeignKey('Director', related_name='films', on_delete=models.CASCADE)
    storyline = models.TextField(null=True, blank=True)
    # actors

    def __str__(self):
        return self.title


class Actor(models.Model):
    first = models.CharField(max_length=128)
    last = models.CharField(max_length=128, blank=True, null=True)
    films = models.ManyToManyField(Film, related_name='actors', blank=True)

    def __str__(self):
        return self.first + ' ' + self.last
