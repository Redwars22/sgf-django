from django.db import models

class Employee(models.Model):
    employee_id = models.CharField(max_length=20, verbose_name="ID")
    employee_name = models.CharField(max_length=100, verbose_name="Nome")
    employee_email = models.EmailField(max_length=100, verbose_name="E-mail")
    employee_contacts = models.CharField(max_length=20, verbose_name="Contatos")

    def __str__(self):
        return self.employee_name

    class Meta:
        app_label = 'djcrud'