from django.db import models

# Create your models here.
class Worker(models.Model):
    wid = models.IntegerField(unique=True)
    wfirstname = models.CharField(max_length=50)
    wlastname = models.CharField(max_length=50)
    wsalary = models.FloatField()
    waddress = models.CharField(max_length=50)

    def __str__(self):
        return str(self.wid)

    def __repr__(self):
        return str(self.wid)




