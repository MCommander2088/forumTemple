from django.db import models


# Create your models here.

class Level(models.Model):
    status = models.BooleanField(default=True)

    song_name = models.CharField(max_length=200)
    song_author = models.CharField(max_length=200)

    pub_date = models.DateTimeField('date published')
    level_author = models.CharField(max_length=100)

    dl_link = models.CharField(max_length=250)
    vd_link = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.song_name}-{self.song_author} {self.level_author}"
