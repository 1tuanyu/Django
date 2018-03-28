from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(u'标题', max_length=100)
    pub_date = models.DateTimeField(u'发布日期', auto_now_add=True)
    lable = models.CharField(u'标签', max_length=30, blank=True)
    content = models.TextField(u'正文', null=True)

    def __str__(self):
        return self.title
