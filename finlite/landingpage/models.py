from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

def validate_max_digits(value):
    max_digits = 9
    if value >= 10**max_digits:
        raise ValidationError(f'Įmonės kodas negali būti didesnis nei {max_digits} skaitmenys.')

class Company(models.Model):
    company_name = models.CharField(max_length=100)
    company_id = models.PositiveIntegerField(validators=[validate_max_digits])
    company_address = models.CharField(max_length=100)
    company_city = models.CharField(max_length=20)
    company_post = models.PositiveIntegerField(validators=[validate_max_digits])
    company_email = models.EmailField(max_length=50)
    company_website = models.URLField(blank=True, null=True)
    company_client_from = models.DateTimeField(default=timezone.now)
    company_user = models.ManyToManyField(User)

    
    
