from django.db import models

from django import forms

# Create your models here.
class ExampleModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ExampleForm(forms.ModelForm):
    class Meta:
        verbose_name = 'Example Form'
        verbose_name_plural = 'Example Forms'
        model = ExampleModel
        fields = ['name']