from django.db import models

class Department(models.Model):
    '''
    description: This class creates a department and its properties
    author: David Everett
    properties:
      name: The name property will contain the name of the department.
      budget: The budget property will be a float that defines the max spending for that department.
    '''

    name = models.CharField(max_length=50)
    budget = models.FloatField()
    

    class Meta:
        verbose_name = ("department")
        verbose_name_plural = ("departments")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("department_detail", kwargs={"pk": self.pk})
