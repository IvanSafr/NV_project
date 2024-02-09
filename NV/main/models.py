from django.db import models

# Create your models here.


from django.db import models

# Create your models here.

# Класс провессий/профилей/ специальностей
class Profession(models.Model):
    id = models.AutoField(primary_key=True)
    profession = models.CharField(max_length=40)

    class Meta():
        verbose_name = "Специальности"

    def _str__(self):
        return self.profession

# Сотрудники
class People(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=200)
    password = models.CharField(max_length=5)
    profile = models.ForeignKey('Profession', on_delete=models.CASCADE)
    discription = models.TextField()

    class Meta():
        verbose_name = "Сотрудники"

    def _str__(self):
        return self.name

# Посещения
class VisRate(models.Model):
    id = models.AutoField(primary_key=True)

    man = models.ForeignKey('People', on_delete=models.CASCADE)

    date = models.DateField(auto_now_add=True)

    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta():
        verbose_name = "Посещаемость"