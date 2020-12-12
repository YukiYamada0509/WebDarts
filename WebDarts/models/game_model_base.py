from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class game_model_base(models.Model):
    user_id = models.IntegerField()
    start_time = models.DateTimeField('start time')
    opponent_id = models.IntegerField()
    round_no = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])
    first_throw = models.CharField(max_length=5)
    second_throw = models.CharField(max_length=5)
    third_thorow = models.CharField(max_length=5)