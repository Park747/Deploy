from django.db import models

# Create your models here.
# 방명록 모델 / 신청곡 모델 / 댓글 모델

class visitorLog(models.Model):
    visitorName = models.CharField('NAME', max_length=50)
    title = models.CharField('TITLE', max_length=100)
    visitorLog = models.TextField('CONTENT', default='')
    visitedDate = models.CharField('DATE', max_length=100, default='')

    def __str__(self):
        return self.title


class Comments(models.Model):
    visitorlog = models.ForeignKey(visitorLog, on_delete=models.CASCADE, related_name='comments', default='', null=True)
    commentContent = models.TextField('COMMENT', default='')

class songRequest(models.Model):
    songName = models.CharField('songName', max_length=100)
    userName = models.CharField('userName', max_length=100)

    def __str__(self):
        return self.songName




