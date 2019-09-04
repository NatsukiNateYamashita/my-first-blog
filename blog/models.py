from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField

class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Photo(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', verbose_name="画像", )
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Post(models.Model): #models.Model はポストがDjango Modelだという意味で、Djangoが、これはデータベースに保存すべきものだと分かるようにしています。
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #他のモデルへのリンク
    tags = models.ManyToManyField(Tag, blank=True)
    main_image = models.ImageField(Photo, upload_to='images/')
    title = models.CharField(max_length=200)
    text = HTMLField("content")
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class MyModel(models.Model):
    content = HTMLField()
