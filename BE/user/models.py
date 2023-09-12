from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True) #diary id 값
    username = models.CharField(max_length=32, unique=True, verbose_name='usernmae')
    password = models.CharField(max_length=100, verbose_name='password')
    start_period = models.DateField(max_length=64, verbose_name='start period')
    end_period = models.DateField(max_length=64, verbose_name='end period')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'
        verbose_name = 'user'