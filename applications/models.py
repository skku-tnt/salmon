from django.db import models

#superuser id:salmon pw:salmon
  

class Mynote(models.Model):
    auther     = models.CharField('작성자', max_length=16, null=False)
    class_id = models.CharField('강의아이디', max_length=16, null=False)
    title      = models.CharField('제목', max_length=126, null=False)
    keyword1   = models.CharField('키워드1', max_length=12, null=True)
    keyword2   = models.CharField('키워드2', max_length=12, null=True)
    keyword3   = models.CharField('키워드3', max_length=12, null=True)
    content    = models.TextField('내용', null=False)
    summary    = models.TextField('요악', null=False)

    def __str__(self):
        return self.title

