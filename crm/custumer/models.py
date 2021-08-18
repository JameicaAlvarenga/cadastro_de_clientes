from django.db import models

# Create your models here.
class Custumer(models.Model):
    frist_name = models.CharField(max_length=38)
    last_name = models.CharField(max_length=50)
    email=models.EmailField()
    brith_date = models.DateField()
    area_code = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=9)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    crate_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.frist_name}{self.last_name}"



