from django.db import models
  

class Mynote(models.Model):
    auther     = models.CharField('작성자', max_length=16, null=False)
    class_id = models.CharField('강의아이디', max_length=16, null=False)
    title      = models.CharField('제목', max_length=126, null=False)
    content    = models.TextField('내용', null=False)
    keyword    = models.TextField('키워드', null=False)
    summary    = models.TextField('요악', null=False)

