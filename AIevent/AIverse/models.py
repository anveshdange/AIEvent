from django.db import models


class AIverse(models.Model):
    Name = models.CharField(max_length=100)
    Event = models.CharField(max_length=30)
    Branch = models.CharField(max_length=100)
    Year = models.CharField(max_length=30)
    Email = models.EmailField(max_length=30)
    Contact = models.CharField(max_length=10)
    Team_Size = models.CharField(max_length=10)
    Team_member = models.CharField(max_length=100, null=True)
    Screenshot = models.ImageField(upload_to="Event/images", null=True)
    Transaction_ID = models.CharField(max_length=40)
    Date = models.DateField(auto_now_add=True)




    def __str__(self):
        return self.Name

