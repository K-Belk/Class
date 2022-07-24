
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from datetime import date


def validate_stroke(stroke):
    allowed_strokes = ['front crawl', 'butterfly', 'breast', 'back','freestyle']
    if stroke not in allowed_strokes:
        raise ValidationError((f'{stroke} is not a allowed stroke'))

def validate_date(record_date):
    if record_date > date.today():
        raise ValidationError(f'{record_date} cannot be if the future')

class SwimRecord(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    team_name = models.CharField(max_length=200)
    relay = models.BooleanField()
    stroke = models.CharField(max_length=50, validators=[validate_stroke])
    distance = models.IntegerField(validators=[MinValueValidator(50)])
    record_date = models.DateTimeField(validators=[validate_date])
    # record_broken_date = models.DateTimeField()
