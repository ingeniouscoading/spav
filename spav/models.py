from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Noticeboard(models.Model):
    notice_title = models.CharField(max_length=100)
    notice_attachment = models.FileField( verbose_name='Attachment', upload_to='noticeboard', null=True)
    notice_link = models.URLField( verbose_name='URL', max_length=200, null=True)
    notice_uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    notice_created_at = models.DateTimeField(auto_now_add=True)
    notice_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.notice_title
    
