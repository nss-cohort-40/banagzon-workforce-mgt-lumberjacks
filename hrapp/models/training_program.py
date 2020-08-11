from django.db import models

class Training_Program(models.Model):

    program_name = models.CharField(max_length=100)
    program_description = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    max_attendees = models.IntegerField((""))

    class Meta:
        verbose_name = ("Training Program")
        verbose_name_plural = ("Training Programs")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
