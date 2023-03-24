from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class DevelopingCompany(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Platform(models.Model):
    name = models.CharField(max_length=200)
    
    developingCompany =  models.ForeignKey(DevelopingCompany, on_delete=models.CASCADE, null=True) #TODO change the default parameter, remove null

    def __str__(self) -> str:
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)

    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    developingCompany = models.ForeignKey(DevelopingCompany, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
