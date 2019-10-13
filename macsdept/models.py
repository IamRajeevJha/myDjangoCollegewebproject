from django.db import models


# Create your models here.
class NoticeText(models.Model):
    subject = models.CharField(max_length=500)
    content = models.TextField()
    date = models.DateField()
    isStaff = models.BooleanField(default=False)
    isStudent = models.BooleanField(default=False)
    isTeacher = models.BooleanField(default=False)
    isAll = models.BooleanField(default=False)
    isResearcher = models.BooleanField(default=False)
    isApproved = models.BooleanField(default=False)
