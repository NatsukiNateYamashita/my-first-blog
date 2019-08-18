from django.db import models
from django.utils import timezone


class Post(models.Model): #models.Model はポストがDjango Modelだという意味で、Djangoが、これはデータベースに保存すべきものだと分かるようにしています。
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #他のモデルへのリンク
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
