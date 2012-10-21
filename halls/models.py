from django.db import models

class Hall(models.Model):
    name = models.CharField(max_length=50)
    lat = models.FloatField()
    lon = models.FloatField()
    address = models.CharField(max_length=60)
    def __unicode__(self):
        return self.name

class Hour(models.Model):
    MEAL_TYPES = (
        ('BRK', 'Breakfast'),
        ('BRU', 'Brunch'),
        ('LUN', 'Lunch'),
        ('DIN', 'Dinner'),
        ('LAT', 'Late Night'),
        ('RET', 'Retail'),
    )

    DAY_CHOICES = (
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    )

    host_hall = models.ForeignKey(Hall)
    day = models.IntegerField(choices=DAY_CHOICES)
    meal_type = models.CharField(max_length=3, choices=MEAL_TYPES)
    start_hour = models.IntegerField()
    start_minute = models.IntegerField()
    end_hour = models.IntegerField()
    end_minute = models.IntegerField()
    def __unicode__(self):
        return u'%s hours on %s for %s' % (self.host_hall, self.day, self.meal_type)


'''
class Meal(models.Model):
    MEAL_TYPES = (
        ('BRK', 'Breakfast'),
        ('BRU', 'Brunch'),
        ('LUN', 'Lunch'),
        ('DIN', 'Dinner'),
        ('LAT', 'Late Night'),
    )

    meal_name = models.CharField(max_length=50)
    meal_type = models.CharField(max_length=3, choices=MEAL_TYPES)
    def __unicode__(self):
        return u'%s' % self.meal_name

class Menu(models.Model):
    DAY_CHOICES = (
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
        )
    meal_id = models.ForeignKey(Meal)
    host_hall = models.ForeignKey(Hall)
    day = models.IntegerField(choices=DAY_CHOICES)

'''