from django.db import models


class Path(models.Model):  # p.studen_set.all() / p.students.all()
    path_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.path_name}"


class Student(models.Model):  # a.path.pathname
    path = models.ForeignKey(
        Path, related_name='students', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
