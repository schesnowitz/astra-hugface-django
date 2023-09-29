from django.db import models

class DataSet(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return f"{self.name}"
    

class Data(models.Model):
    data_set = models.ForeignKey(DataSet, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    content = models.TextField()
    def __str__(self):
        return f"{self.data_set.name} : {self.description}"