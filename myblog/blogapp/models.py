from django.db import models

# Create your models here.


class blog(models.Model):
    title = models.CharField(max_length=200)
    published = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()

    def summary(self):
        return self.body[:100]

    def pub_date(self):
        return self.published.strftime('%b %e, %Y')

    def __str__(self):
        return self.title
