from django.db import models

# Create your models here.
class Player(models.Model):
    tag = models.CharField(max_length=12)
    name = models.CharField(max_length=50)
    expLevel = models.IntegerField()
    trophies = models.IntegerField()
    bestTrophies = models.IntegerField()

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('player', args=[str(self.tag)])
