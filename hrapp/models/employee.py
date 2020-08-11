from django.db import models
from .department import Department

class Employee(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    start_date = models.DateField()
    is_supervisor = models.BooleanField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = ("employee")
        verbose_name_plural = ("employees")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("employee_detail", kwargs={"pk": self.pk})
