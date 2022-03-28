from django.db import models

GENDER_CHOICES = (('female', 'Female'), ('male', 'Male'))


class Patient(models.Model):
    name = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    birth_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def birth_date_formate(self):
        return self.birth_date.strftime('%d/%m/%Y')
