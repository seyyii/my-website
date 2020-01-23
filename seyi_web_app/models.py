from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Service(models.Model):
    srv_title = models.CharField(max_length=150, verbose_name='Service Title')
    srv_img = models.ImageField(null=True, upload_to='img_uploads', blank=True, verbose_name='Service Image')
    srv_content = models.TextField(blank=True, verbose_name='Service Content')

    def __str__(self):
        return self.srv_title


class Portfolio(models.Model):
    port_title = models.CharField(max_length=150, verbose_name='Website Name')
    port_link = models.URLField(null=True, max_length=150, verbose_name='Web link')
    port_img = models.ImageField(null=True, upload_to='img_uploads', blank=True, verbose_name='Post Image')
    created_date = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    def __str__(self):
        return self.port_title 


class Client(models.Model):
    cl_name = models.CharField(max_length=150, verbose_name='Client Name')
    cl_img = models.ImageField(null=True, upload_to='img_uploads', blank=True, verbose_name='Client Image')
    cl_comment = models.TextField(blank=True, verbose_name='Client Commentt')

    def __str__(self):
        return self.cl_name


class Subscribe(models.Model):
    sc_email = models.EmailField(null=True, verbose_name='')

    def __str__(self):
        return self.sc_email

class Mycv(models.Model):
    name = models.CharField(default= '', max_length=40)
    mycv_file = models.FileField(null=True, verbose_name='mycv',upload_to='pdf')

    def __str__(self):
        return self.name       

    def get_absolute_url(self):
        return self.mycv_file
