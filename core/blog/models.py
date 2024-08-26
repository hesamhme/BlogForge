from django.db import models

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=25)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey('Catgory', on_delete=models.SET_NULL, null=False)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField()

    def __str__(self):
        return self.title

class Ctegory(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

